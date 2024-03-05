using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF._44;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoTotales", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoTotales
{
    [XmlIgnore] private Collection<EcfEncabezadoTotalesImpuestosAdicionalesImpuestoAdicional> _impuestosAdicionales;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfEncabezadoTotales" /> class.</para>
    /// </summary>
    public EcfEncabezadoTotales()
    {
        _impuestosAdicionales = new Collection<EcfEncabezadoTotalesImpuestosAdicionalesImpuestoAdicional>();
    }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoExento", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoExento { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoExento property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoExentoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoImpuestoAdicional", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoImpuestoAdicional { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoImpuestoAdicional property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoImpuestoAdicionalSpecified { get; set; }

    [XmlArray("ImpuestosAdicionales", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("ImpuestoAdicional", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfEncabezadoTotalesImpuestosAdicionalesImpuestoAdicional> ImpuestosAdicionales
    {
        get => _impuestosAdicionales;
        private set => _impuestosAdicionales = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the ImpuestosAdicionales collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool ImpuestosAdicionalesSpecified => ImpuestosAdicionales.Count != 0;

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