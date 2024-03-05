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
[XmlType("EcfDetallesItemsItemTablaImpuestoAdicional", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaImpuestoAdicional
{
    [XmlIgnore] private Collection<EcfDetallesItemsItemTablaImpuestoAdicionalImpuestoAdicional> _impuestoAdicional;

    /// <summary>
    ///     <para xml:lang="en">
    ///         Initializes a new instance of the <see cref="EcfDetallesItemsItemTablaImpuestoAdicional" />
    ///         class.
    ///     </para>
    /// </summary>
    public EcfDetallesItemsItemTablaImpuestoAdicional()
    {
        _impuestoAdicional = new Collection<EcfDetallesItemsItemTablaImpuestoAdicionalImpuestoAdicional>();
    }

    [Required]
    [XmlElement("ImpuestoAdicional", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDetallesItemsItemTablaImpuestoAdicionalImpuestoAdicional> ImpuestoAdicional
    {
        get => _impuestoAdicional;
        private set => _impuestoAdicional = value;
    }
}