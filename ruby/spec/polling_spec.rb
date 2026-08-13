require "spec_helper"

RSpec.describe EcfDgii::Polling do
  describe ".poll_until_complete" do
    it "polls until status is Finished" do
      states = [
        double(progress: "InProcess"),
        double(progress: "InProcess"),
        double(progress: "Finished")
      ]

      call_count = 0
      result = described_class.poll_until_complete(
        EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.01)
      ) do
        call_count += 1
        states[call_count - 1]
      end

      expect(call_count).to eq(3)
      expect(result.progress).to eq("Finished")
    end

    it "polls until status is Error" do
      states = [
        double(progress: "InProcess"),
        double(progress: "Error")
      ]

      call_count = 0
      result = described_class.poll_until_complete(
        EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.01)
      ) do
        call_count += 1
        states[call_count - 1]
      end

      expect(call_count).to eq(2)
      expect(result.progress).to eq("Error")
    end

    it "raises PollingTimeoutError if it exceeds timeout" do
      options = EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.002, timeout: 0.005)

      expect {
        described_class.poll_until_complete(options) do
          double(progress: "InProcess")
        end
      }.to raise_error(EcfDgii::PollingTimeoutError)
    end

    it "raises PollingMaxRetriesError if it exceeds max retries" do
      options = EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.002, max_retries: 3)

      expect {
        described_class.poll_until_complete(options) do
          double(progress: "InProcess")
        end
      }.to raise_error(EcfDgii::PollingMaxRetriesError)
    end

    it "uses defaults when no options provided" do
      call_count = 0
      result = described_class.poll_until_complete do
        call_count += 1
        double(progress: call_count > 1 ? "Finished" : "InProcess")
      end

      expect(call_count).to eq(2)
      expect(result.progress).to eq("Finished")
    end

    it "supports cancellation via callable" do
      call_count = 0
      options = EcfDgii::PollingOptions.new(
        initial_delay: 0.001,
        max_delay: 0.01,
        cancellation: -> { call_count >= 2 }
      )

      expect {
        described_class.poll_until_complete(options) do
          call_count += 1
          double(progress: "InProcess")
        end
      }.to raise_error(EcfDgii::PollingTimeoutError, /cancelled/)
    end

    it "handles Hash results with progress" do
      result = described_class.poll_until_complete(
        EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.01)
      ) do
        { "progress" => "Finished" }
      end

      expect(result).to eq({ "progress" => "Finished" })
    end

    it "handles Hash results with symbol keys" do
      result = described_class.poll_until_complete(
        EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.01)
      ) do
        { progress: "Finished" }
      end

      expect(result).to eq({ progress: "Finished" })
    end
  end

  describe ".extract_progress" do
    it "extracts progress from object responding to progress" do
      obj = double(progress: "Finished")
      expect(described_class.send(:extract_progress, obj)).to eq("Finished")
    end

    it "extracts progress from object with progress.value" do
      progress_value = double(value: "Finished")
      obj = double(progress: progress_value)
      expect(described_class.send(:extract_progress, obj)).to eq("Finished")
    end

    it "extracts progress from Hash with string keys" do
      expect(described_class.send(:extract_progress, { "progress" => "Error" })).to eq("Error")
    end

    it "extracts progress from Hash with symbol keys" do
      expect(described_class.send(:extract_progress, { progress: "Finished" })).to eq("Finished")
    end
  end
end
