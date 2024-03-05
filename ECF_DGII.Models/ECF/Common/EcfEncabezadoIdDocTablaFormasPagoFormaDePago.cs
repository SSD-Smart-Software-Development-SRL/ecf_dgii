using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoIdDocTablaFormasPagoFormaDePago", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoIdDocTablaFormasPagoFormaDePago
{
    [Required]
    [XmlElement("FormaPago", Form = XmlSchemaForm.Unqualified)]
    public FormaPagoType FormaPago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [Required]
    [XmlElement("MontoPago", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoPago { get; set; }
}