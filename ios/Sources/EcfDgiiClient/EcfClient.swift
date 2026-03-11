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

/// Maps TipoeCFType to the API route number.
private let ecfTypeRouteMap: [TipoeCFType: String] = [
    .facturaDeCreditoFiscalElectronica: "31",
    .facturaDeConsumoElectronica: "32",
    .notaDeDebitoElectronica: "33",
    .notaDeCreditoElectronica: "34",
    .comprasElectronico: "41",
    .gastosMenoresElectronico: "43",
    .regimenesEspecialesElectronico: "44",
    .gubernamentalElectronico: "45",
    .comprobanteDeExportacionesElectronico: "46",
    .comprobanteParaPagosAlExteriorElectronico: "47",
]

/// High-level client for the ECF DGII API.
///
/// Wraps the auto-generated API classes and provides a convenient `sendEcf` method
/// that automatically routes ECFs by type, polls for completion, and handles errors.
///
/// Usage:
/// ```swift
/// let client = EcfClient(apiKey: "your-jwt-token", environment: .test)
/// let result = try await client.sendEcf(ecf: myEcf)
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

    // MARK: - Send ECF with polling

    /// Send an ECF and poll until processing completes.
    ///
    /// Determines the correct endpoint from `ecf.encabezado.idDoc.tipoeCF`,
    /// posts the ECF, then polls until `progress` is `Finished` or `Error`.
    ///
    /// - Parameters:
    ///   - ecf: The ECF document to send.
    ///   - pollingOptions: Optional polling configuration.
    /// - Returns: The final `EcfResponse` when processing is complete.
    /// - Throws: `EcfProcessingError` if the ECF was rejected, or other errors for network/polling failures.
    public func sendEcf(ecf: ECF, pollingOptions: PollingOptions = .default) async throws -> EcfResponse {
        let tipoeCF = ecf.encabezado.idDoc.tipoeCF
        guard let route = ecfTypeRouteMap[tipoeCF] else {
            throw NSError(domain: "EcfClient", code: -1, userInfo: [
                NSLocalizedDescriptionKey: "Unknown tipoeCF: \(tipoeCF)"
            ])
        }

        let rnc = ecf.encabezado.emisor.rncEmisor
        let encf = ecf.encabezado.idDoc.encf

        // POST to the typed endpoint
        let postResponse = try await postEcf(route: route, ecf: ecf)

        // Poll until complete
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

    // MARK: - Private helpers

    private func postEcf(route: String, ecf: ECF) async throws -> EcfResponse {
        switch route {
        case "31": return try await EcfAPI.recepcionEcf31(ECF: ecf, apiConfiguration: apiConfiguration)
        case "32": return try await EcfAPI.recepcionEcf32(ECF: ecf, apiConfiguration: apiConfiguration)
        case "33": return try await EcfAPI.recepcionEcf33(ECF: ecf, apiConfiguration: apiConfiguration)
        case "34": return try await EcfAPI.recepcionEcf34(ECF: ecf, apiConfiguration: apiConfiguration)
        case "41": return try await EcfAPI.recepcionEcf41(ECF: ecf, apiConfiguration: apiConfiguration)
        case "43": return try await EcfAPI.recepcionEcf43(ECF: ecf, apiConfiguration: apiConfiguration)
        case "44": return try await EcfAPI.recepcionEcf44(ECF: ecf, apiConfiguration: apiConfiguration)
        case "45": return try await EcfAPI.recepcionEcf45(ECF: ecf, apiConfiguration: apiConfiguration)
        case "46": return try await EcfAPI.recepcionEcf46(ECF: ecf, apiConfiguration: apiConfiguration)
        case "47": return try await EcfAPI.recepcionEcf47(ECF: ecf, apiConfiguration: apiConfiguration)
        default:
            throw NSError(domain: "EcfClient", code: -1, userInfo: [
                NSLocalizedDescriptionKey: "Unknown ECF route: \(route)"
            ])
        }
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
