namespace ECF_DGII.Models.ConsultaDirectorio;

public record Directorio
{
    public string? Nombre { get; init; }
    public string? Rnc { get; init; }
    public string? UrlRecepcion { get; init; }
    public string? UrlAceptacion { get; init; }
    public string? UrlOpcional { get; init; }
}
