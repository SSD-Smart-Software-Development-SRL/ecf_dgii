namespace ECF_DGII.Models.Anulacion;

public record RespuestaAnulacionRango
{
    public string? Rnc { get; init; }
    public string? Codigo { get; init; }
    public string? Nombre { get; init; }
    public string[]? Mensajes { get; init; }
}