# DGII ECF


| Paquetes  |              |
|-----------|--------------|
| Modelos   |[![NuGet Downloads](https://img.shields.io/nuget/dt/SSDDO.ECF_DGII.Models)](https://www.nuget.org/packages/SSDDO.ECF_DGII.SDK)|
| DGII SDK  |![NuGet Downloads](https://img.shields.io/nuget/dt/SSDDO.ECF_DGII.SDK)


Libraria que puede ser utilizada para implementar la factura electrónica en República Dominicana, acorde a los lineamientos de la DGII

## Ejemplo

1. Instalar la libreria desde Nuget
```sh
dotnet add package SSDDO.ECF_DGII.Models
dotnet add package SSDDO.ECF_DGII.SDK
```

2. Invocar el servicio requerido utilizando DGII SDK y de ser necesario parsear puedes utilizar los modelos ECF y serializarlos a xml para enviar la información de recepción EFC.

```csharp
// Program.cs, C# 6.0+
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using Microsoft.Extensions.Configuration;
using Refit;
using ECF_DGII.Models.Autenticacion;
using ECF_DGII.SDK;

// Conseguir API Token
const string urlAmbiente = "https://ecf.dgii.gov.do/testecf";
using var certificate = new X509Certificate(fileName: "./certificate.crt", password: "1234", keyStorageFlags: X509KeyStorageFlags.Exportable);

// Estas interfaces pueden ser definidas utilizando dependency injection, para más información ver la documentación de Refit
var autenticacionAPI = RestService.For<IAutenticacionAPI>(urlAmbiente);
var recepcionFCAPI = RestService.For<IRecepcionFCAPI>(urlAmbiente);

// Convierte stream a XmlDocument
static XmlDocument ToXmlDocument(Stream stream)
{
    var xmlDoc = new XmlDocument();
    xmlDoc.Load(stream);
    return xmlDoc;
}

// Convierte un XMLDocument to stream
Stream ToStream(XmlDocument xml)
{
    var stream = new MemoryStream();
    var lastStreamPosition = stream.Position;
    using var xmlWriter = XmlWriter.Create(stream, writerSettings);
    xml.Save(xmlWriter);

    if (stream.CanSeek)
        stream.Position = lastStreamPosition;

    return stream;
}

static void Sign(XmlDocument xml, X509Certificate2 certificate)
{
    // codigo adaptado del código de como firmar un XML documentado por la DGII
    using var privateKey = certificate.GetPrivateKey();
    var exportedKeyMaterial = privateKey.ToXmlString(true);
    privateKey.FromXmlString(exportedKeyMaterial);
    SignedXml signedXml = new(xml)
    {
        SigningKey = privateKey,
    };
    signedXml.SignedInfo.SignatureMethod = "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256";
    Reference reference = new()
    {
        DigestMethod = "http://www.w3.org/2001/04/xmlenc#sha256",
        Uri = string.Empty,
    };
    reference.AddTransform(new XmlDsigEnvelopedSignatureTransform());
    signedXml.AddReference(reference);
    KeyInfo keyInfo = new();
    keyInfo.AddClause(new KeyInfoX509Data(certificate));
    signedXml.KeyInfo = keyInfo;
    signedXml.ComputeSignature();
    var xmlFirmaDigital = signedXml.GetXml();
    xml.DocumentElement.AppendChild(xml.ImportNode(xmlFirmaDigital, true));
}

async Task<RespuestaSemilla> GetAPIToken() {
    using var semillaResponse = await autenticacionAPI.Semilla().ConfigureAwait(false);
    await using var responseStream = semillaResponse.Content;
    var xml = ToXmlDcoument(responseStream);
    Sign(xml, certificate)
    await using var signedSemillaStream = ToStream(xml);
    // Object stream necesitado por Refit para enviar un archivo en un request
    var streamPart = new StreamPart(signedSemillaStream, "00100000000-semilla.xml", "text/xml");
    var tokenResponse = await autenticacionAPI.ValidarSemilla(streamPart).ConfigureAwait(false);
    if (!tokenResponse.IsSuccessStatusCode)
        throw new InvalidOperationException($"Error `{tokenResponse.StatusCode}` getting SemillaRespuesta.", tokenResponse.Error);
    return tokenResponse.Content;
}

// Conseguir API token
var respuestaSemilla = GetAPIToken();

// Leer un archivo XML ya firmado o crear un xml utilizando uno de las clases definidas en `ECF_DGII.Models.ECF._31, 32... etc` 
// y firmarlo programaticamente
await using var recepcionFCXml = File.OpenRead("./Data/RecepcionFC.xml");
var streamPart = new StreamPart(recepcionFCXml, "101672919E3200000001.xml", "text/xml");
// Notar que el response es un objecto POCO, en este caso `Models.RecepcionFC.Respuesta`
var response = await recepcionFCAPI.Recepcion(streamPart, apiKey: respuestaSemilla.APIKey).ConfigureAwait(false);

// ...
```

> Las pruebas unitarias no han sido aun verificadas


## Por que utilizar esta libreria

- **Abstracción de complejidad:** El SDK proporciona una capa de abstracción que oculta la complejidad del protocolo HTTP y la gestión de conexiones, lo que permite a los desarrolladores enfocarse en la lógica de la aplicación en lugar de preocuparse por los detalles de la comunicación de red.
- **Facilidad de uso:** Al utilizar el SDK, los desarrolladores pueden interactuar con el API utilizando objetos y métodos familiares en lugar de tener que construir manualmente las solicitudes HTTP y analizar las respuestas. Esto reduce la curva de aprendizaje y acelera el desarrollo.
- **Consistencia y coherencia:** El SDK proporciona una interfaz coherente y consistente para interactuar con el API, lo que facilita el mantenimiento del código y garantiza que todas las interacciones con el API sigan las mejores prácticas.
- **Validación de datos:** El SDK incluye validación de datos integrada, lo que ayuda a garantizar que los datos enviados al API cumplan con los requisitos esperados, reduciendo así el riesgo de errores y fallos en tiempo de ejecución.
- **Manejo de errores:** El SDK proporcionará manejo de errores integrado, incluyendo la gestión de casos como timeouts, errores de red y respuestas inesperadas del API, lo que simplifica el código y mejora la robustez de la aplicación.
- **Actualizaciones y mantenimiento:** Al utilizar un SDK, los desarrolladores se benefician de las actualizaciones y mejoras continuas proporcionadas por el mantenimiento del SDK, lo que garantiza que el código esté siempre actualizado y sea compatible con las últimas versiones del API.
- **Documentación integrada:** El SDK incluirá la documentación integrada, incluyendo descripciones de métodos, ejemplos de uso y referencias de parámetros, lo que facilitará la comprensión y el uso del API.
- **Compatibilidad multiplataforma:** El SDK ofrecerá compatibilidad multiplataforma, lo que permitirá a los desarrolladores utilizar el mismo código para interactuar con el API desde diferentes entornos de desarrollo, como aplicaciones web, móviles o de escritorio.

> Aun con la facilidad que provee esta libreria otros aspectos como seguridad, almacenamiento de los xml, actualizacion, manejo de errores, reintentar request fallidos, entre otros tienen que ser desarrollados, lo que influira en el tiempo y costo de desarrollo. 
Para una implementacion completa que incluye seguridad, almacenamiento, web site administrativo, manejo de certificados, implementacion modulo de recepcion de ECF, listo para la certificación de la DGII y mas visita nuestro producto: [ECF SSD](https://ecf.sdd.com.do), nuestra herramienta es completa, segura, eficiente, y puede ser instalada de servidores On Premise, en la nube, o utilizar nuestra implementación SAAS de la herramienta. Visita el producto aquí https://ecf.ssd.com.do 

____

🇩🇴 Hecho con plátano power

_© Smart Software Development SSD SRL 2024_