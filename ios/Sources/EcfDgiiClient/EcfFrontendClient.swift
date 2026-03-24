//
// EcfFrontendClient.swift
//
// Cliente de solo lectura para la API de ECF DGII.
// Solo expone endpoints GET — diseñado para uso en frontend/móvil
// con un token de solo lectura con alcance a un RNC específico.
//

import Foundation
#if canImport(Security)
import Security
#endif

// MARK: - Keychain Helper

/// Simple Keychain wrapper for storing the read-only ECF token.
private enum KeychainTokenStore {
    static let service = "ecf-dgii-token"
    static let account = "api-key"

    static func save(_ token: String) throws {
        let data = Data(token.utf8)

        // Delete any existing item first
        let deleteQuery: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
        ]
        SecItemDelete(deleteQuery as CFDictionary)

        let addQuery: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
            kSecValueData as String: data,
            kSecAttrAccessible as String: kSecAttrAccessibleAfterFirstUnlock,
        ]
        let status = SecItemAdd(addQuery as CFDictionary, nil)
        guard status == errSecSuccess else {
            throw KeychainError.unableToSave(status)
        }
    }

    static func load() throws -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne,
        ]
        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)

        switch status {
        case errSecSuccess:
            guard let data = result as? Data, let token = String(data: data, encoding: .utf8) else {
                return nil
            }
            return token
        case errSecItemNotFound:
            return nil
        default:
            throw KeychainError.unableToLoad(status)
        }
    }

    enum KeychainError: Error, LocalizedError {
        case unableToSave(OSStatus)
        case unableToLoad(OSStatus)

        var errorDescription: String? {
            switch self {
            case .unableToSave(let status):
                return "Keychain save failed with status \(status)"
            case .unableToLoad(let status):
                return "Keychain load failed with status \(status)"
            }
        }
    }
}

/// Cliente de solo lectura para la API de ECF DGII.
///
/// Expone únicamente operaciones de consulta (GET). No permite enviar,
/// modificar ni eliminar comprobantes. Ideal para aplicaciones frontend/móviles
/// que usan un token de solo lectura generado por el backend.
///
/// El cliente gestiona el token automáticamente:
/// 1. Busca un token en cache (Keychain por defecto)
/// 2. Si no existe, llama a `getToken()` y lo almacena con `cacheToken()`
/// 3. Si recibe un 401, refresca el token y reintenta la petición
///
/// ```swift
/// let client = EcfFrontendClient(
///     getToken: {
///         let (data, _) = try await URLSession.shared.data(from: tokenURL)
///         return try JSONDecoder().decode(TokenResponse.self, from: data).apiKey
///     },
///     environment: .prod
/// )
/// let ecfs = try await client.queryEcf(rnc: "131880681", encf: "E310000051630")
/// ```
public final class EcfFrontendClient: Sendable {

    /// Closure that fetches a fresh read-only token from the consumer's backend.
    private let getToken: @Sendable () async throws -> String

    /// Closure that persists a token. Defaults to Keychain storage.
    private let cacheToken: @Sendable (String) async throws -> Void

    /// Closure that retrieves a previously cached token. Defaults to Keychain read.
    private let getCachedToken: @Sendable () async throws -> String?

    /// Target environment (test, cert, prod).
    private let environment: EcfEnvironment

    /// Optional base URL override.
    private let baseUrl: String?

    /// Creates a new EcfFrontendClient with token management closures.
    ///
    /// - Parameters:
    ///   - getToken: **Required.** Closure that returns a fresh read-only Bearer token.
    ///     Typically calls your backend's `/ecf-token` endpoint.
    ///   - cacheToken: Optional closure to persist the token. Defaults to Keychain storage
    ///     with service name `"ecf-dgii-token"`.
    ///   - getCachedToken: Optional closure to retrieve a cached token. Defaults to reading
    ///     from Keychain.
    ///   - environment: Target environment. Defaults to `.test`.
    ///   - baseUrl: Optional base URL override. Takes precedence over `environment`.
    public init(
        getToken: @escaping @Sendable () async throws -> String,
        cacheToken: (@Sendable (String) async throws -> Void)? = nil,
        getCachedToken: (@Sendable () async throws -> String?)? = nil,
        environment: EcfEnvironment = .test,
        baseUrl: String? = nil
    ) {
        self.getToken = getToken
        self.cacheToken = cacheToken ?? { token in
            try KeychainTokenStore.save(token)
        }
        self.getCachedToken = getCachedToken ?? {
            try KeychainTokenStore.load()
        }
        self.environment = environment
        self.baseUrl = baseUrl
    }

    // MARK: - Internal Token Management

    /// Resolves a valid token: checks cache first, then fetches and caches a new one.
    private func resolveToken() async throws -> String {
        if let cached = try await getCachedToken() {
            return cached
        }
        let token = try await getToken()
        try await cacheToken(token)
        return token
    }

    /// Builds an `EcfDgiiClientAPIConfiguration` for the given token.
    private func makeConfiguration(token: String) -> EcfDgiiClientAPIConfiguration {
        let resolvedBaseUrl = baseUrl ?? environment.baseUrl
        return EcfDgiiClientAPIConfiguration(
            basePath: resolvedBaseUrl,
            customHeaders: ["Authorization": "Bearer \(token)"]
        )
    }

    /// Executes an API call with automatic token resolution and 401 retry.
    ///
    /// 1. Resolve token (cache → fetch → cache)
    /// 2. Execute the request
    /// 3. On 401, refresh token and retry once
    private func withAuth<T>(_ operation: @Sendable (EcfDgiiClientAPIConfiguration) async throws(ErrorResponse) -> T) async throws(ErrorResponse) -> T {
        let token: String
        do {
            token = try await resolveToken()
        } catch {
            throw ErrorResponse.error(0, nil, nil, error)
        }
        let config = makeConfiguration(token: token)

        do {
            return try await operation(config)
        } catch let errorResponse as ErrorResponse {
            // Check if 401 — refresh token and retry
            if case .error(let statusCode, _, _, _) = errorResponse, statusCode == 401 {
                let freshToken: String
                do {
                    freshToken = try await getToken()
                    try await cacheToken(freshToken)
                } catch {
                    throw ErrorResponse.error(0, nil, nil, error)
                }
                let freshConfig = makeConfiguration(token: freshToken)
                return try await operation(freshConfig)
            }
            throw errorResponse
        }
    }

    // MARK: - ECF Query Operations

    /// Query ECFs by RNC and eNCF.
    public func queryEcf(rnc: String, encf: String, includeEcfContent: Bool? = nil) async throws(ErrorResponse) -> [EcfResponse] {
        try await withAuth { config in
            try await EcfAPI.queryEcf(rnc: rnc, encf: encf, includeEcfContent: includeEcfContent, apiConfiguration: config)
        }
    }

    /// Search ECFs for a specific RNC.
    public func searchEcfs(
        rnc: String,
        encfs: [String]? = nil,
        ids: [UUID]? = nil,
        tiposEcfs: [AllTipoECFTypes]? = nil,
        includeEcfContent: Bool? = nil,
        fromFechaEmision: Date? = nil,
        toFechaEmision: Date? = nil,
        amountFrom: Double? = nil,
        amountTo: Double? = nil,
        page: Int? = nil,
        limit: Int? = nil
    ) async throws(ErrorResponse) -> PaginatedApiResultOfEcfResponse {
        try await withAuth { config in
            try await EcfAPI.searchEcfs(
                rnc: rnc,
                encfs: encfs,
                ids: ids,
                tiposEcfs: tiposEcfs,
                includeEcfContent: includeEcfContent,
                fromFechaEmision: fromFechaEmision,
                toFechaEmision: toFechaEmision,
                amountFrom: amountFrom,
                amountTo: amountTo,
                page: page,
                limit: limit,
                apiConfiguration: config
            )
        }
    }

    /// Search all ECFs across all companies.
    public func searchAllEcfs(
        encfs: [String]? = nil,
        ids: [UUID]? = nil,
        tiposEcfs: [AllTipoECFTypes]? = nil,
        includeEcfContent: Bool? = nil,
        fromFechaEmision: Date? = nil,
        toFechaEmision: Date? = nil,
        amountFrom: Double? = nil,
        amountTo: Double? = nil,
        page: Int? = nil,
        limit: Int? = nil
    ) async throws(ErrorResponse) -> PaginatedApiResultOfEcfResponse {
        try await withAuth { config in
            try await EcfAPI.searchAllEcfs(
                encfs: encfs,
                ids: ids,
                tiposEcfs: tiposEcfs,
                includeEcfContent: includeEcfContent,
                fromFechaEmision: fromFechaEmision,
                toFechaEmision: toFechaEmision,
                amountFrom: amountFrom,
                amountTo: amountTo,
                page: page,
                limit: limit,
                apiConfiguration: config
            )
        }
    }

    /// Get a specific ECF by message ID.
    public func getEcfById(rnc: String, id: UUID, includeEcfContent: Bool? = nil) async throws(ErrorResponse) -> [EcfResponse] {
        try await withAuth { config in
            try await EcfAPI.getEcfById(rnc: rnc, id: id, includeEcfContent: includeEcfContent, apiConfiguration: config)
        }
    }

    // MARK: - Company Operations

    /// List companies with optional filters.
    public func getCompanies(
        rncs: [String]? = nil,
        names: [String]? = nil,
        page: Int? = nil,
        limit: Int? = nil
    ) async throws(ErrorResponse) -> PaginatedApiResultOfCompanyResponse {
        try await withAuth { config in
            try await CompanyAPI.getCompanies(rncs: rncs, names: names, page: page, limit: limit, apiConfiguration: config)
        }
    }

    /// Get a company by RNC.
    public func getCompanyByRnc(rnc: String) async throws(ErrorResponse) -> CompanyResponse {
        try await withAuth { config in
            try await CompanyAPI.getCompanyByRnc(rnc: rnc, apiConfiguration: config)
        }
    }
}
