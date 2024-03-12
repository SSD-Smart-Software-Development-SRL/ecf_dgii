namespace ECF_DGII.Models.ConsultaDirectorio;

public record Directorio(
    string? Nombre,
    string? Rnc,
    string? UrlRecepcion,
    string? UrlAceptacion,
    string? UrlOpcional
);
