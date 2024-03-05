using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._31;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoIdDoc", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoIdDoc
{
    [XmlIgnore] private Collection<EcfEncabezadoIdDocTablaFormasPagoFormaDePago> _tablaFormasPago;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfEncabezadoIdDoc" /> class.</para>
    /// </summary>
    public EcfEncabezadoIdDoc()
    {
        _tablaFormasPago = new Collection<EcfEncabezadoIdDocTablaFormasPagoFormaDePago>();
    }

    [Required]
    [XmlElement("TipoeCF", Form = XmlSchemaForm.Unqualified)]
    public TipoeCfType TipoeCf { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 13.</para>
    ///     <para xml:lang="en">Maximum length: 13.</para>
    ///     <para xml:lang="en">Pattern: ([a-z0-9A-Z]{13}).</para>
    /// </summary>
    [MinLength(13)]
    [MaxLength(13)]
    [RegularExpression("([a-z0-9A-Z]{13})")]
    [Required]
    [XmlElement("eNCF", Form = XmlSchemaForm.Unqualified)]
    public string Encf { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [Required]
    [XmlElement("FechaVencimientoSecuencia", Form = XmlSchemaForm.Unqualified)]
    public string FechaVencimientoSecuencia { get; set; }

    [XmlElement("IndicadorEnvioDiferido", Form = XmlSchemaForm.Unqualified)]
    public IndicadorEnvioDiferidoType IndicadorEnvioDiferido { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the IndicadorEnvioDiferido property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool IndicadorEnvioDiferidoSpecified { get; set; }

    [XmlElement("IndicadorMontoGravado", Form = XmlSchemaForm.Unqualified)]
    public IndicadorMontoGravadoType IndicadorMontoGravado { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the IndicadorMontoGravado property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool IndicadorMontoGravadoSpecified { get; set; }

    [XmlElement("IndicadorServicioTodoIncluido", Form = XmlSchemaForm.Unqualified)]
    public IndicadorServicioTodoIncluidoType IndicadorServicioTodoIncluido { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the IndicadorServicioTodoIncluido property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool IndicadorServicioTodoIncluidoSpecified { get; set; }

    [Required]
    [XmlElement("TipoIngresos", Form = XmlSchemaForm.Unqualified)]
    public TipoIngresosValidationType TipoIngresos { get; set; }

    [Required]
    [XmlElement("TipoPago", Form = XmlSchemaForm.Unqualified)]
    public TipoPagoType TipoPago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaLimitePago", Form = XmlSchemaForm.Unqualified)]
    public string FechaLimitePago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: [\s\d\w]{1,15}.</para>
    /// </summary>
    [RegularExpression("[\\s\\d\\w]{1,15}")]
    [XmlElement("TerminoPago", Form = XmlSchemaForm.Unqualified)]
    public string TerminoPago { get; set; }

    [XmlArray("TablaFormasPago", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("FormaDePago", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfEncabezadoIdDocTablaFormasPagoFormaDePago> TablaFormasPago
    {
        get => _tablaFormasPago;
        private set => _tablaFormasPago = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the TablaFormasPago collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool TablaFormasPagoSpecified => TablaFormasPago.Count != 0;

    [XmlElement("TipoCuentaPago", Form = XmlSchemaForm.Unqualified)]
    public TipoCuentaPagoType TipoCuentaPago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TipoCuentaPago property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TipoCuentaPagoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 28.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(28)]
    [XmlElement("NumeroCuentaPago", Form = XmlSchemaForm.Unqualified)]
    public string NumeroCuentaPago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 75.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(75)]
    [XmlElement("BancoPago", Form = XmlSchemaForm.Unqualified)]
    public string BancoPago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaDesde", Form = XmlSchemaForm.Unqualified)]
    public string FechaDesde { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaHasta", Form = XmlSchemaForm.Unqualified)]
    public string FechaHasta { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 1.</para>
    ///     <para xml:lang="en">Total number of digits: 4.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,4}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,4}")]
    [XmlElement("TotalPaginas", Form = XmlSchemaForm.Unqualified)]
    public short TotalPaginas { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TotalPaginas property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TotalPaginasSpecified { get; set; }
}