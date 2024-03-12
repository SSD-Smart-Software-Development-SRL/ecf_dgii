using System.Text;
using ECF_DGII.SDK.Tests.Extensions;
using FluentAssertions;
using Microsoft.Extensions.Configuration;
using Refit;

namespace ECF_DGII.SDK.Tests;

public class AutenticacionTests
{
    private readonly IAutenticacionAPI api;

    public AutenticacionTests()
    {
        api = RestService.For<IAutenticacionAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenGetSemillaTest()
    {
        // Act
        using var response = await api.Semilla();

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Content.Should().NotBeNull();
        using var reader = new StreamReader(response.Content, Encoding.UTF8);
        var text = await reader.ReadToEndAsync();
        text.Should().NotBeNullOrEmpty();
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenVerificaSemillaTest()
    {
        // Arrange
        using var certificate = new ConfigurationBuilder()
            .SetBasePath(AppContext.BaseDirectory)
            .AddEnvironmentVariables()
            .AddUserSecrets<AutenticacionTests>()
            .Build()
            .ReadCertificateFromBase64();
        using var semillaResponse = await api.Semilla();
        await using var semillaStream = semillaResponse.Content
            .ToXmlDocument()
            .Sign(certificate)
            .ToStream();
        var streamPart = new StreamPart(semillaStream, "00100000000-semilla.xml", "text/xml");

        // Act
        var tokenResponse = await api.ValidarSemilla(streamPart);

        // Assert
        var now = DateTime.Now.ToUniversalTime();
        tokenResponse.IsSuccessStatusCode.Should().BeTrue();
        tokenResponse.Content.Should().NotBeNull();
        tokenResponse.Content.Expira.ToUniversalTime().Should().BeCloseTo(now.AddHours(1), TimeSpan.FromMinutes(10));
        tokenResponse.Content.Expedido.ToUniversalTime().Should().BeBefore(now);
        tokenResponse.Content.Token.Should().NotBeEmpty();
    }
}