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
[XmlType("EcfEncabezadoOtraMoneda", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoOtraMoneda
{
    [XmlElement("TipoMoneda", Form = XmlSchemaForm.Unqualified)]
    public TipoMonedaType TipoMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TipoMoneda property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TipoMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 7.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 4.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,3}(.[0-9]{1,4})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,3}(.[0-9]{1,4})?")]
    [XmlElement("TipoCambio", Form = XmlSchemaForm.Unqualified)]
    public decimal TipoCambio { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TipoCambio property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TipoCambioSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoExentoOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoExentoOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoExentoOtraMoneda property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoExentoOtraMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoTotalOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoTotalOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoTotalOtraMoneda property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoTotalOtraMonedaSpecified { get; set; }
}