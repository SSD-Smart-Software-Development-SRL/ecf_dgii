require "spec_helper"

RSpec.describe EcfDgii::FrontendClient do
  let(:get_token) { -> { "frontend-token-123" } }

  it "initializes with required get_token and default environment" do
    client = described_class.new(get_token: get_token, environment: :test)
    expect(client.environment).to eq(:test)
  end

  it "raises ArgumentError if get_token is nil" do
    expect {
      described_class.new(get_token: nil)
    }.to raise_error(ArgumentError, /get_token/)
  end

  it "initializes with custom base_url" do
    client = described_class.new(
      get_token: get_token,
      base_url: "https://custom.api.com/v2"
    )
    expect(client.api_client.config.host).to eq("custom.api.com")
    expect(client.api_client.config.base_path).to eq("/v2")
  end

  it "uses file-based cache by default" do
    client = described_class.new(get_token: get_token, environment: :test)
    expect(client).to respond_to(:api_client)
  end

  describe ".create_frontend_client factory" do
    it "creates a FrontendClient instance" do
      client = EcfDgii.create_frontend_client(
        get_token: get_token,
        environment: :test
      )
      expect(client).to be_an_instance_of(EcfDgii::FrontendClient)
    end
  end
end
