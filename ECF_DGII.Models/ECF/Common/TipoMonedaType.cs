using System.CodeDom.Compiler;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("TipoMonedaType", Namespace = "")]
public enum TipoMonedaType
{
    [XmlEnum("BRL")] Brl,

    [XmlEnum("CAD")] Cad,

    [XmlEnum("CHF")] Chf,

    [XmlEnum("CHY")] Chy,

    [XmlEnum("XDR")] Xdr,

    [XmlEnum("DKK")] Dkk,

    [XmlEnum("EUR")] Eur,

    [XmlEnum("GBP")] Gbp,

    [XmlEnum("JPY")] Jpy,

    [XmlEnum("NOK")] Nok,

    [XmlEnum("SCP")] Scp,

    [XmlEnum("SEK")] Sek,

    [XmlEnum("USD")] Usd,

    [XmlEnum("VEF")] Vef,

    [XmlEnum("HTG")] Htg
}