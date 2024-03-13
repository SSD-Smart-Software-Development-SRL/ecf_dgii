using ECF_DGII.Models.Autenticacion;
using Refit;

namespace ECF_DGII.SDK;

public interface IAutenticacionAPI
{
    [Get("/autenticacion/api/Autenticacion/Semilla")]
    Task<IApiResponse<Stream>> Semilla();

    [Post("/autenticacion/api/Autenticacion/ValidarSemilla"), Multipart]
    Task<IApiResponse<RespuestaSemilla>> ValidarSemilla(StreamPart xml);
}
