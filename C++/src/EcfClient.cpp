/**
 * EcfClient.cpp
 *
 * High-level client for the ECF DGII API.
 */

#include "ecf-dgii-client/EcfClient.h"

#include <cstdlib>
#include <thread>
#include <algorithm>

namespace ecf_dgii {

using namespace org::openapitools::client::api;
using namespace org::openapitools::client::model;

// ECF type to route number mapping
static const std::map<TipoeCFType::eTipoeCFType, std::string> ECF_TYPE_ROUTE_MAP = {
    { TipoeCFType::eTipoeCFType::FACTURADECREDITOFISCALELECTRONICA, "31" },
    { TipoeCFType::eTipoeCFType::FACTURADECONSUMOELECTRONICA, "32" },
    { TipoeCFType::eTipoeCFType::NOTADEDEBITOELECTRONICA, "33" },
    { TipoeCFType::eTipoeCFType::NOTADECREDITOELECTRONICA, "34" },
    { TipoeCFType::eTipoeCFType::COMPRASELECTRONICO, "41" },
    { TipoeCFType::eTipoeCFType::GASTOSMENORESELECTRONICO, "43" },
    { TipoeCFType::eTipoeCFType::REGIMENESESPECIALESELECTRONICO, "44" },
    { TipoeCFType::eTipoeCFType::GUBERNAMENTALELECTRONICO, "45" },
    { TipoeCFType::eTipoeCFType::COMPROBANTEDEEXPORTACIONESELECTRONICO, "46" },
    { TipoeCFType::eTipoeCFType::COMPROBANTEPARAPAGOSALEXTERIORELECTRONICO, "47" },
};

utility::string_t EcfClient::resolveBaseUrl(const EcfClientConfig& config) {
    if (!config.baseUrl.empty()) {
        return utility::conversions::to_string_t(config.baseUrl);
    }

    const char* envUrl = std::getenv("ECF_API_URL");
    if (envUrl && envUrl[0] != '\0') {
        return utility::conversions::to_string_t(std::string(envUrl));
    }

    static const std::map<std::string, std::string> ENVIRONMENT_URLS = {
        { "test", "https://api.test.ecfx.ssd.com.do" },
        { "cert", "https://api.cert.ecfx.ssd.com.do" },
        { "prod", "https://api.prod.ecfx.ssd.com.do" },
    };

    auto it = ENVIRONMENT_URLS.find(config.environment);
    if (it != ENVIRONMENT_URLS.end()) {
        return utility::conversions::to_string_t(it->second);
    }

    return utility::conversions::to_string_t(std::string("https://api.test.ecfx.ssd.com.do"));
}

std::string EcfClient::resolveApiKey(const EcfClientConfig& config) {
    if (!config.apiKey.empty()) {
        return config.apiKey;
    }

    const char* envKey = std::getenv("ECF_API_KEY");
    if (envKey && envKey[0] != '\0') {
        return std::string(envKey);
    }

    throw std::invalid_argument("API key is required. Set it in EcfClientConfig.apiKey or ECF_API_KEY environment variable.");
}

EcfClient::EcfClient(const EcfClientConfig& config) {
    auto apiConfig = std::make_shared<ApiConfiguration>();
    apiConfig->setBaseUrl(resolveBaseUrl(config));

    std::string apiKey = resolveApiKey(config);
    apiConfig->getDefaultHeaders()[_XPLATSTR("Authorization")] =
        utility::conversions::to_string_t("Bearer " + apiKey);

    m_apiClient = std::make_shared<ApiClient>(apiConfig);
    m_ecfApi = std::make_shared<EcfApi>(m_apiClient);
    m_companyApi = std::make_shared<CompanyApi>(m_apiClient);
    m_recepcionApi = std::make_shared<RecepcionApi>(m_apiClient);
    m_dgiiApi = std::make_shared<DgiiApi>(m_apiClient);
    m_apiKeyApi = std::make_shared<ApiKeyApi>(m_apiClient);
}

pplx::task<std::shared_ptr<EcfResponse>> EcfClient::sendEcf(
    std::shared_ptr<ECF> ecf,
    const PollingOptions& options
) {
    // Validate required fields
    if (!ecf || !ecf->encabezadoIsSet() || !ecf->getEncabezado()) {
        throw std::invalid_argument("ECF must have encabezado");
    }

    auto encabezado = ecf->getEncabezado();

    if (!encabezado->idDocIsSet() || !encabezado->getIdDoc()) {
        throw std::invalid_argument("ECF must have encabezado.idDoc");
    }

    auto idDoc = encabezado->getIdDoc();

    if (!idDoc->tipoeCFIsSet() || !idDoc->getTipoeCF()) {
        throw std::invalid_argument("ECF must have encabezado.idDoc.tipoeCF");
    }

    auto tipoeCF = idDoc->getTipoeCF()->getValue();

    if (ECF_TYPE_ROUTE_MAP.find(tipoeCF) == ECF_TYPE_ROUTE_MAP.end()) {
        throw std::invalid_argument("Unknown tipoeCF value");
    }

    if (!encabezado->emisorIsSet() || !encabezado->getEmisor()) {
        throw std::invalid_argument("ECF must have encabezado.emisor");
    }

    auto emisor = encabezado->getEmisor();

    if (!emisor->rncEmisorIsSet()) {
        throw std::invalid_argument("ECF must have encabezado.emisor.rncEmisor");
    }

    utility::string_t rnc = emisor->getRncEmisor();

    if (!idDoc->encfIsSet()) {
        throw std::invalid_argument("ECF must have encabezado.idDoc.encf");
    }

    utility::string_t encf = idDoc->getEncf();

    // Capture values for the lambda chain
    auto ecfApi = m_ecfApi;

    // POST to the typed endpoint, then poll until complete
    return postEcf(tipoeCF, ecf).then(
        [this, ecfApi, rnc, encf, options](std::shared_ptr<EcfResponse> initialResponse) {
            utility::string_t messageId = initialResponse->getMessageId();

            return pollUntilComplete(
                // Poll function: query ECF status
                [ecfApi, rnc, encf, messageId]() -> pplx::task<std::shared_ptr<EcfResponse>> {
                    return ecfApi->queryEcf(rnc, encf, boost::optional<bool>(false))
                        .then([messageId](std::vector<std::shared_ptr<EcfResponse>> results) -> std::shared_ptr<EcfResponse> {
                            // Find the matching response by messageId
                            for (const auto& r : results) {
                                if (r->messageIdIsSet() && r->getMessageId() == messageId) {
                                    return r;
                                }
                            }
                            // Fall back to first result
                            if (!results.empty()) {
                                return results[0];
                            }
                            throw std::runtime_error("No ECF response found for the given rnc/encf");
                        });
                },
                // Completion predicate
                [](const std::shared_ptr<EcfResponse>& r) -> bool {
                    if (!r || !r->progressIsSet() || !r->getProgress()) {
                        return false;
                    }
                    auto progress = r->getProgress()->getValue();
                    return progress == EcfProgress::eEcfProgress::FINISHED ||
                           progress == EcfProgress::eEcfProgress::ERROR;
                },
                options
            );
        }
    ).then([](std::shared_ptr<EcfResponse> result) -> std::shared_ptr<EcfResponse> {
        // Check if the result is an error
        if (result && result->progressIsSet() && result->getProgress()) {
            if (result->getProgress()->getValue() == EcfProgress::eEcfProgress::ERROR) {
                std::string errorMsg = "ECF processing failed";
                if (result->errorsIsSet()) {
                    errorMsg = utility::conversions::to_utf8string(result->getErrors());
                } else if (result->mensajeIsSet()) {
                    errorMsg = utility::conversions::to_utf8string(result->getMensaje());
                }
                throw EcfError(errorMsg, result);
            }
        }
        return result;
    });
}

pplx::task<std::shared_ptr<EcfResponse>> EcfClient::postEcf(
    TipoeCFType::eTipoeCFType tipoeCF,
    std::shared_ptr<ECF> ecf
) {
    switch (tipoeCF) {
        case TipoeCFType::eTipoeCFType::FACTURADECREDITOFISCALELECTRONICA:
            return m_ecfApi->recepcionEcf31(ecf);
        case TipoeCFType::eTipoeCFType::FACTURADECONSUMOELECTRONICA:
            return m_ecfApi->recepcionEcf32(ecf);
        case TipoeCFType::eTipoeCFType::NOTADEDEBITOELECTRONICA:
            return m_ecfApi->recepcionEcf33(ecf);
        case TipoeCFType::eTipoeCFType::NOTADECREDITOELECTRONICA:
            return m_ecfApi->recepcionEcf34(ecf);
        case TipoeCFType::eTipoeCFType::COMPRASELECTRONICO:
            return m_ecfApi->recepcionEcf41(ecf);
        case TipoeCFType::eTipoeCFType::GASTOSMENORESELECTRONICO:
            return m_ecfApi->recepcionEcf43(ecf);
        case TipoeCFType::eTipoeCFType::REGIMENESESPECIALESELECTRONICO:
            return m_ecfApi->recepcionEcf44(ecf);
        case TipoeCFType::eTipoeCFType::GUBERNAMENTALELECTRONICO:
            return m_ecfApi->recepcionEcf45(ecf);
        case TipoeCFType::eTipoeCFType::COMPROBANTEDEEXPORTACIONESELECTRONICO:
            return m_ecfApi->recepcionEcf46(ecf);
        case TipoeCFType::eTipoeCFType::COMPROBANTEPARAPAGOSALEXTERIORELECTRONICO:
            return m_ecfApi->recepcionEcf47(ecf);
        default:
            throw std::invalid_argument("Unknown tipoeCF value");
    }
}

pplx::task<std::shared_ptr<EcfResponse>> EcfClient::pollUntilComplete(
    std::function<pplx::task<std::shared_ptr<EcfResponse>>()> fn,
    std::function<bool(const std::shared_ptr<EcfResponse>&)> isComplete,
    const PollingOptions& options
) {
    struct PollState {
        std::function<pplx::task<std::shared_ptr<EcfResponse>>()> fn;
        std::function<bool(const std::shared_ptr<EcfResponse>&)> isComplete;
        PollingOptions options;
        std::chrono::milliseconds currentDelay;
        int retries;
        std::chrono::steady_clock::time_point startTime;

        PollState(
            std::function<pplx::task<std::shared_ptr<EcfResponse>>()> f,
            std::function<bool(const std::shared_ptr<EcfResponse>&)> ic,
            const PollingOptions& opts
        ) : fn(std::move(f)), isComplete(std::move(ic)), options(opts),
            currentDelay(opts.initialDelay), retries(0),
            startTime(std::chrono::steady_clock::now()) {}
    };

    auto state = std::make_shared<PollState>(std::move(fn), std::move(isComplete), options);

    // Recursive polling using task continuations
    std::function<pplx::task<std::shared_ptr<EcfResponse>>(std::shared_ptr<PollState>)> pollOnce;
    pollOnce = [pollOnce](std::shared_ptr<PollState> s) -> pplx::task<std::shared_ptr<EcfResponse>> {
        return s->fn().then([pollOnce, s](std::shared_ptr<EcfResponse> result) -> pplx::task<std::shared_ptr<EcfResponse>> {
            if (s->isComplete(result)) {
                return pplx::task_from_result(result);
            }

            s->retries++;

            if (s->retries >= s->options.maxRetries) {
                throw PollingMaxRetriesError(s->options.maxRetries);
            }

            if (s->options.timeout.count() > 0) {
                auto elapsed = std::chrono::steady_clock::now() - s->startTime;
                if (elapsed >= s->options.timeout) {
                    throw PollingTimeoutError();
                }
            }

            // Sleep with exponential backoff
            auto delay = s->currentDelay;
            s->currentDelay = std::chrono::milliseconds(
                std::min(
                    static_cast<long long>(s->currentDelay.count() * s->options.backoffMultiplier),
                    s->options.maxDelay.count()
                )
            );

            // Use a timer task for the delay
            return pplx::create_task([delay]() {
                std::this_thread::sleep_for(delay);
            }).then([pollOnce, s]() -> pplx::task<std::shared_ptr<EcfResponse>> {
                return pollOnce(s);
            });
        });
    };

    return pollOnce(state);
}

// ---------------------------------------------------------------------------
// EcfFrontendClient
// ---------------------------------------------------------------------------

utility::string_t EcfFrontendClient::resolveBaseUrl(const EcfFrontendClientConfig& config) {
    if (!config.baseUrl.empty()) {
        return utility::conversions::to_string_t(config.baseUrl);
    }

    const char* envUrl = std::getenv("ECF_API_URL");
    if (envUrl && envUrl[0] != '\0') {
        return utility::conversions::to_string_t(std::string(envUrl));
    }

    static const std::map<std::string, std::string> ENVIRONMENT_URLS = {
        { "test", "https://api.test.ecfx.ssd.com.do" },
        { "cert", "https://api.cert.ecfx.ssd.com.do" },
        { "prod", "https://api.prod.ecfx.ssd.com.do" },
    };

    auto it = ENVIRONMENT_URLS.find(config.environment);
    if (it != ENVIRONMENT_URLS.end()) {
        return utility::conversions::to_string_t(it->second);
    }

    return utility::conversions::to_string_t(std::string("https://api.test.ecfx.ssd.com.do"));
}

void EcfFrontendClient::defaultCacheToken(const std::string& token) {
    // Default implementation: encrypt and write token to a file on disk.
    // TODO: Implement platform-specific encrypted file storage.
    (void)token;
}

std::string EcfFrontendClient::defaultGetCachedToken() {
    // Default implementation: read encrypted token from disk.
    // Returns empty string if no cached token is found.
    // TODO: Implement platform-specific encrypted file storage.
    return "";
}

std::string EcfFrontendClient::resolveToken() {
    // Try cached token first
    auto getCached = m_config.getCachedToken;
    if (getCached) {
        std::string cached = getCached();
        if (!cached.empty()) {
            return cached;
        }
    }

    // Fetch a fresh token via the required callback
    if (!m_config.getToken) {
        throw std::invalid_argument(
            "EcfFrontendClientConfig.getToken is required. "
            "Provide a callback that returns a read-only API token from your backend.");
    }

    std::string token = m_config.getToken();
    if (token.empty()) {
        throw std::runtime_error("getToken callback returned an empty token");
    }

    // Cache the token
    auto cache = m_config.cacheToken;
    if (cache) {
        cache(token);
    }

    return token;
}

EcfFrontendClient::EcfFrontendClient(const EcfFrontendClientConfig& config)
    : m_config(config)
{
    // Apply default cache callbacks if not provided
    if (!m_config.cacheToken) {
        m_config.cacheToken = &EcfFrontendClient::defaultCacheToken;
    }
    if (!m_config.getCachedToken) {
        m_config.getCachedToken = &EcfFrontendClient::defaultGetCachedToken;
    }

    auto apiConfig = std::make_shared<ApiConfiguration>();
    apiConfig->setBaseUrl(resolveBaseUrl(m_config));

    std::string apiKey = resolveToken();
    apiConfig->getDefaultHeaders()[_XPLATSTR("Authorization")] =
        utility::conversions::to_string_t("Bearer " + apiKey);

    m_apiClient = std::make_shared<ApiClient>(apiConfig);
    m_ecfApi = std::make_shared<EcfApi>(m_apiClient);
    m_companyApi = std::make_shared<CompanyApi>(m_apiClient);
}

} // namespace ecf_dgii
