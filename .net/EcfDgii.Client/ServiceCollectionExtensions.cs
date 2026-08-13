using System;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;

namespace EcfDgii.Client
{
    /// <summary>
    /// Extension methods for setting up ECF DGII SDK services in an <see cref="IServiceCollection"/>.
    /// </summary>
    public static class ServiceCollectionExtensions
    {
        /// <summary>
        /// Adds the <see cref="EcfClient"/> to the service collection.
        /// </summary>
        /// <param name="services">The service collection.</param>
        /// <param name="setupAction">Optional action to configure the client options.</param>
        /// <returns>The service collection.</returns>
        public static IServiceCollection AddEcfClient(this IServiceCollection services, Action<EcfClientOptions>? setupAction = null)
        {
            var options = new EcfClientOptions();
            setupAction?.Invoke(options);

            services.TryAddSingleton(options);
            services.TryAddScoped<EcfClient>();

            return services;
        }

        /// <summary>
        /// Adds the <see cref="EcfFrontendClient"/> to the service collection.
        /// </summary>
        /// <param name="services">The service collection.</param>
        /// <param name="setupAction">Action to configure the frontend client options.</param>
        /// <returns>The service collection.</returns>
        public static IServiceCollection AddEcfFrontendClient(this IServiceCollection services, Action<EcfFrontendClientOptions> setupAction)
        {
            if (setupAction == null) throw new ArgumentNullException(nameof(setupAction));

            services.TryAddScoped(sp =>
            {
                var options = new EcfFrontendClientOptions();
                setupAction(options);
                return new EcfFrontendClient(options);
            });

            return services;
        }
    }
}
