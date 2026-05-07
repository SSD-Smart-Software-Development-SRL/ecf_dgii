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

// NOTE: The previous high-level sendEcf/postEcf/pollUntilComplete helpers
// have been removed because the OpenAPI spec no longer carries a unified
// ECF schema. Per-eCF-type schemas (Ecf31ECF ... Ecf47ECF) now exist with
// distinct typed Encabezado/IdDoc/Emisor. Callers should invoke the
// matching typed endpoint on EcfApi directly. A typed send-and-poll wrapper
// is on the roadmap.

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
