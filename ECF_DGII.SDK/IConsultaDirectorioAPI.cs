using ECF_DGII.Models.ConsultaDirectorio;
using Refit;

namespace ECF_DGII.SDK;

public interface IConsultaDirectorioAPI
{
    [Get("/consultadirectorio/api/Consultas/Listado")]
    Task<IApiResponse<Directorio[]>> Listado([Authorize] string apiKey);

    [Get("/consultadirectorio/api/Consultas/ObtenerDirectorioPorRnc")]
    Task<IApiResponse<DirectorioModel[]>> ObtenerDirectorioPorRnc(string RNC, [Authorize] string apiKey);
}
