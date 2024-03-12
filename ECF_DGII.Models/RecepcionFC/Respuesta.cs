namespace ECF_DGII.Models.RecepcionFC;

public record Respuesta(
    EstadoCF Codigo,
    string? Estado,
    MensajeRespuesta[]? Mensajes,
    string? Enfc,
    bool SecuenciaUtilizada
);
