namespace ECF_DGII.Models.EstatusServicios;

public record VentanaDeMantenimiento
{
    public string? Ambiente { get; init; }
    public string? HoraInicio { get; init; }
    public string? HoraFin { get; init; }
    public string[]? Dias { get; init; }
}