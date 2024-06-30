namespace ECF_DGII.Models.Autenticacion;

public record RespuestaSemilla
{
    public string? Token { get; set; }
    public DateTime Expira { get; set; }
    public DateTime Expedido { get; set; }
}