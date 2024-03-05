using System.CodeDom.Compiler;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("TipoCuentaPagoType", Namespace = "")]
public enum TipoCuentaPagoType
{
    [XmlEnum("CT")] Ct,

    [XmlEnum("AH")] Ah,

    [XmlEnum("OT")] Ot
}