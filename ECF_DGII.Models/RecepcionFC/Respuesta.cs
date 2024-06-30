namespace ECF_DGII.Models.RecepcionFC;

public record Respuesta
{
    public EstadoCF Codigo { get; init; }
    public string? Estado { get; init; }
    public MensajeRespuesta[]? Mensajes { get; init; }
    public string? Enfc { get; init; }
    public bool SecuenciaUtilizada { get; init; }
}
