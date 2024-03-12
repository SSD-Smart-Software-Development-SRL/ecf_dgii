namespace ECF_DGII.Models.ConsultaEstado;

public record RespuestaConsultaEstado(
    int Codigo,
    string? Estado,
    string? RncEmisor,
    string? NcfElectronico,
    double? MontoTotal,
    double? TotalITBIS,
    string? FechaEmision,
    string? FechaFirma,
    string? RncComprador,
    string? CodigoSeguridad,
    string? IdExtranjero
);
