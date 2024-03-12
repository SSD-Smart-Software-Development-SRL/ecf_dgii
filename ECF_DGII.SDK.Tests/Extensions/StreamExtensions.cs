using System.Xml;

namespace ECF_DGII.SDK.Tests.Extensions;

internal static class StreamExtensions
{
    public static XmlDocument ToXmlDocument(this Stream stream)
    {
        var xmlDoc = new XmlDocument();
        xmlDoc.Load(stream);
        return xmlDoc;
    }
}