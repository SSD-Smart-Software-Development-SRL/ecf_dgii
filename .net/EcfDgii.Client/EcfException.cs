using System;
using EcfDgii.Client.Generated.Models;

namespace EcfDgii.Client
{
    /// <summary>
    /// Thrown when an ECF processing completes with an error status.
    /// </summary>
    public class EcfException : Exception
    {
        /// <summary>The full ECF response that contains the error details.</summary>
        public EcfResponse Response { get; }

        public EcfException(string message, EcfResponse response)
            : base(message)
        {
            Response = response;
        }
    }

    /// <summary>
    /// Thrown when polling exceeds the maximum number of retries.
    /// </summary>
    public class PollingMaxRetriesException : Exception
    {
        public int Retries { get; }

        public PollingMaxRetriesException(int retries)
            : base($"Polling exceeded maximum retries ({retries})")
        {
            Retries = retries;
        }
    }

    /// <summary>
    /// Thrown when polling exceeds the configured timeout.
    /// </summary>
    public class PollingTimeoutException : TimeoutException
    {
        public PollingTimeoutException(string message = "Polling timed out")
            : base(message) { }
    }
}
