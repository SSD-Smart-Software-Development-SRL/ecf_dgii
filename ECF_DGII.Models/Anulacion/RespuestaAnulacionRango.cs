namespace ECF_DGII.Models.Anulacion;

public record RespuestaAnulacionRango(
    string? Rnc,
    string? Codigo,
    string? Nombre,
    string[]? Mensajes
);