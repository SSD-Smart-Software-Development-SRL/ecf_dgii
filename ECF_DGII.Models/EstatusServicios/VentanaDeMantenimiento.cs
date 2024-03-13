namespace ECF_DGII.Models.EstatusServicios;

public record VentanaDeMantenimiento(
    string? Ambiente,
    string? HoraInicio,
    string? HoraFin,
    string[]? Dias
);
