require "json"
require_relative "exceptions"

module EcfDgii
  # A restricted, read-only client that only exposes GET endpoints.
  # Suitable for use in frontend / browser code where write operations
  # should not be available.
  #
  # Token lifecycle is handled automatically:
  # 1. On each request, checks {get_cached_token}. If nil, calls {get_token}
  #    then {cache_token}.
  # 2. On 401 responses, calls {get_token} again, updates the cache, and
  #    retries the request.
  #
  # Mirrors the TypeScript {EcfFrontendClient} 1:1.
  #
  # @example Basic usage
  #   client = EcfDgii::FrontendClient.new(
  #     get_token: -> { my_backend.fetch_token },
  #     environment: :test
  #   )
  #   ecfs = client.query_ecf("131460941", "E310000051630")
  class FrontendClient
    ENVIRONMENT_URLS = {
      test: "https://api.test.ecfx.ssd.com.do",
      cert: "https://api.cert.ecfx.ssd.com.do",
      prod: "https://api.prod.ecfx.ssd.com.do"
    }.freeze

    # @return [EcfDgii::Generated::ApiClient] The underlying generated API client.
    attr_reader :api_client

    # @return [Symbol] The configured environment.
    attr_reader :environment

    # Create a new frontend client.
    #
    # @param get_token [Proc] Function that fetches a fresh token
    #   (e.g. calls your backend's GET /ecf-token). **Required**.
    # @param cache_token [Proc, nil] Function to cache the token.
    #   Defaults to file-based cache at +~/.ecf-dgii/token+.
    # @param get_cached_token [Proc, nil] Function to retrieve a cached token.
    #   Defaults to file-based cache.
    # @param base_url [String, nil] Base URL override. Takes precedence over +environment+.
    # @param environment [Symbol] Target environment (+:test+, +:cert+, +:prod+).
    #   Defaults to +:test+.
    # @param timeout [Integer] HTTP timeout in seconds. Defaults to 30.
    def initialize(get_token:, cache_token: nil, get_cached_token: nil,
                   base_url: nil, environment: :test, timeout: 30)
      raise ArgumentError, "get_token is required for EcfDgii::FrontendClient" unless get_token

      resolved_url = base_url || ENVIRONMENT_URLS[environment.to_sym]
      raise ArgumentError, "Invalid environment or base URL" if resolved_url.nil? || resolved_url.empty?

      @get_token = get_token
      @cache_token = cache_token || method(:default_cache_token)
      @get_cached_token = get_cached_token || method(:default_get_cached_token)

      config = EcfDgii::Generated::Configuration.new
      uri = URI.parse(resolved_url)

      config.scheme = uri.scheme
      config.host = uri.host
      config.base_path = uri.path.empty? ? "" : uri.path
      config.timeout = timeout

      @api_client = EcfDgii::Generated::ApiClient.new(config)
      @environment = environment.to_sym
    end

    # ---------------------------------------------------------------------------
    # Base API clients (lazy-loaded)
    # ---------------------------------------------------------------------------

    def ecf_api
      @ecf_api ||= EcfDgii::Generated::EcfApi.new(token_api_client)
    end

    def company_api
      @company_api ||= EcfDgii::Generated::CompanyApi.new(token_api_client)
    end

    # ---------------------------------------------------------------------------
    # ECF query operations (read-only GETs)
    # ---------------------------------------------------------------------------

    # Query ECFs by RNC and eNCF.
    def query_ecf(rnc, encf, opts = {})
      ecf_api.query_ecf(rnc, encf, opts)
    end

    # Search ECFs for a specific RNC.
    def search_ecfs(rnc, opts = {})
      ecf_api.search_ecfs(rnc, opts)
    end

    # Search all ECFs across all companies.
    def search_all_ecfs(opts = {})
      ecf_api.search_all_ecfs(opts)
    end

    # Get a specific ECF by message ID.
    def get_ecf_by_id(rnc, id)
      ecf_api.get_ecf_by_id(rnc, id)
    end

    # ---------------------------------------------------------------------------
    # Company operations (read-only GETs)
    # ---------------------------------------------------------------------------

    # List companies with optional filters.
    def get_companies(opts = {})
      company_api.get_companies(opts)
    end

    # Get a company by RNC.
    def get_company_by_rnc(rnc)
      company_api.get_company_by_rnc(rnc)
    end

    private

    # Creates an ApiClient that injects a Bearer token with cache + auto-refresh.
    def token_api_client
      return @token_api_client if @token_api_client

      config = @api_client.config.dup
      # We'll override the access_token via a custom middleware-like approach.
      # Faraday supports request/response middleware via the builder.
      # Instead of a fixed access_token, we inject it per-request with retry on 401.

      client = EcfDgii::Generated::ApiClient.new(config)

      # Store original call method
      original_call = client.method(:call_api)

      # Define the client's token lifecycle as a singleton method
      client.define_singleton_method(:call_api) do |http_method, path, opts = {}|
        # 1. Get token (from cache or fresh)
        token = get_cached_token_proc.call
        if token.nil? || token.empty?
          token = get_token_proc.call
          cache_token_proc.call(token)
        end

        # Set the token
        opts[:header_params] ||= {}
        opts[:header_params]["Authorization"] = "Bearer #{token}"

        # Make the request
        response = original_call.call(http_method, path, opts)

        # 2. On 401, refresh and retry
        if response.respond_to?(:code) && response.code == 401
          token = get_token_proc.call
          cache_token_proc.call(token)
          opts[:header_params]["Authorization"] = "Bearer #{token}"
          response = original_call.call(http_method, path, opts)
        end

        response
      end

      # Store procs for the singleton method closure
      client.instance_variable_set(:@get_token_proc, @get_token)
      client.instance_variable_set(:@cache_token_proc, @cache_token)
      client.instance_variable_set(:@get_cached_token_proc, @get_cached_token)

      # Define accessors for the closure
      client.define_singleton_method(:get_token_proc) { @get_token_proc }
      client.define_singleton_method(:cache_token_proc) { @cache_token_proc }
      client.define_singleton_method(:get_cached_token_proc) { @get_cached_token_proc }

      @token_api_client = client
    end

    # Default file-based token cache: ~/.ecf-dgii/token
    def default_cache_dir
      @default_cache_dir ||= begin
        dir = File.expand_path("~/.ecf-dgii")
        Dir.mkdir(dir) unless Dir.exist?(dir)
        dir
      end
    end

    def default_cache_token(token)
      File.write(File.join(default_cache_dir, "token"), token)
    end

    def default_get_cached_token
      path = File.join(default_cache_dir, "token")
      File.exist?(path) ? File.read(path).strip : nil
    end
  end

  # Factory that creates a restricted read-only client suitable for frontend use.
  # Only GET endpoints are exposed.
  #
  # @param get_token [Proc] Function that fetches a fresh token.
  # @param cache_token [Proc, nil] Function to cache the token.
  # @param get_cached_token [Proc, nil] Function to retrieve a cached token.
  # @param base_url [String, nil] Base URL override.
  # @param environment [Symbol] Target environment.
  #
  # @return [EcfDgii::FrontendClient]
  def self.create_frontend_client(get_token:, cache_token: nil, get_cached_token: nil,
                                   base_url: nil, environment: :test, timeout: 30)
    FrontendClient.new(
      get_token: get_token,
      cache_token: cache_token,
      get_cached_token: get_cached_token,
      base_url: base_url,
      environment: environment,
      timeout: timeout
    )
  end
end
