require "spec_helper"

RSpec.describe EcfDgii::EcfError do
  it "can be created with just a message" do
    error = described_class.new("Something went wrong")
    expect(error.message).to eq("Something went wrong")
    expect(error.response).to be_nil
  end

  it "can be created with a message and response" do
    response = double("EcfResponse", progress: "Error", errors: "Failed")
    error = described_class.new("Processing failed", response)
    expect(error.message).to eq("Processing failed")
    expect(error.response).to eq(response)
  end

  it "inherits from StandardError" do
    expect(described_class.superclass).to eq(StandardError)
  end
end

RSpec.describe EcfDgii::PollingTimeoutError do
  it "has a default message" do
    error = described_class.new
    expect(error.message).to eq("Polling timed out")
  end

  it "inherits from EcfError" do
    expect(described_class.superclass).to eq(EcfDgii::EcfError)
  end
end

RSpec.describe EcfDgii::PollingMaxRetriesError do
  it "includes retry count in message" do
    error = described_class.new(60)
    expect(error.message).to include("60")
  end

  it "inherits from EcfError" do
    expect(described_class.superclass).to eq(EcfDgii::EcfError)
  end
end

