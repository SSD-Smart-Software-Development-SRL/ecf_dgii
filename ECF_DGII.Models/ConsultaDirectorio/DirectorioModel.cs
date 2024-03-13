namespace ECF_DGII.Models.ConsultaDirectorio;

public record DirectorioModel(
    string? Nombre,
    string? Rnc,
    string? UrlRecepcion,
    string? UrlAceptacion,
    string? UrlOpcional
);