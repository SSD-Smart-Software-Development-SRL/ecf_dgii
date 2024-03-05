using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemTablaSubRecargoSubRecargo", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaSubRecargoSubRecargo
{
    [Required]
    [XmlElement("TipoSubRecargo", Form = XmlSchemaForm.Unqualified)]
    public TipoDescuentoRecargoType TipoSubRecargo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 5.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,3}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,3}(.[0-9]{1,2})?")]
    [XmlElement("SubRecargoPorcentaje", Form = XmlSchemaForm.Unqualified)]
    public decimal SubRecargoPorcentaje { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SubRecargoPorcentaje property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubRecargoPorcentajeSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoSubRecargo", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoSubRecargo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoSubRecargo property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoSubRecargoSpecified { get; set; }
}