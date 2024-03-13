using ECF_DGII.Models.EstatusServicios;
using Refit;

namespace ECF_DGII.SDK;

public interface IEstatusServiciosAPI
{
    [Get("/api/EstatusServicios/ObtenerEstatus")]
    Task<IApiResponse<RespuestaEstatusServicio[]>> ObtenerEstatus([Authorize] string apiKey);

    [Get("/api/EstatusServicios/ObtenerVentanasMantenimiento")]
    Task<IApiResponse<RespuestaVentanaDeMantenimiento>> ObtenerVentanasMantenimiento([Authorize] string apiKey);

    [Get("/api/EstatusServicios/VerificarEstado")]
    Task<IApiResponse<RespuestaEstado>> VerificarEstado(Ambiente ambiente, [Authorize] string apiKey);
}
