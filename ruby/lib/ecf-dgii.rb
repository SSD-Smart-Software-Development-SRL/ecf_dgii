require "uri"
require_relative "ecf_dgii/version"
require_relative "ecf_dgii/generated"
require_relative "ecf_dgii/exceptions"
require_relative "ecf_dgii/client"
require_relative "ecf_dgii/polling"
require_relative "ecf_dgii/frontend_client"

module EcfDgii
  class << self
    attr_accessor :configuration
  end

  def self.configure
    self.configuration ||= Configuration.new
    yield(configuration)
    @client = nil
  end

  def self.client
    @client ||= Client.new(
      api_key: configuration&.api_key,
      base_url: configuration&.base_url,
      environment: configuration&.environment || :test,
      timeout: configuration&.timeout || 30
    )
  end

  class Configuration
    attr_accessor :api_key, :base_url, :environment, :timeout

    def initialize
      @api_key = ENV["ECF_API_KEY"]
      @base_url = ENV["ECF_API_URL"]
      @environment = :test
      @timeout = 30
    end
  end
end

require_relative "ecf_dgii/railtie" if defined?(Rails)
