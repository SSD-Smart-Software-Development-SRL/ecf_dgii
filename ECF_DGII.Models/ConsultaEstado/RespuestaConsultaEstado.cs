namespace ECF_DGII.Models.ConsultaEstado;

public record RespuestaConsultaEstado
{
    public int Codigo { get; init; }
    public string? Estado { get; init; }
    public string? RncEmisor { get; init; }
    public string? NcfElectronico { get; init; }
    public double? MontoTotal { get; init; }
    public double? TotalITBIS { get; init; }
    public string? FechaEmision { get; init; }
    public string? FechaFirma { get; init; }
    public string? RncComprador { get; init; }
    public string? CodigoSeguridad { get; init; }
    public string? IdExtranjero { get; init; }
}
