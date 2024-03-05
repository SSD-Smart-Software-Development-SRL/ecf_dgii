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
[XmlType("EcfEncabezadoIdDocTablaFormasPago", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoIdDocTablaFormasPago
{
    [XmlIgnore] private Collection<EcfEncabezadoIdDocTablaFormasPagoFormaDePago> _formaDePago;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfEncabezadoIdDocTablaFormasPago" /> class.</para>
    /// </summary>
    public EcfEncabezadoIdDocTablaFormasPago()
    {
        _formaDePago = new Collection<EcfEncabezadoIdDocTablaFormasPagoFormaDePago>();
    }

    [Required]
    [XmlElement("FormaDePago", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfEncabezadoIdDocTablaFormasPagoFormaDePago> FormaDePago
    {
        get => _formaDePago;
        private set => _formaDePago = value;
    }
}