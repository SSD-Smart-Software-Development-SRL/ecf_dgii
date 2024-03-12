using System.Security.Cryptography.X509Certificates;
using System.Security.Cryptography.Xml;
using System.Text;
using System.Xml;

namespace ECF_DGII.SDK.Tests.Extensions;

public static class XmlDocumentExtensions
{
    private static readonly XmlWriterSettings writerSettings = new()
    {
        Indent = false,
        OmitXmlDeclaration = false,
        Async = false,
        CloseOutput = false,
        Encoding = Encoding.UTF8
    };

    public static XmlDocument Sign(this XmlDocument xml, X509Certificate2 certificate)
    {
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

        return xml;
    }

    public static Stream ToStream(this XmlDocument xml)
    {
        var stream = new MemoryStream();
        var lastStreamPosition = stream.Position;
        using var xmlWriter = XmlWriter.Create(stream, writerSettings);
        xml.Save(xmlWriter);

        if (stream.CanSeek)
            stream.Position = lastStreamPosition;

        return stream;
    }
}