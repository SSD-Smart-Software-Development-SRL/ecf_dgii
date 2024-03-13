using ECF_DGII.Models.RecepcionFC;
using Refit;

namespace ECF_DGII.SDK;

public interface IRecepcionFCAPI
{
    [Post("/recepcionfc/api/recepcion/ecf")]
    Task<IApiResponse<Respuesta>> Recepcion(StreamPart xml, [Authorize] string apiKey);
}
