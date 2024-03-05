using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF._44;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfPaginacionPagina", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfPaginacionPagina
{
    /// <summary>
    ///     <para xml:lang="en">Minimum inclusive value: 1.</para>
    ///     <para xml:lang="en">Maximum inclusive value: 1000.</para>
    ///     <para xml:lang="en">Total number of digits: 4.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,4}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,4}")]
    [Range(typeof(decimal), "1", "1000")]
    [XmlElement("PaginaNo", Form = XmlSchemaForm.Unqualified)]
    public ushort PaginaNo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the PaginaNo property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool PaginaNoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum inclusive value: 1.</para>
    ///     <para xml:lang="en">Maximum inclusive value: 1000.</para>
    ///     <para xml:lang="en">Total number of digits: 4.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,4}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,4}")]
    [Range(typeof(decimal), "1", "1000")]
    [XmlElement("NoLineaDesde", Form = XmlSchemaForm.Unqualified)]
    public ushort NoLineaDesde { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the NoLineaDesde property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool NoLineaDesdeSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum inclusive value: 1.</para>
    ///     <para xml:lang="en">Maximum inclusive value: 1000.</para>
    ///     <para xml:lang="en">Total number of digits: 4.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,4}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,4}")]
    [Range(typeof(decimal), "1", "1000")]
    [XmlElement("NoLineaHasta", Form = XmlSchemaForm.Unqualified)]
    public ushort NoLineaHasta { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the NoLineaHasta property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool NoLineaHastaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("SubtotalExentoPagina", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalExentoPagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SubtotalExentoPagina property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalExentoPaginaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("SubtotalImpuestoAdicionalPagina", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalImpuestoAdicionalPagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the SubtotalImpuestoAdicionalPagina property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalImpuestoAdicionalPaginaSpecified { get; set; }

    [XmlElement("SubtotalImpuestoAdicional", Form = XmlSchemaForm.Unqualified)]
    public EcfPaginacionPaginaSubtotalImpuestoAdicional SubtotalImpuestoAdicional { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoSubtotalPagina", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoSubtotalPagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoSubtotalPagina property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoSubtotalPaginaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("SubtotalMontoNoFacturablePagina", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalMontoNoFacturablePagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the SubtotalMontoNoFacturablePagina property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalMontoNoFacturablePaginaSpecified { get; set; }
}