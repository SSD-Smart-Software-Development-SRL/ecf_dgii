using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._47;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfInformacionReferencia", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfInformacionReferencia
{
    /// <summary>
    ///     <para xml:lang="en">Minimum length: 11.</para>
    ///     <para xml:lang="en">Maximum length: 19.</para>
    /// </summary>
    [MinLength(11)]
    [MaxLength(19)]
    [XmlElement("NCFModificado", Form = XmlSchemaForm.Unqualified)]
    public string NcfModificado { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: [0-9]{11}|[0-9]{9}.</para>
    /// </summary>
    [RegularExpression("[0-9]{11}|[0-9]{9}")]
    [XmlElement("RNCOtroContribuyente", Form = XmlSchemaForm.Unqualified)]
    public string RncOtroContribuyente { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaNCFModificado", Form = XmlSchemaForm.Unqualified)]
    public string FechaNcfModificado { get; set; }

    [XmlElement("CodigoModificacion", Form = XmlSchemaForm.Unqualified)]
    public CodigoModificacionType CodigoModificacion { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the CodigoModificacion property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool CodigoModificacionSpecified { get; set; }
}