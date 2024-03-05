using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._31;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoTotalesImpuestosAdicionalesImpuestoAdicional", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoTotalesImpuestosAdicionalesImpuestoAdicional
{
    [Required]
    [XmlElement("TipoImpuesto", Form = XmlSchemaForm.Unqualified)]
    public CodificacionTipoImpuestosType TipoImpuesto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 5.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,3}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,3}(.[0-9]{1,2})?")]
    [Required]
    [XmlElement("TasaImpuestoAdicional", Form = XmlSchemaForm.Unqualified)]
    public decimal TasaImpuestoAdicional { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoImpuestoSelectivoConsumoEspecifico", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoImpuestoSelectivoConsumoEspecifico { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the MontoImpuestoSelectivoConsumoEspecifico property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool MontoImpuestoSelectivoConsumoEspecificoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoImpuestoSelectivoConsumoAdvalorem", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoImpuestoSelectivoConsumoAdvalorem { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the MontoImpuestoSelectivoConsumoAdvalorem property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool MontoImpuestoSelectivoConsumoAdvaloremSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("OtrosImpuestosAdicionales", Form = XmlSchemaForm.Unqualified)]
    public decimal OtrosImpuestosAdicionales { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the OtrosImpuestosAdicionales property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool OtrosImpuestosAdicionalesSpecified { get; set; }
}