using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.Autenticacion;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("SemillaModel", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
[XmlRoot("SemillaModel", Namespace = "")]
public class SemillaModel
{
    [Required]
    [XmlElement("valor", Form = XmlSchemaForm.Unqualified)]
    public string Valor { get; set; }

    [Required]
    [XmlElement("fecha", Form = XmlSchemaForm.Unqualified, DataType = "dateTime")]
    public DateTime Fecha { get; set; }

    [Required] [XmlAnyElement] public XmlElement Any { get; set; }
}