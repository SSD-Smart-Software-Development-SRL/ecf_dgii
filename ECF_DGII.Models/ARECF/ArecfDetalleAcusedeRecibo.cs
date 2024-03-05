using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ARECF;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("ArecfDetalleAcusedeRecibo", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class ArecfDetalleAcusedeRecibo
{
    [Required]
    [XmlElement("Version", Form = XmlSchemaForm.Unqualified)]
    public VersionType Version { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: [0-9]{11}|[0-9]{9}.</para>
    /// </summary>
    [RegularExpression("[0-9]{11}|[0-9]{9}")]
    [Required]
    [XmlElement("RNCEmisor", Form = XmlSchemaForm.Unqualified)]
    public string RncEmisor { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: [0-9]{11}|[0-9]{9}.</para>
    /// </summary>
    [RegularExpression("[0-9]{11}|[0-9]{9}")]
    [Required]
    [XmlElement("RNCComprador", Form = XmlSchemaForm.Unqualified)]
    public string RncComprador { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 9.</para>
    ///     <para xml:lang="en">Maximum length: 13.</para>
    ///     <para xml:lang="en">Pattern: ([a-z0-9A-Z]{13,13})|([a-z0-9A-Z]{11,11})|([a-z0-9A-Z]{9,9})*.</para>
    /// </summary>
    [MinLength(9)]
    [MaxLength(13)]
    [RegularExpression("([a-z0-9A-Z]{13,13})|([a-z0-9A-Z]{11,11})|([a-z0-9A-Z]{9,9})*")]
    [Required]
    [XmlElement("eNCF", Form = XmlSchemaForm.Unqualified)]
    public string Encf { get; set; }

    [Required]
    [XmlElement("Estado", Form = XmlSchemaForm.Unqualified)]
    public EstadoType Estado { get; set; }

    [XmlElement("CodigoMotivoNoRecibido", Form = XmlSchemaForm.Unqualified)]
    public CodigoMotivoNoRecibidoType CodigoMotivoNoRecibido { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the CodigoMotivoNoRecibido property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool CodigoMotivoNoRecibidoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Pattern: (3[01]|[12][0-9]|0[1-9])-(1[0-2]|0[1-9])-[0-9]{4}
    ///         (2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9]).
    ///     </para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0[1-9])-(1[0-2]|0[1-9])-[0-9]{4} (2[0-3]|[01]?[0-9]):([0-5]?[0-9" +
                       "]):([0-5]?[0-9])")]
    [Required]
    [XmlElement("FechaHoraAcuseRecibo", Form = XmlSchemaForm.Unqualified)]
    public string FechaHoraAcuseRecibo { get; set; }
}