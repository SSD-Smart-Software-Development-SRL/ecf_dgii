using ECF_DGII.Models.ConsultaResultado;
using Refit;

namespace ECF_DGII.SDK;

public interface IConsultaResultadoAPI
{
    [Get("/consultaresultado/api/Consultas/Estado")]
    Task<IApiResponse<RespuestaConsultaTrackId>> Estado(
        string trackId,
        [Authorize] string apiKey);
}
