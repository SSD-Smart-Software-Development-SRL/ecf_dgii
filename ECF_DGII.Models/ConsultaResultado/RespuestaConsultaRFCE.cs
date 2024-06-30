namespace ECF_DGII.Models.ConsultaResultado;

public record RespuestaConsultaTrackId
{
    public string? TrackId { get; init; }
    public string? Codigo { get; init; }
    public string? Estado { get; init; }
    public string? Rnc { get; init; }
    public string? Encf { get; init; }
    public bool SecuenciaUtilizada { get; init; }
    public string? FechaRecepcion { get; init; }
    public Mensaje[]? Mensajes { get; init; }
}