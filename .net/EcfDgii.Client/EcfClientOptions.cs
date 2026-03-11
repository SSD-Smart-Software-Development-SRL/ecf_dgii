using System;

namespace EcfDgii.Client
{
    /// <summary>
    /// Target API environment.
    /// </summary>
    public enum EcfEnvironment
    {
        Test,
        Cert,
        Prod
    }

    /// <summary>
    /// Configuration options for <see cref="EcfClient"/>.
    /// </summary>
    public class EcfClientOptions
    {
        /// <summary>
        /// API key (JWT Bearer token) used for authentication.
        /// If not set, falls back to the <c>ECF_API_KEY</c> environment variable.
        /// </summary>
        public string? ApiKey { get; set; }

        /// <summary>
        /// Base URL override. Takes precedence over <see cref="Environment"/>.
        /// If not set, falls back to the <c>ECF_API_URL</c> environment variable.
        /// </summary>
        public string? BaseUrl { get; set; }

        /// <summary>
        /// Target environment. Defaults to <see cref="EcfEnvironment.Test"/>.
        /// </summary>
        public EcfEnvironment Environment { get; set; } = EcfEnvironment.Test;
    }

    /// <summary>
    /// Options for the send-and-poll workflow.
    /// </summary>
    public class PollingOptions
    {
        /// <summary>Initial delay between polls in milliseconds. Default: 1000.</summary>
        public int InitialDelayMs { get; set; } = 1000;

        /// <summary>Maximum delay between polls in milliseconds. Default: 30000.</summary>
        public int MaxDelayMs { get; set; } = 30000;

        /// <summary>Maximum number of poll attempts. Default: 60.</summary>
        public int MaxRetries { get; set; } = 60;

        /// <summary>Backoff multiplier applied after each poll. Default: 2.</summary>
        public double BackoffMultiplier { get; set; } = 2;

        /// <summary>Total timeout in milliseconds. When exceeded, polling stops. Optional (null = no timeout).</summary>
        public int? TimeoutMs { get; set; }
    }
}
