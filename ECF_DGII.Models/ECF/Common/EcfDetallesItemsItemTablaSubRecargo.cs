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
[XmlType("EcfDetallesItemsItemTablaSubRecargo", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaSubRecargo
{
    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaSubRecargoSubRecargo> _subRecargo;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfDetallesItemsItemTablaSubRecargo" /> class.</para>
    /// </summary>
    public EcfDetallesItemsItemTablaSubRecargo()
    {
        _subRecargo = new Collection<EcfDetallesItemsItemTablaSubRecargoSubRecargo>();
    }

    [Required]
    [XmlElement("SubRecargo", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaSubRecargoSubRecargo> SubRecargo
    {
        get => _subRecargo;
        private set => _subRecargo = value;
    }
}