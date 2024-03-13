using ECF_DGII.Models.ConsultaTrackId;
using Refit;

namespace ECF_DGII.SDK;

public interface IConsultaTrackIdAPI
{
    [Get("/consultatrackids/api/TrackIds/Consulta")]
    Task<IApiResponse<TrackingDetalle>> Consulta(
        string RncEmisor,
        string Encf,
        [Authorize] string apiKey);
}
