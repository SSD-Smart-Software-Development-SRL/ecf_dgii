using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF._45;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMoneda", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMoneda
{
    [XmlIgnore]
    private Collection<EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMonedaImpuestoAdicionalOtraMoneda>
        _impuestoAdicionalOtraMoneda;

    /// <summary>
    ///     <para xml:lang="en">
    ///         Initializes a new instance of the
    ///         <see cref="EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMoneda" /> class.
    ///     </para>
    /// </summary>
    public EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMoneda()
    {
        _impuestoAdicionalOtraMoneda =
            new Collection<EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMonedaImpuestoAdicionalOtraMoneda>();
    }

    [Required]
    [XmlElement("ImpuestoAdicionalOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfEncabezadoOtraMonedaImpuestosAdicionalesOtraMonedaImpuestoAdicionalOtraMoneda>
        ImpuestoAdicionalOtraMoneda
    {
        get => _impuestoAdicionalOtraMoneda;
        private set => _impuestoAdicionalOtraMoneda = value;
    }
}