namespace ECF_DGII.Models.RespuestaAprobacionComercial;

public record RespuestaAprobacionComercial(
    string? Codigo,
    string? Estado,
    string[]? Mensaje
);