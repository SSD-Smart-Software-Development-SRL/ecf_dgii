using ECF_DGII.Models.RespuestaAprobacionComercial;
using Refit;

namespace ECF_DGII.SDK;

public interface IAprobacionComercialAPI
{
    [Post("/aprobacioncomercial/api/AprobacionComercial")]
    Task<IApiResponse<RespuestaAprobacionComercial>> AprobacionComercial(StreamPart xml, [Authorize] string apiKey);
}
