using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemTablaSubDescuentoSubDescuento", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaSubDescuentoSubDescuento
{
    [Required]
    [XmlElement("TipoSubDescuento", Form = XmlSchemaForm.Unqualified)]
    public TipoDescuentoRecargoType TipoSubDescuento { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 5.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,3}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,3}(.[0-9]{1,2})?")]
    [XmlElement("SubDescuentoPorcentaje", Form = XmlSchemaForm.Unqualified)]
    public decimal SubDescuentoPorcentaje { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SubDescuentoPorcentaje property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubDescuentoPorcentajeSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoSubDescuento", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoSubDescuento { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoSubDescuento property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoSubDescuentoSpecified { get; set; }
}