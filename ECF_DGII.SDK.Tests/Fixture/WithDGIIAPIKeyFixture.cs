using ECF_DGII.Models.Autenticacion;
using ECF_DGII.SDK.Tests.Extensions;
using Microsoft.Extensions.Configuration;
using Refit;

namespace ECF_DGII.SDK.Tests.Fixture;

public sealed class WithDGIIAPIKeyFixture : IAsyncLifetime
{
    private readonly IAutenticacionAPI autenticacionAPI;
    private RespuestaSemilla? respuestaSemilla;

    internal string APIKey
    {
        get
        {
            if (respuestaSemilla is null || string.IsNullOrWhiteSpace(respuestaSemilla.Token))
                throw new Exception("The API key is null empty or white space");
            if (respuestaSemilla.Expira.ToUniversalTime() >= DateTime.UtcNow)
                throw new Exception("The API key has expired");
            return respuestaSemilla.Token;
        }
    }

    public WithDGIIAPIKeyFixture()
    {
        autenticacionAPI = RestService.For<IAutenticacionAPI>("https://ecf.dgii.gov.do/testecf");
    }

    public async Task InitializeAsync()
    {
        using var certificate = new ConfigurationBuilder()
            .SetBasePath(AppContext.BaseDirectory)
            .AddUserSecrets<AutenticacionTests>()
            .Build()
            .ReadCertificateFromBase64();
        using var semillaResponse = await autenticacionAPI.Semilla();
        await using var semillaStream = semillaResponse.Content
            .ToXmlDocument()
            .Sign(certificate)
            .ToStream();
        var streamPart = new StreamPart(semillaStream, "00100000000-semilla.xml", "text/xml");
        var tokenResponse = await autenticacionAPI.ValidarSemilla(streamPart);
        if (!tokenResponse.IsSuccessStatusCode)
            throw new InvalidOperationException($"Error `{tokenResponse.StatusCode}` getting SemillaRespuesta.", tokenResponse.Error);
        respuestaSemilla = tokenResponse.Content;
    }

    public Task DisposeAsync() => Task.CompletedTask;
}
