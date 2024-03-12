namespace ECF_DGII.Models.ConsultaRFCE;

public record RespuestaConsultaRFCE(
    string? Rnc,
    string Encf,
    bool SecuenciaUtilizada,
    string? Codigo,
    string? Estado,
    Mensaje[]? Mensajes
);
