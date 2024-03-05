using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._44;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItem", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItem
{
    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaCodigosItemCodigosItem> _tablaCodigosItem;

    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaImpuestoAdicionalImpuestoAdicional> _tablaImpuestoAdicional;

    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaSubDescuentoSubDescuento> _tablaSubDescuento;

    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaSubRecargoSubRecargo> _tablaSubRecargo;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfDetallesItemsItem" /> class.</para>
    /// </summary>
    public EcfDetallesItemsItem()
    {
        _tablaCodigosItem = new Collection<EcfDetallesItemsItemTablaCodigosItemCodigosItem>();
        _tablaSubDescuento = new Collection<EcfDetallesItemsItemTablaSubDescuentoSubDescuento>();
        _tablaSubRecargo = new Collection<EcfDetallesItemsItemTablaSubRecargoSubRecargo>();
        _tablaImpuestoAdicional = new Collection<EcfDetallesItemsItemTablaImpuestoAdicionalImpuestoAdicional>();
    }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 4.</para>
    ///     <para xml:lang="en">Minimum inclusive value: 1.</para>
    ///     <para xml:lang="en">Maximum inclusive value: 1000.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{0,4}.</para>
    /// </summary>
    [RegularExpression("[0-9]{0,4}")]
    [Range(typeof(decimal), "1", "1000")]
    [Required]
    [XmlElement("NumeroLinea", Form = XmlSchemaForm.Unqualified)]
    public ushort NumeroLinea { get; set; }

    [XmlArray("TablaCodigosItem", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("CodigosItem", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaCodigosItemCodigosItem> TablaCodigosItem
    {
        get => _tablaCodigosItem;
        private set => _tablaCodigosItem = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the TablaCodigosItem collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool TablaCodigosItemSpecified => TablaCodigosItem.Count != 0;

    [Required]
    [XmlElement("IndicadorFacturacion", Form = XmlSchemaForm.Unqualified)]
    public IndicadorFacturacionType IndicadorFacturacion { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 80.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(80)]
    [Required]
    [XmlElement("NombreItem", Form = XmlSchemaForm.Unqualified)]
    public string NombreItem { get; set; }

    [Required]
    [XmlElement("IndicadorBienoServicio", Form = XmlSchemaForm.Unqualified)]
    public IndicadorBienoServicioType IndicadorBienoServicio { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 1000.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(1000)]
    [XmlElement("DescripcionItem", Form = XmlSchemaForm.Unqualified)]
    public string DescripcionItem { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [Required]
    [XmlElement("CantidadItem", Form = XmlSchemaForm.Unqualified)]
    public decimal CantidadItem { get; set; }

    [XmlElement("UnidadMedida", Form = XmlSchemaForm.Unqualified)]
    public UnidadMedidaType UnidadMedida { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the UnidadMedida property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool UnidadMedidaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaElaboracion", Form = XmlSchemaForm.Unqualified)]
    public string FechaElaboracion { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaVencimientoItem", Form = XmlSchemaForm.Unqualified)]
    public string FechaVencimientoItem { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 20.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 4.</para>
    ///     <para xml:lang="en">Pattern: (\d{1,16})(\.\d{1,4})?.</para>
    /// </summary>
    [RegularExpression("(\\d{1,16})(\\.\\d{1,4})?")]
    [Required]
    [XmlElement("PrecioUnitarioItem", Form = XmlSchemaForm.Unqualified)]
    public decimal PrecioUnitarioItem { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("DescuentoMonto", Form = XmlSchemaForm.Unqualified)]
    public decimal DescuentoMonto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the DescuentoMonto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool DescuentoMontoSpecified { get; set; }

    [XmlArray("TablaSubDescuento", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("SubDescuento", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaSubDescuentoSubDescuento> TablaSubDescuento
    {
        get => _tablaSubDescuento;
        private set => _tablaSubDescuento = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the TablaSubDescuento collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool TablaSubDescuentoSpecified => TablaSubDescuento.Count != 0;

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("RecargoMonto", Form = XmlSchemaForm.Unqualified)]
    public decimal RecargoMonto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the RecargoMonto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool RecargoMontoSpecified { get; set; }

    [XmlArray("TablaSubRecargo", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("SubRecargo", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaSubRecargoSubRecargo> TablaSubRecargo
    {
        get => _tablaSubRecargo;
        private set => _tablaSubRecargo = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the TablaSubRecargo collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool TablaSubRecargoSpecified => TablaSubRecargo.Count != 0;

    [XmlArray("TablaImpuestoAdicional", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("ImpuestoAdicional", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaImpuestoAdicionalImpuestoAdicional> TablaImpuestoAdicional
    {
        get => _tablaImpuestoAdicional;
        private set => _tablaImpuestoAdicional = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the TablaImpuestoAdicional collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool TablaImpuestoAdicionalSpecified => TablaImpuestoAdicional.Count != 0;

    [XmlElement("OtraMonedaDetalle", Form = XmlSchemaForm.Unqualified)]
    public EcfDetallesItemsItemOtraMonedaDetalle OtraMonedaDetalle { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [Required]
    [XmlElement("MontoItem", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoItem { get; set; }
}