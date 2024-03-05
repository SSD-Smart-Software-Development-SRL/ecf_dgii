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
[XmlType("EcfDetallesItemsItemTablaCodigosItem", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaCodigosItem
{
    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaCodigosItemCodigosItem> _codigosItem;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfDetallesItemsItemTablaCodigosItem" /> class.</para>
    /// </summary>
    public EcfDetallesItemsItemTablaCodigosItem()
    {
        _codigosItem = new Collection<EcfDetallesItemsItemTablaCodigosItemCodigosItem>();
    }

    [Required]
    [XmlElement("CodigosItem", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaCodigosItemCodigosItem> CodigosItem
    {
        get => _codigosItem;
        private set => _codigosItem = value;
    }
}