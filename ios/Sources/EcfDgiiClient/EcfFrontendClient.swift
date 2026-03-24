//
// EcfFrontendClient.swift
//
// Cliente de solo lectura para la API de ECF DGII.
// Solo expone endpoints GET — diseñado para uso en frontend/móvil
// con un token de solo lectura con alcance a un RNC específico.
//

import Foundation

/// Cliente de solo lectura para la API de ECF DGII.
///
/// Expone únicamente operaciones de consulta (GET). No permite enviar,
/// modificar ni eliminar comprobantes. Ideal para aplicaciones frontend/móviles
/// que usan un token de solo lectura generado por el backend.
///
/// ```swift
/// let client = EcfFrontendClient(apiKey: readOnlyToken, environment: .prod)
/// let ecfs = try await client.queryEcf(rnc: "131880681", encf: "E310000051630")
/// ```
public final class EcfFrontendClient: Sendable {

    /// The API configuration used for all requests.
    public let apiConfiguration: EcfDgiiClientAPIConfiguration

    /// Creates a new EcfFrontendClient.
    ///
    /// - Parameters:
    ///   - apiKey: Read-only Bearer token for authentication.
    ///   - environment: Target environment. Defaults to `.test`.
    ///   - baseUrl: Optional base URL override. Takes precedence over `environment`.
    public init(apiKey: String, environment: EcfEnvironment = .test, baseUrl: String? = nil) {
        let resolvedBaseUrl = baseUrl ?? environment.baseUrl
        self.apiConfiguration = EcfDgiiClientAPIConfiguration(
            basePath: resolvedBaseUrl,
            customHeaders: ["Authorization": "Bearer \(apiKey)"]
        )
    }

    // MARK: - ECF Query Operations

    /// Query ECFs by RNC and eNCF.
    public func queryEcf(rnc: String, encf: String, includeEcfContent: Bool? = nil) async throws(ErrorResponse) -> [EcfResponse] {
        try await EcfAPI.queryEcf(rnc: rnc, encf: encf, includeEcfContent: includeEcfContent, apiConfiguration: apiConfiguration)
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
            apiConfiguration: apiConfiguration
        )
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
            apiConfiguration: apiConfiguration
        )
    }

    /// Get a specific ECF by message ID.
    public func getEcfById(rnc: String, id: UUID, includeEcfContent: Bool? = nil) async throws(ErrorResponse) -> [EcfResponse] {
        try await EcfAPI.getEcfById(rnc: rnc, id: id, includeEcfContent: includeEcfContent, apiConfiguration: apiConfiguration)
    }

    // MARK: - Company Operations

    /// List companies with optional filters.
    public func getCompanies(
        rncs: [String]? = nil,
        names: [String]? = nil,
        page: Int? = nil,
        limit: Int? = nil
    ) async throws(ErrorResponse) -> PaginatedApiResultOfCompanyResponse {
        try await CompanyAPI.getCompanies(rncs: rncs, names: names, page: page, limit: limit, apiConfiguration: apiConfiguration)
    }

    /// Get a company by RNC.
    public func getCompanyByRnc(rnc: String) async throws(ErrorResponse) -> CompanyResponse {
        try await CompanyAPI.getCompanyByRnc(rnc: rnc, apiConfiguration: apiConfiguration)
    }
}
