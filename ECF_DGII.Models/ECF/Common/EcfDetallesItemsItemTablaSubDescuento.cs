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
[XmlType("EcfDetallesItemsItemTablaSubDescuento", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaSubDescuento
{
    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaSubDescuentoSubDescuento> _subDescuento;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfDetallesItemsItemTablaSubDescuento" /> class.</para>
    /// </summary>
    public EcfDetallesItemsItemTablaSubDescuento()
    {
        _subDescuento = new Collection<EcfDetallesItemsItemTablaSubDescuentoSubDescuento>();
    }

    [Required]
    [XmlElement("SubDescuento", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaSubDescuentoSubDescuento> SubDescuento
    {
        get => _subDescuento;
        private set => _subDescuento = value;
    }
}