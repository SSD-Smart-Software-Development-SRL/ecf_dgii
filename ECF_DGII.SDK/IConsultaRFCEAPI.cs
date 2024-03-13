using ECF_DGII.Models.ConsultaRFCE;
using Refit;

namespace ECF_DGII.SDK;

public interface IConsultaRFCEAPI
{
    [Get("/ecf/consultarfce/api/Consultas/Consulta")]
    Task<IApiResponse<RespuestaConsultaRFCE>> Consulta(
        string RNC_Emisor,
        string ENCF,
        string Cod_Seguridad_eCF,
        [Authorize] string apiKey);
}
