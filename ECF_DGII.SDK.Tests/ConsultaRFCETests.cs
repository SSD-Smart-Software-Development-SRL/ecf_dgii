using ECF_DGII.SDK.Tests.Fixture;
using FluentAssertions;
using Refit;

namespace ECF_DGII.SDK.Tests;

[Collection("DGIIAPITests")]
public class ConsultaRFCETests
{
    private readonly WithDGIIAPIKeyFixture fixture;
    private readonly IConsultaRFCEAPI consultaRFCEAPI;

    public ConsultaRFCETests(WithDGIIAPIKeyFixture fixture)
    {
        this.fixture = fixture;
        consultaRFCEAPI = RestService.For<IConsultaRFCEAPI>("https://fc.dgii.gov.do");
    }

    [Fact]
    public async Task WhenConsultaRFCE()
    {
        // Act
        var response = await consultaRFCEAPI.Consulta("", "", "", fixture.APIKey);

        // Assert
        response.IsSuccessStatusCode.Should().BeTrue();
        response.Error.Should().BeNull();
        response.Content.Should().NotBeNull();
        response.Content.Rnc.Should().NotBeEmpty();
        response.Content.Encf.Should().BeEmpty();
        response.Content.SecuenciaUtilizada.Should().BeTrue();
        response.Content.Codigo.Should().NotBeEmpty();
        response.Content.Estado.Should().NotBeEmpty();
        response.Content.Mensajes.Should().BeEmpty();
    }
}