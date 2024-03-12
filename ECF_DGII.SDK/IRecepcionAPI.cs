using ECF_DGII.Models.Recepcion;
using Refit;

namespace ECF_DGII.SDK;

public interface IRecepcionAPI
{
    [Post("/recepcion/api/FacturasElectronicas")]
    Task<IApiResponse<RespuestaRecepcion>> FacturasElectronicas(StreamPart xml, [Authorize] string apiKey);
}
