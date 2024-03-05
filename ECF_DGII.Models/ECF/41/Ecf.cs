using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF._41;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("ECF", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
[XmlRoot("ECF", Namespace = "")]
public class Ecf
{
    [XmlIgnore] private Collection<EcfDescuentosORecargosDescuentoORecargo> _descuentosORecargos;

    [XmlIgnore] private Collection<EcfDetallesItemsItem> _detallesItems;

    [XmlIgnore] private Collection<EcfPaginacionPagina> _paginacion;

    [XmlIgnore] private Collection<EcfSubtotalesSubtotal> _subtotales;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="Ecf" /> class.</para>
    /// </summary>
    public Ecf()
    {
        _detallesItems = new Collection<EcfDetallesItemsItem>();
        _subtotales = new Collection<EcfSubtotalesSubtotal>();
        _descuentosORecargos = new Collection<EcfDescuentosORecargosDescuentoORecargo>();
        _paginacion = new Collection<EcfPaginacionPagina>();
    }

    [Required]
    [XmlElement("Encabezado", Form = XmlSchemaForm.Unqualified)]
    public EcfEncabezado Encabezado { get; set; }

    [Required]
    [XmlArray("DetallesItems", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("Item", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItem> DetallesItems
    {
        get => _detallesItems;
        private set => _detallesItems = value;
    }

    [XmlArray("Subtotales", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("Subtotal", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfSubtotalesSubtotal> Subtotales
    {
        get => _subtotales;
        private set => _subtotales = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the Subtotales collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubtotalesSpecified => Subtotales.Count != 0;

    [XmlArray("DescuentosORecargos", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("DescuentoORecargo", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDescuentosORecargosDescuentoORecargo> DescuentosORecargos
    {
        get => _descuentosORecargos;
        private set => _descuentosORecargos = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the DescuentosORecargos collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool DescuentosORecargosSpecified => DescuentosORecargos.Count != 0;

    [XmlArray("Paginacion", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("Pagina", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfPaginacionPagina> Paginacion
    {
        get => _paginacion;
        private set => _paginacion = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the Paginacion collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool PaginacionSpecified => Paginacion.Count != 0;

    [XmlElement("InformacionReferencia", Form = XmlSchemaForm.Unqualified)]
    public EcfInformacionReferencia InformacionReferencia { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 19.</para>
    ///     <para xml:lang="en">
    ///         Pattern: (3[01]|[12][0-9]|0[1-9])-(1[0-2]|0[1-9])-((19|20)\d{2})
    ///         (2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9]).
    ///     </para>
    /// </summary>
    [MaxLength(19)]
    [RegularExpression("(3[01]|[12][0-9]|0[1-9])-(1[0-2]|0[1-9])-((19|20)\\d{2}) (2[0-3]|[01]?[0-9]):([0-5" +
                       "]?[0-9]):([0-5]?[0-9])")]
    [Required]
    [XmlElement("FechaHoraFirma", Form = XmlSchemaForm.Unqualified)]
    public string FechaHoraFirma { get; set; }

    [Required] [XmlAnyElement] public XmlElement Any { get; set; }
}