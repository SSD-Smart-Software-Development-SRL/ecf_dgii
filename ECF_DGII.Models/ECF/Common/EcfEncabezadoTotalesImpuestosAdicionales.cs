using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF._44;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoTotalesImpuestosAdicionales", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoTotalesImpuestosAdicionales
{
    [XmlIgnore] private Collection<EcfEncabezadoTotalesImpuestosAdicionalesImpuestoAdicional> _impuestoAdicional;

    /// <summary>
    ///     <para xml:lang="en">
    ///         Initializes a new instance of the <see cref="EcfEncabezadoTotalesImpuestosAdicionales" />
    ///         class.
    ///     </para>
    /// </summary>
    public EcfEncabezadoTotalesImpuestosAdicionales()
    {
        _impuestoAdicional = new Collection<EcfEncabezadoTotalesImpuestosAdicionalesImpuestoAdicional>();
    }

    [Required]
    [XmlElement("ImpuestoAdicional", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfEncabezadoTotalesImpuestosAdicionalesImpuestoAdicional> ImpuestoAdicional
    {
        get => _impuestoAdicional;
        private set => _impuestoAdicional = value;
    }
}