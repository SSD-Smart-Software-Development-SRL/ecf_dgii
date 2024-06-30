namespace ECF_DGII.Models.EstatusServicios;

public record RespuestaVentanaDeMantenimiento
{
    public VentanaDeMantenimiento[] VentanaMantenimientos { get; init; }
}
