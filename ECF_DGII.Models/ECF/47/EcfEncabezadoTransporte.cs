using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF._47;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoTransporte", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoTransporte
{
    /// <summary>
    ///     <para xml:lang="en">Maximum length: 60.</para>
    ///     <para xml:lang="en">Pattern: [a-zA-ZñÑáéíóúÁÉÍÓÚ,\s]*.</para>
    /// </summary>
    [MaxLength(60)]
    [RegularExpression("[a-zA-ZñÑáéíóúÁÉÍÓÚ,\\s]*")]
    [XmlElement("PaisDestino", Form = XmlSchemaForm.Unqualified)]
    public string PaisDestino { get; set; }
}