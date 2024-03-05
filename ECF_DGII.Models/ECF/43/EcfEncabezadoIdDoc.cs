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
[XmlType("EcfEncabezadoIdDoc", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoIdDoc
{
    [Required]
    [XmlElement("TipoeCF", Form = XmlSchemaForm.Unqualified)]
    public TipoeCfType TipoeCf { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 13.</para>
    ///     <para xml:lang="en">Maximum length: 13.</para>
    ///     <para xml:lang="en">Pattern: ([a-z0-9A-Z]{13}).</para>
    /// </summary>
    [MinLength(13)]
    [MaxLength(13)]
    [RegularExpression("([a-z0-9A-Z]{13})")]
    [Required]
    [XmlElement("eNCF", Form = XmlSchemaForm.Unqualified)]
    public string Encf { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [Required]
    [XmlElement("FechaVencimientoSecuencia", Form = XmlSchemaForm.Unqualified)]
    public string FechaVencimientoSecuencia { get; set; }

    [XmlElement("TipoPago", Form = XmlSchemaForm.Unqualified)]
    public TipoPagoType TipoPago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TipoPago property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TipoPagoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 1.</para>
    ///     <para xml:lang="en">Total number of digits: 4.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,4}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,4}")]
    [XmlElement("TotalPaginas", Form = XmlSchemaForm.Unqualified)]
    public short TotalPaginas { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TotalPaginas property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TotalPaginasSpecified { get; set; }
}