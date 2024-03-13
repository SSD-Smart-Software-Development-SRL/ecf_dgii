using ECF_DGII.Models.Anulacion;
using Refit;

namespace ECF_DGII.SDK;

public interface IAnulacionAPI
{
    [Post("/anulacionrangos/api/Operaciones/AnularRango")]
    Task<IApiResponse<RespuestaAnulacionRango>> Operaciones(StreamPart xml, [Authorize] string apiKey);
}
