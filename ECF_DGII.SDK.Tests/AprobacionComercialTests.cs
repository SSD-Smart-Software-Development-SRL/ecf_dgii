using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class AprobacionComercialTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IAprobacionComercialAPI aprobacionComercialAPI;

    public AprobacionComercialTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        aprobacionComercialAPI = RestService.For<IAprobacionComercialAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenAprobacionComercialTest()
    {
        // Arrange
        await using var approbacionComercialXml = File.OpenRead("./Data/AprobacionComercial.xml");
        var streamPart = new StreamPart(approbacionComercialXml, "101672919E3200000001.xml", "text/xml");
        
        // Act
        var response = await aprobacionComercialAPI.AprobacionComercial(streamPart, fixture.APIKey);
        
        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.Codigo.Should().NotBeEmpty();
        response.Content.Estado.Should().NotBeEmpty();
        response.Content.Mensaje.Should().BeNullOrEmpty();
    }
}