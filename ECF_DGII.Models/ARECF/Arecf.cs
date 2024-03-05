using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ARECF;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("ARECF", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
[XmlRoot("ARECF", Namespace = "")]
public class Arecf
{
    [Required]
    [XmlElement("DetalleAcusedeRecibo", Form = XmlSchemaForm.Unqualified)]
    public ArecfDetalleAcusedeRecibo DetalleAcusedeRecibo { get; set; }

    [XmlAnyElement] public XmlElement Any { get; set; }
}