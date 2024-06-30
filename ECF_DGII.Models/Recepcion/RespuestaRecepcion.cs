namespace ECF_DGII.Models.Recepcion;

public record RespuestaRecepcion
{
    public string? TrackId { get; init;}
    public string? Error { get; init;}
    public string? Mensaje { get; init;}
}