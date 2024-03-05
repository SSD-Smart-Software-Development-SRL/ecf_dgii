using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF._46;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItems", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItems
{
    [XmlIgnore] private Collection<EcfDetallesItemsItem> _item;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfDetallesItems" /> class.</para>
    /// </summary>
    public EcfDetallesItems()
    {
        _item = new Collection<EcfDetallesItemsItem>();
    }

    [Required]
    [XmlElement("Item", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItem> Item
    {
        get => _item;
        private set => _item = value;
    }
}