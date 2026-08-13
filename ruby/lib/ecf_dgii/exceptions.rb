module EcfDgii
  # Base error class for ECF SDK errors.
  class EcfError < StandardError
    # The full EcfResponse object containing details about the error.
    attr_reader :response

    def initialize(message, response = nil)
      super(message)
      @response = response
    end
  end

  # Raised when polling exceeds the total timeout.
  class PollingTimeoutError < EcfError
    def initialize(message = "Polling timed out")
      super(message)
    end
  end

  # Raised when polling exceeds the maximum number of retries.
  class PollingMaxRetriesError < EcfError
    def initialize(retries)
      super("Polling exceeded maximum retries (#{retries})")
    end
  end
end
