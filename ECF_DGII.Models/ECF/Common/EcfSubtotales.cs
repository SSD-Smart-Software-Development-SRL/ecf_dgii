using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF._47;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfSubtotales", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfSubtotales
{
    [XmlIgnore] private Collection<EcfSubtotalesSubtotal> _subtotal;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfSubtotales" /> class.</para>
    /// </summary>
    public EcfSubtotales()
    {
        _subtotal = new Collection<EcfSubtotalesSubtotal>();
    }

    [Required]
    [XmlElement("Subtotal", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfSubtotalesSubtotal> Subtotal
    {
        get => _subtotal;
        private set => _subtotal = value;
    }
}