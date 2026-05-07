//
// EcfClient.swift
//
// High-level client for the ECF DGII API with automatic routing and polling.
//

import Foundation

/// Environment options for the ECF API.
public enum EcfEnvironment: String, Sendable {
    case test
    case cert
    case prod

    var baseUrl: String {
        switch self {
        case .test: return "https://api.test.ecfx.ssd.com.do"
        case .cert: return "https://api.cert.ecfx.ssd.com.do"
        case .prod: return "https://api.prod.ecfx.ssd.com.do"
        }
    }
}

/// Configuration for polling behavior.
public struct PollingOptions: Sendable {
    /// Initial delay between polls in seconds. Default: 1.0
    public var initialDelay: TimeInterval
    /// Maximum delay between polls in seconds. Default: 30.0
    public var maxDelay: TimeInterval
    /// Maximum number of retries. Default: 60
    public var maxRetries: Int
    /// Backoff multiplier. Default: 2.0
    public var backoffMultiplier: Double
    /// Total timeout in seconds. Optional.
    public var timeout: TimeInterval?

    public init(
        initialDelay: TimeInterval = 1.0,
        maxDelay: TimeInterval = 30.0,
        maxRetries: Int = 60,
        backoffMultiplier: Double = 2.0,
        timeout: TimeInterval? = nil
    ) {
        self.initialDelay = initialDelay
        self.maxDelay = maxDelay
        self.maxRetries = maxRetries
        self.backoffMultiplier = backoffMultiplier
        self.timeout = timeout
    }

    public static let `default` = PollingOptions()
}

/// Error thrown when ECF processing fails at DGII.
public struct EcfProcessingError: Error, Sendable {
    public let message: String
    public let response: EcfResponse

    public init(message: String, response: EcfResponse) {
        self.message = message
        self.response = response
    }
}

/// Error thrown when polling times out.
public struct PollingTimeoutError: Error, Sendable {
    public let message: String
    public init(message: String = "Polling timed out") {
        self.message = message
    }
}

/// Error thrown when polling exceeds maximum retries.
public struct PollingMaxRetriesError: Error, Sendable {
    public let maxRetries: Int
    public init(maxRetries: Int) {
        self.maxRetries = maxRetries
    }
}

/// High-level client for the ECF DGII API.
///
/// Wraps the auto-generated API classes and provides convenient `sendEcf`
/// overloads — one per electronic-receipt type — that POST the document,
/// poll until processing completes, and surface errors.
///
/// Usage:
/// ```swift
/// let client = EcfClient(apiKey: "your-jwt-token", environment: .test)
/// let result = try await client.sendEcf(ecf: myEcf31)
/// ```
public final class EcfClient: Sendable {

    /// The API configuration used for all requests.
    public let apiConfiguration: EcfDgiiClientAPIConfiguration

    /// Creates a new EcfClient.
    ///
    /// - Parameters:
    ///   - apiKey: JWT Bearer token for authentication.
    ///   - environment: Target environment. Defaults to `.test`.
    ///   - baseUrl: Optional base URL override. Takes precedence over `environment`.
    public init(apiKey: String, environment: EcfEnvironment = .test, baseUrl: String? = nil) {
        let resolvedBaseUrl = baseUrl ?? environment.baseUrl
        self.apiConfiguration = EcfDgiiClientAPIConfiguration(
            basePath: resolvedBaseUrl,
            customHeaders: ["Authorization": "Bearer \(apiKey)"]
        )
    }

    // MARK: - Send ECF (per type)

    /// Send a Factura de Crédito Fiscal Electrónica (e-CF 31) and poll until completion.
    public func sendEcf(ecf: Ecf31ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf31(ecf31ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Factura de Consumo Electrónica (e-CF 32) and poll until completion.
    public func sendEcf(ecf: Ecf32ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf32(ecf32ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Nota de Débito Electrónica (e-CF 33) and poll until completion.
    public func sendEcf(ecf: Ecf33ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf33(ecf33ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Nota de Crédito Electrónica (e-CF 34) and poll until completion.
    public func sendEcf(ecf: Ecf34ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf34(ecf34ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Compras Electrónico (e-CF 41) and poll until completion.
    public func sendEcf(ecf: Ecf41ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf41(ecf41ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Gastos Menores Electrónico (e-CF 43) and poll until completion.
    public func sendEcf(ecf: Ecf43ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf43(ecf43ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Regímenes Especiales Electrónico (e-CF 44) and poll until completion.
    public func sendEcf(ecf: Ecf44ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf44(ecf44ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Gubernamental Electrónico (e-CF 45) and poll until completion.
    public func sendEcf(ecf: Ecf45ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf45(ecf45ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Comprobante de Exportaciones Electrónico (e-CF 46) and poll until completion.
    public func sendEcf(ecf: Ecf46ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf46(ecf46ECF: ecf, apiConfiguration: $0) }
        )
    }

    /// Send a Comprobante para Pagos al Exterior Electrónico (e-CF 47) and poll until completion.
    public func sendEcf(ecf: Ecf47ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        try await sendInternal(
            rnc: ecf.encabezado.emisor.rncEmisor,
            encf: ecf.encabezado.idDoc.encf,
            pollingOptions: pollingOptions,
            post: { try await EcfAPI.recepcionEcf47(ecf47ECF: ecf, apiConfiguration: $0) }
        )
    }

    // MARK: - Private helpers

    private func sendInternal(
        rnc: String,
        encf: String,
        pollingOptions: PollingOptions,
        post: @Sendable (EcfDgiiClientAPIConfiguration) async throws -> EcfResponse
    ) async throws -> EcfResponse {
        let postResponse = try await post(apiConfiguration)

        let result = try await pollUntilComplete(
            pollingOptions: pollingOptions,
            fetch: {
                let responses = try await EcfAPI.queryEcf(
                    rnc: rnc,
                    encf: encf,
                    apiConfiguration: self.apiConfiguration
                )
                let match = responses.first(where: { $0.messageId == postResponse.messageId }) ?? responses.first
                guard let match else {
                    throw NSError(domain: "EcfClient", code: -2, userInfo: [
                        NSLocalizedDescriptionKey: "No ECF response found for rnc/encf"
                    ])
                }
                return match
            },
            isComplete: { response in
                response.progress == .finished || response.progress == .error
            }
        )

        if result.progress == .error {
            throw EcfProcessingError(
                message: result.errors ?? result.mensaje ?? "ECF processing failed",
                response: result
            )
        }

        return result
    }

    private func pollUntilComplete(
        pollingOptions: PollingOptions,
        fetch: @Sendable () async throws -> EcfResponse,
        isComplete: @Sendable (EcfResponse) -> Bool
    ) async throws -> EcfResponse {
        let startTime = Date()
        var delay = pollingOptions.initialDelay
        var retries = 0

        while true {
            try Task.checkCancellation()

            let result = try await fetch()

            if isComplete(result) {
                return result
            }

            retries += 1

            if retries >= pollingOptions.maxRetries {
                throw PollingMaxRetriesError(maxRetries: pollingOptions.maxRetries)
            }

            if let timeout = pollingOptions.timeout,
               Date().timeIntervalSince(startTime) >= timeout {
                throw PollingTimeoutError()
            }

            try await Task.sleep(nanoseconds: UInt64(delay * 1_000_000_000))
            delay = min(delay * pollingOptions.backoffMultiplier, pollingOptions.maxDelay)
        }
    }
}
