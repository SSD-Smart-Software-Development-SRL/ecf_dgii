using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF._46;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoTotales", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoTotales
{
    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoGravadoTotal", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoGravadoTotal { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoGravadoTotal property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoGravadoTotalSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoGravadoI3", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoGravadoI3 { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoGravadoI3 property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoGravadoI3Specified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,2}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,2}")]
    [XmlElement("ITBIS3", Form = XmlSchemaForm.Unqualified)]
    public sbyte Itbis3 { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the Itbis3 property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool Itbis3Specified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("TotalITBIS", Form = XmlSchemaForm.Unqualified)]
    public decimal TotalItbis { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TotalItbis property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TotalItbisSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("TotalITBIS3", Form = XmlSchemaForm.Unqualified)]
    public decimal TotalItbis3 { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TotalItbis3 property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TotalItbis3Specified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [Required]
    [XmlElement("MontoTotal", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoTotal { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [+-]?[0-9]{1,16}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[+-]?[0-9]{1,16}(.[0-9]{1,2})?")]
    [XmlElement("MontoNoFacturable", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoNoFacturable { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoNoFacturable property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoNoFacturableSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [+-]?[0-9]{1,16}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[+-]?[0-9]{1,16}(.[0-9]{1,2})?")]
    [XmlElement("MontoPeriodo", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoPeriodo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoPeriodo property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoPeriodoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [+-]?[0-9]{1,16}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[+-]?[0-9]{1,16}(.[0-9]{1,2})?")]
    [XmlElement("SaldoAnterior", Form = XmlSchemaForm.Unqualified)]
    public decimal SaldoAnterior { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SaldoAnterior property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SaldoAnteriorSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoAvancePago", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoAvancePago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoAvancePago property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoAvancePagoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [+-]?[0-9]{1,16}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[+-]?[0-9]{1,16}(.[0-9]{1,2})?")]
    [XmlElement("ValorPagar", Form = XmlSchemaForm.Unqualified)]
    public decimal ValorPagar { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the ValorPagar property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool ValorPagarSpecified { get; set; }
}