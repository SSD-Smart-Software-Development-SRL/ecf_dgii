using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class AnulacionTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IAnulacionAPI anulacionAPI;

    public AnulacionTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        anulacionAPI = RestService.For<IAnulacionAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    public async Task WhenAprobacionComercialTest()
    {
        // Arrange
        await using var anulacionXml = File.OpenRead("./Data/Anulacion.xml");
        var streamPart = new StreamPart(anulacionXml, "101672919E3200000001.xml", "text/xml");
        
        // Act
        var response = await anulacionAPI.Operaciones(streamPart, fixture.APIKey);
        
        // Asserts
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.Rnc.Should().NotBeEmpty();
        response.Content.Codigo.Should().NotBeEmpty();
        response.Content.Mensajes.Should().BeNullOrEmpty();
    }
}