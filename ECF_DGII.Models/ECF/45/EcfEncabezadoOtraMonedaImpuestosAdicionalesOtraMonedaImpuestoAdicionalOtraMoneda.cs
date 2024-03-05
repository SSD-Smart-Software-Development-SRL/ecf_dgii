using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._45;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMonedaImpuestoAdicionalOtraMoneda", Namespace = "",
    AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMonedaImpuestoAdicionalOtraMoneda
{
    [XmlElement("TipoImpuestoOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public CodificacionTipoImpuestosType TipoImpuestoOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TipoImpuestoOtraMoneda property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TipoImpuestoOtraMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 5.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,3}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,3}(.[0-9]{1,2})?")]
    [XmlElement("TasaImpuestoAdicionalOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal TasaImpuestoAdicionalOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the TasaImpuestoAdicionalOtraMoneda property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool TasaImpuestoAdicionalOtraMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoImpuestoSelectivoConsumoEspecificoOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoImpuestoSelectivoConsumoEspecificoOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the MontoImpuestoSelectivoConsumoEspecificoOtraMoneda
    ///         property is specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool MontoImpuestoSelectivoConsumoEspecificoOtraMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoImpuestoSelectivoConsumoAdvaloremOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoImpuestoSelectivoConsumoAdvaloremOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the MontoImpuestoSelectivoConsumoAdvaloremOtraMoneda
    ///         property is specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool MontoImpuestoSelectivoConsumoAdvaloremOtraMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("OtrosImpuestosAdicionalesOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal OtrosImpuestosAdicionalesOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the OtrosImpuestosAdicionalesOtraMoneda property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool OtrosImpuestosAdicionalesOtraMonedaSpecified { get; set; }
}