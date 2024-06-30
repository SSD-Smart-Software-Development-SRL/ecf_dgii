namespace ECF_DGII.Models.RespuestaAprobacionComercial;

public record RespuestaAprobacionComercial
{
    public string? Codigo { get; init; }
    public string? Estado { get; init; }
    public string[]? Mensaje { get; init; }
};