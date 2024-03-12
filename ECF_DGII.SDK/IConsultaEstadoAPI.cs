using ECF_DGII.Models.ConsultaEstado;
using Refit;

namespace ECF_DGII.SDK;

public interface IConsultaEstadoAPI
{
    [Get("/consultaestado/api/Consultas/Estado")]
    Task<IApiResponse<RespuestaConsultaEstado>> Estado(
        string RncEmisor,
        string NcfElectronico,
        string RncComprador,
        string CodigoSeguridad,
        [Authorize] string apiKey);
}
