using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class ConsultaEstadoTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IConsultaEstadoAPI consultaEstadoAPI;

    public ConsultaEstadoTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        consultaEstadoAPI = RestService.For<IConsultaEstadoAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenConsultaEstadoTest()
    {
        // Act
        var response = await consultaEstadoAPI.Estado("", "", "", "", fixture.APIKey);
        
        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.Codigo.Should().BeGreaterThan(100);
        response.Content.Estado.Should().NotBeEmpty();
        response.Content.RncEmisor.Should().NotBeEmpty();
        response.Content.NcfElectronico.Should().NotBeEmpty();
        response.Content.MontoTotal.Should().BeGreaterThan(100000000);
        response.Content.TotalITBIS.Should().BeGreaterThan(100000000);
        response.Content.FechaEmision.Should().NotBeEmpty();
        response.Content.FechaFirma.Should().NotBeEmpty();
        response.Content.RncComprador.Should().NotBeEmpty();
        response.Content.CodigoSeguridad.Should().NotBeEmpty();
        response.Content.IdExtranjero.Should().NotBeEmpty();
    }
}