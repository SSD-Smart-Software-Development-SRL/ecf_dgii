using System.Collections.Frozen;
using System.Reflection;
using System.Xml.Schema;

namespace ECF_DGII.Models;

public static class XsdHandler
{
    public static readonly FrozenDictionary<string, XmlSchemaSet> XmlSchemaSet = new Dictionary<string, XmlSchemaSet>
    {
        { "ARECF.ARECF v1.0.xsd", new() },
        { "Autenticacion.Semilla v.1.0.xsd", new() },
        { "ECF.e-CF 31 v.1.0.xsd", new() },
        { "ECF.e-CF 32 v.1.0.xsd", new() },
        { "ECF.e-CF 33 v.1.0.xsd", new() },
        { "ECF.e-CF 34 v.1.0.xsd", new() },
        { "ECF.e-CF 41 v.1.0.xsd", new() },
        { "ECF.e-CF 43 v.1.0.xsd", new() },
        { "ECF.e-CF 44 v.1.0.xsd", new() },
        { "ECF.e-CF 45 v.1.0.xsd", new() },
        { "ECF.e-CF 46 v.1.0.xsd", new() },
        { "ECF.e-CF 47 v.1.0.xsd", new() }
    }.ToFrozenDictionary();

    static XsdHandler()
    {
        var assembly = Assembly.GetExecutingAssembly();

        foreach (var resourceName in XmlSchemaSet.Keys)
        {
            using var stream = assembly.GetManifestResourceStream(resourceName) ??
                               throw new Exception($"Resource not found: {resourceName}");
            var schema = XmlSchema.Read(stream, null) ?? throw new Exception($"Error loading {resourceName}");
            XmlSchemaSet[resourceName].Add(schema);
        }
    }
}