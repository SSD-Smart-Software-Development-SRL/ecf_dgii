using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF._46;

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
    [XmlElement("SubtotalMontoGravadoPagina", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalMontoGravadoPagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SubtotalMontoGravadoPagina property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalMontoGravadoPaginaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("SubtotalMontoGravado3Pagina", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalMontoGravado3Pagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SubtotalMontoGravado3Pagina property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalMontoGravado3PaginaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("SubtotalItbisPagina", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalItbisPagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SubtotalItbisPagina property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalItbisPaginaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("SubtotalItbis3Pagina", Form = XmlSchemaForm.Unqualified)]
    public decimal SubtotalItbis3Pagina { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the SubtotalItbis3Pagina property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalItbis3PaginaSpecified { get; set; }

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