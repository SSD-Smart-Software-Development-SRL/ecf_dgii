using ECF_DGII.Models.ConsultaDirectorio;
using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class ConsultaDirectorioTests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IConsultaDirectorioAPI consultaDirectorioAPI;

    public ConsultaDirectorioTests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        consultaDirectorioAPI = RestService.For<IConsultaDirectorioAPI>("https://ecf.dgii.gov.do/testecf");
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenListadoTest()
    {
        // Act
        var response = await consultaDirectorioAPI.Listado(fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNullOrEmpty();
        response.Content.Should().BeEquivalentTo([new Directorio("", "", "", "", "")]);
    }

    [Fact]
    [Trait("Type", "Integration")]
    public async Task WhenObtenerDirectorioPorRncTest()
    {
        // Act
        var response = await consultaDirectorioAPI.ObtenerDirectorioPorRnc("", fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNullOrEmpty();
        response.Content.Should().BeEquivalentTo([new DirectorioModel("", "", "", "", "")]);
    }
}