namespace ECF_DGII.Models.ConsultaRFCE;

public record RespuestaConsultaRFCE
{
    public string? Rnc { get; init; }
    public string Encf { get; init; }
    public bool SecuenciaUtilizada { get; init; }
    public string? Codigo { get; init; }
    public string? Estado { get; init; }
    public Mensaje[]? Mensajes { get; init; }
}