using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._43;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezado", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezado
{
    [Required]
    [XmlElement("Version", Form = XmlSchemaForm.Unqualified)]
    public VersionType Version { get; set; }

    [Required]
    [XmlElement("IdDoc", Form = XmlSchemaForm.Unqualified)]
    public EcfEncabezadoIdDoc IdDoc { get; set; }

    [Required]
    [XmlElement("Emisor", Form = XmlSchemaForm.Unqualified)]
    public EcfEncabezadoEmisor Emisor { get; set; }

    [Required]
    [XmlElement("Totales", Form = XmlSchemaForm.Unqualified)]
    public EcfEncabezadoTotales Totales { get; set; }

    [XmlElement("OtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public EcfEncabezadoOtraMoneda OtraMoneda { get; set; }
}