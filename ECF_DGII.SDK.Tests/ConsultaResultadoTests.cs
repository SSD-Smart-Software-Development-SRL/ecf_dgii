using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class ConsultaResultadoTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IConsultaResultadoAPI consultaResultadoAPI;

    public ConsultaResultadoTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        consultaResultadoAPI = RestService.For<IConsultaResultadoAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    public async Task WhenConsultaResultadoTest()
    {
        // Act
        var response = await consultaResultadoAPI.Estado("1234", fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.TrackId.Should().NotBeEmpty();
        response.Content.Codigo.Should().NotBeEmpty();
        response.Content.Estado.Should().NotBeEmpty();
        response.Content.Rnc.Should().NotBeEmpty();
        response.Content.Encf.Should().BeEmpty();
        response.Content.SecuenciaUtilizada.Should().BeTrue();
        response.Content.FechaRecepcion.Should().NotBeEmpty();
        response.Content.Mensajes.Should().BeEmpty();
    }
}