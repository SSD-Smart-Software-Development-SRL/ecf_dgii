require_relative "exceptions"

module EcfDgii
  # Configuration options for polling with exponential backoff.
  #
  # Matches the TypeScript SDK's PollingOptions interface 1:1.
  class PollingOptions
    # @return [Float] Initial delay between polls in seconds. Default: 1.0
    attr_accessor :initial_delay

    # @return [Float] Maximum delay between polls in seconds. Default: 30.0
    attr_accessor :max_delay

    # @return [Integer] Maximum number of retries. Default: 60
    attr_accessor :max_retries

    # @return [Float] Backoff multiplier. Default: 2.0
    attr_accessor :backoff_multiplier

    # @return [Float, nil] Total timeout in seconds. Optional (nil = no timeout).
    attr_accessor :timeout

    # @return [Proc, nil] Optional cancellation callable.
    #   Called before each poll iteration. If it returns a truthy value,
    #   polling is aborted with PollingTimeoutError.
    attr_accessor :cancellation

    def initialize(initial_delay: 1.0, max_delay: 30.0, max_retries: 60,
                   backoff_multiplier: 2.0, timeout: nil, cancellation: nil)
      @initial_delay = initial_delay
      @max_delay = max_delay
      @max_retries = max_retries
      @backoff_multiplier = backoff_multiplier
      @timeout = timeout
      @cancellation = cancellation
    end
  end

  # Polling logic with exponential backoff.
  #
  # Usage:
  #   EcfDgii::Polling.poll_until_complete do
  #     client.query_ecf(rnc, encf)
  #   end
  module Polling
    # Terminal progress values matching the ECF API contract.
    #   - "Finished" → ECF processing completed successfully
    #   - "Error"    → ECF processing failed (throws EcfError in client)
    TERMINAL_PROGRESS = %w[Finished Error].freeze

    # Poll a block until its result indicates completion, using exponential backoff.
    #
    # @yieldreturn [Object] An object that responds to #progress
    # @param options [PollingOptions, nil] Polling configuration
    # @return [Object] The final result when progress is terminal
    # @raise [PollingTimeoutError] If total timeout is exceeded
    # @raise [PollingMaxRetriesError] If max retries is exceeded
    def self.poll_until_complete(options = nil)
      opts = options || PollingOptions.new
      delay = opts.initial_delay
      retries = 0
      start_time = Process.clock_gettime(Process::CLOCK_MONOTONIC)

      loop do
        # Check cancellation before each iteration
        if opts.cancellation && opts.cancellation.call
          raise PollingTimeoutError, "Polling was cancelled"
        end

        result = yield

        progress = extract_progress(result)

        return result if TERMINAL_PROGRESS.include?(progress)

        retries += 1

        if opts.max_retries > 0 && retries >= opts.max_retries
          raise PollingMaxRetriesError.new(opts.max_retries)
        end

        if opts.timeout && opts.timeout > 0
          elapsed = Process.clock_gettime(Process::CLOCK_MONOTONIC) - start_time
          if elapsed >= opts.timeout
            raise PollingTimeoutError,
                  "Polling timed out after #{opts.timeout}s (last progress: #{progress})"
          end
        end

        sleep(delay)
        delay = [delay * opts.backoff_multiplier, opts.max_delay].min
      end
    end

    # Extract the progress value from a result, regardless of its type.
    #
    # @param result [Object] An API model object, Hash, or anything responding to #progress
    # @return [String] The progress value as a string
    def self.extract_progress(result)
      progress = nil
      if result.respond_to?(:progress)
        progress = result.progress
      elsif result.is_a?(Hash)
        progress = result[:progress] || result["progress"]
      end

      progress = progress.value if progress.respond_to?(:value)
      progress.to_s
    end

    private_class_method :extract_progress
  end
end
