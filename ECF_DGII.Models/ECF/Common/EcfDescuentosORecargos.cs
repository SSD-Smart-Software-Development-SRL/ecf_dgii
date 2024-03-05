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
[XmlType("EcfDescuentosORecargos", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDescuentosORecargos
{
    [XmlIgnore] private Collection<EcfDescuentosORecargosDescuentoORecargo> _descuentoORecargo;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfDescuentosORecargos" /> class.</para>
    /// </summary>
    public EcfDescuentosORecargos()
    {
        _descuentoORecargo = new Collection<EcfDescuentosORecargosDescuentoORecargo>();
    }

    [Required]
    [XmlElement("DescuentoORecargo", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfDescuentosORecargosDescuentoORecargo> DescuentoORecargo
    {
        get => _descuentoORecargo;
        private set => _descuentoORecargo = value;
    }
}