namespace ECF_DGII.Models.EstatusServicios;

public record RespuestaEstatusServicio
{
    public string? Servicio { get; init; }
    public string? Status { get; init; }
    public string? Ambiente { get; init; }
}

