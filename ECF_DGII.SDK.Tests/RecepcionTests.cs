using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class RecepcionTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IRecepcionAPI recepcionAPI;

    public RecepcionTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        recepcionAPI = RestService.For<IRecepcionAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenFacturaElectronicaTest()
    {
        // Arrange
        await using var recepcionXml = File.OpenRead("./Data/RecepcionFC.xml");
        var streamPart = new StreamPart(recepcionXml, "101672919E3200000001.xml", "text/xml");

        // Act
        var response = await recepcionAPI.FacturasElectronicas(streamPart, fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.TrackId.Should().NotBeEmpty();
        response.Content.Error.Should().BeEmpty();
        response.Content.Mensaje.Should().BeEmpty();
    }
}