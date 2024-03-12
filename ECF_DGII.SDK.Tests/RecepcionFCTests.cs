using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class RecepcionFCTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IRecepcionFCAPI recepcionFCAPI;

    public RecepcionFCTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        recepcionFCAPI = RestService.For<IRecepcionFCAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    public async Task WhenRecepcionTest()
    {
        // Arrange
        await using var recepcionFCXml = File.OpenRead("./Data/RecepcionFC.xml");
        var streamPart = new StreamPart(recepcionFCXml, "101672919E3200000001.xml", "text/xml");

        // Act
        var response = await recepcionFCAPI.Recepcion(streamPart, fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.Codigo.Should().Be(Models.RecepcionFC.EstadoCF.One);
        response.Content.Estado.Should().NotBeEmpty();
        response.Content.Enfc.Should().NotBeEmpty();
        response.Content.SecuenciaUtilizada.Should().BeFalse();
        response.Content.Mensajes.Should().BeEmpty();
    }
}