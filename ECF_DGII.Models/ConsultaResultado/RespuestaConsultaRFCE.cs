namespace ECF_DGII.Models.ConsultaResultado;

public record RespuestaConsultaTrackId(
    string? TrackId,
    string? Codigo,
    string? Estado,
    string? Rnc,
    string? Encf,
    bool SecuenciaUtilizada,
    string? FechaRecepcion,
    Mensaje[]? Mensajes
);
