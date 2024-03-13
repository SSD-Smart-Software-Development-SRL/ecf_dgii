using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class ConsultaTrackIdTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IConsultaTrackIdAPI consultaTrackIdAPI;

    public ConsultaTrackIdTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        consultaTrackIdAPI = RestService.For<IConsultaTrackIdAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenConsultaTrackIdTest()
    {
        // Act
        var response = await consultaTrackIdAPI.Consulta("", "", fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.TrackId.Should().NotBeEmpty();
        response.Content.Estado.Should().NotBeEmpty();
        response.Content.FechaRecepcion.Should().NotBeEmpty();
    }
}