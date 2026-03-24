/**
 * EcfClient.h
 *
 * High-level client for the ECF DGII API.
 * Wraps the auto-generated API classes and provides a sendEcf method
 * that handles routing, polling, and error handling.
 */

#ifndef ECF_DGII_CLIENT_ECFCLIENT_H_
#define ECF_DGII_CLIENT_ECFCLIENT_H_

#include "ecf-dgii-client/ApiClient.h"
#include "ecf-dgii-client/ApiConfiguration.h"
#include "ecf-dgii-client/api/EcfApi.h"
#include "ecf-dgii-client/api/CompanyApi.h"
#include "ecf-dgii-client/api/RecepcionApi.h"
#include "ecf-dgii-client/api/DgiiApi.h"
#include "ecf-dgii-client/api/ApiKeyApi.h"
#include "ecf-dgii-client/model/ECF.h"
#include "ecf-dgii-client/model/EcfResponse.h"
#include "ecf-dgii-client/model/EcfProgress.h"
#include "ecf-dgii-client/model/TipoeCFType.h"

#include <string>
#include <memory>
#include <functional>
#include <stdexcept>
#include <chrono>

namespace ecf_dgii {

using namespace org::openapitools::client::api;
using namespace org::openapitools::client::model;

/**
 * Configuration for the ECF DGII client.
 */
struct EcfClientConfig {
    /// JWT Bearer token for API authentication.
    /// Falls back to ECF_API_KEY environment variable if empty.
    std::string apiKey;

    /// Target environment: "test", "cert", or "prod". Defaults to "test".
    std::string environment = "test";

    /// Base URL override. Takes precedence over environment.
    /// Falls back to ECF_API_URL environment variable if empty.
    std::string baseUrl;
};

/**
 * Options for polling the ECF status.
 */
struct PollingOptions {
    /// Initial delay between polls. Default: 1000ms.
    std::chrono::milliseconds initialDelay{1000};

    /// Maximum delay between polls. Default: 30000ms.
    std::chrono::milliseconds maxDelay{30000};

    /// Maximum number of retries. Default: 60.
    int maxRetries = 60;

    /// Backoff multiplier. Default: 2.0.
    double backoffMultiplier = 2.0;

    /// Total timeout. Default: 0 (no timeout).
    std::chrono::milliseconds timeout{0};
};

/**
 * Exception thrown when ECF processing results in an error.
 */
class EcfError : public std::runtime_error {
public:
    EcfError(const std::string& message, std::shared_ptr<EcfResponse> response)
        : std::runtime_error(message), m_response(std::move(response)) {}

    std::shared_ptr<EcfResponse> getResponse() const { return m_response; }

private:
    std::shared_ptr<EcfResponse> m_response;
};

/**
 * Exception thrown when polling exceeds maximum retries.
 */
class PollingMaxRetriesError : public std::runtime_error {
public:
    explicit PollingMaxRetriesError(int retries)
        : std::runtime_error("Polling exceeded maximum retries (" + std::to_string(retries) + ")") {}
};

/**
 * Exception thrown when polling times out.
 */
class PollingTimeoutError : public std::runtime_error {
public:
    PollingTimeoutError() : std::runtime_error("Polling timed out") {}
};

/**
 * High-level client for the ECF DGII API.
 *
 * Provides direct access to all API endpoints via the raw API objects,
 * plus a high-level sendEcf() method that handles routing, polling,
 * and error handling automatically.
 */
class EcfClient {
public:
    explicit EcfClient(const EcfClientConfig& config);

    // -------------------------------------------------------------------------
    // High-level ECF send + poll
    // -------------------------------------------------------------------------

    /**
     * Send an ECF and poll until processing completes.
     *
     * Determines the correct endpoint from ecf.encabezado.idDoc.tipoeCF,
     * posts the ECF, then polls until progress is Finished or Error.
     *
     * @param ecf The ECF document to send.
     * @param options Polling configuration (optional).
     * @return The final EcfResponse when processing is complete.
     * @throws EcfError if processing results in an error.
     * @throws PollingMaxRetriesError if max retries exceeded.
     * @throws PollingTimeoutError if timeout exceeded.
     * @throws std::invalid_argument if required fields are missing.
     */
    pplx::task<std::shared_ptr<EcfResponse>> sendEcf(
        std::shared_ptr<ECF> ecf,
        const PollingOptions& options = PollingOptions{}
    );

    // -------------------------------------------------------------------------
    // Raw API access
    // -------------------------------------------------------------------------

    /** Access the underlying EcfApi for direct endpoint calls. */
    std::shared_ptr<EcfApi> ecfApi() const { return m_ecfApi; }

    /** Access the underlying CompanyApi for direct endpoint calls. */
    std::shared_ptr<CompanyApi> companyApi() const { return m_companyApi; }

    /** Access the underlying RecepcionApi for direct endpoint calls. */
    std::shared_ptr<RecepcionApi> recepcionApi() const { return m_recepcionApi; }

    /** Access the underlying DgiiApi for direct endpoint calls. */
    std::shared_ptr<DgiiApi> dgiiApi() const { return m_dgiiApi; }

    /** Access the underlying ApiKeyApi for direct endpoint calls. */
    std::shared_ptr<ApiKeyApi> apiKeyApi() const { return m_apiKeyApi; }

private:
    /**
     * Route an ECF to the correct typed endpoint based on tipoeCF.
     */
    pplx::task<std::shared_ptr<EcfResponse>> postEcf(
        TipoeCFType::eTipoeCFType tipoeCF,
        std::shared_ptr<ECF> ecf
    );

    /**
     * Poll until the predicate returns true, using exponential backoff.
     */
    pplx::task<std::shared_ptr<EcfResponse>> pollUntilComplete(
        std::function<pplx::task<std::shared_ptr<EcfResponse>>()> fn,
        std::function<bool(const std::shared_ptr<EcfResponse>&)> isComplete,
        const PollingOptions& options
    );

    static utility::string_t resolveBaseUrl(const EcfClientConfig& config);
    static std::string resolveApiKey(const EcfClientConfig& config);

    std::shared_ptr<ApiClient> m_apiClient;
    std::shared_ptr<EcfApi> m_ecfApi;
    std::shared_ptr<CompanyApi> m_companyApi;
    std::shared_ptr<RecepcionApi> m_recepcionApi;
    std::shared_ptr<DgiiApi> m_dgiiApi;
    std::shared_ptr<ApiKeyApi> m_apiKeyApi;
};

/**
 * Configuration for the read-only frontend client.
 */
struct EcfFrontendClientConfig {
    /// Callback that returns a read-only API token (REQUIRED).
    /// Typically calls your backend's GET /ecf-token endpoint.
    std::function<std::string()> getToken;

    /// Callback to cache a token (OPTIONAL).
    /// Default: encrypts and writes the token to a file on disk.
    std::function<void(const std::string&)> cacheToken;

    /// Callback to retrieve a cached token (OPTIONAL).
    /// Default: reads from the encrypted file on disk.
    /// Must return an empty string if no cached token is found.
    std::function<std::string()> getCachedToken;

    /// Target environment: "test", "cert", or "prod". Defaults to "test".
    std::string environment = "test";

    /// Base URL override. Takes precedence over environment.
    /// Falls back to ECF_API_URL environment variable if empty.
    std::string baseUrl;
};

/**
 * Read-only frontend client for the ECF DGII API.
 *
 * Provides access only to EcfApi and CompanyApi for querying and searching
 * ECFs and companies. Does not support sending ECFs, managing API keys,
 * or any write/delete operations.
 *
 * Token management is handled via callbacks:
 * - getToken (REQUIRED): fetches a fresh read-only token from your backend
 * - cacheToken (OPTIONAL): persists the token; defaults to encrypted file on disk
 * - getCachedToken (OPTIONAL): retrieves a cached token; defaults to encrypted file on disk
 */
class EcfFrontendClient {
public:
    explicit EcfFrontendClient(const EcfFrontendClientConfig& config);

    /** Access the underlying EcfApi for direct endpoint calls. */
    std::shared_ptr<EcfApi> ecfApi() const { return m_ecfApi; }

    /** Access the underlying CompanyApi for direct endpoint calls. */
    std::shared_ptr<CompanyApi> companyApi() const { return m_companyApi; }

private:
    static utility::string_t resolveBaseUrl(const EcfFrontendClientConfig& config);

    /// Resolve the token: try cache first, then fetch via getToken and cache it.
    std::string resolveToken();

    /// Default file-based cache: write encrypted token to disk.
    static void defaultCacheToken(const std::string& token);

    /// Default file-based cache: read encrypted token from disk (empty if not found).
    static std::string defaultGetCachedToken();

    EcfFrontendClientConfig m_config;
    std::shared_ptr<ApiClient> m_apiClient;
    std::shared_ptr<EcfApi> m_ecfApi;
    std::shared_ptr<CompanyApi> m_companyApi;
};

} // namespace ecf_dgii

#endif /* ECF_DGII_CLIENT_ECFCLIENT_H_ */
