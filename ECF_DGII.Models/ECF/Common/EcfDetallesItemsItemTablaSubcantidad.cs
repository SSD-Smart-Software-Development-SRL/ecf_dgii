using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemTablaSubcantidad", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaSubcantidad
{
    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaSubcantidadSubcantidadItem> _subcantidadItem;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfDetallesItemsItemTablaSubcantidad" /> class.</para>
    /// </summary>
    public EcfDetallesItemsItemTablaSubcantidad()
    {
        _subcantidadItem = new Collection<EcfDetallesItemsItemTablaSubcantidadSubcantidadItem>();
    }

    [Required]
    [XmlElement("SubcantidadItem", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaSubcantidadSubcantidadItem> SubcantidadItem
    {
        get => _subcantidadItem;
        private set => _subcantidadItem = value;
    }
}