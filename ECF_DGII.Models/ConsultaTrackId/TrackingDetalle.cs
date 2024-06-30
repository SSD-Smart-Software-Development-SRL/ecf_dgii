namespace ECF_DGII.Models.ConsultaTrackId;

public record TrackingDetalle
{
    public string? TrackId { get; init; }
    public string? Estado { get; init; }
    public string? FechaRecepcion { get; init; }
}