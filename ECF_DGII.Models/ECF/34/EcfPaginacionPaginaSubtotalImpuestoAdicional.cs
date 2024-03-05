using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF._34;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfPaginacionPaginaSubtotalImpuestoAdicional", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfPaginacionPaginaSubtotalImpuestoAdicional
{
    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("SubtotalImpuestoSelectivoConsumoEspecificoPagina", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalImpuestoSelectivoConsumoEspecificoPagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the SubtotalImpuestoSelectivoConsumoEspecificoPagina
    ///         property is specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalImpuestoSelectivoConsumoEspecificoPaginaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("SubtotalOtrosImpuesto", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalOtrosImpuesto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SubtotalOtrosImpuesto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalOtrosImpuestoSpecified { get; set; }
}