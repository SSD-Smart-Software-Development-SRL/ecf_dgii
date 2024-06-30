using ECF_DGII.Models.EstatusServicios;
using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class EstatusServiciosTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IEstatusServiciosAPI estatusServiciosAPI;

    public EstatusServiciosTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        estatusServiciosAPI = RestService.For<IEstatusServiciosAPI>("https://statusecf.dgii.gov.do");
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenObtenerEstatusTest()
    {
        // Act
        var response = await estatusServiciosAPI.ObtenerEstatus(fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNullOrEmpty();
        response.Content.Should().BeEquivalentTo([new RespuestaEstatusServicio()
        {
            Servicio = "",
            Status = "",
            Ambiente = ""
        }]);
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenObtenerVentanasDeMantenimientoEstatusTest()
    {
        // Act
        var response = await estatusServiciosAPI.ObtenerVentanasMantenimiento(fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.VentanaMantenimientos.Should().BeEquivalentTo([new VentanaDeMantenimiento()
        {
            Ambiente = "",
            HoraInicio = "",
            HoraFin = "",
            Dias = [],
        }]);
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenObtenerVerificarEstadoTest()
    {
        // Act
        var response = await estatusServiciosAPI.VerificarEstado(Ambiente.PreCertificacion, fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.Estado.Should().Be("Disponible");
    }
}