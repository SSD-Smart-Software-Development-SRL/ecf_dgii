using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemTablaSubcantidadSubcantidadItem", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaSubcantidadSubcantidadItem
{
    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 19.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 3.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(.[0-9]{1,3})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(.[0-9]{1,3})?")]
    [XmlElement("Subcantidad", Form = XmlSchemaForm.Unqualified)]
    public decimal Subcantidad { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the Subcantidad property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SubcantidadSpecified { get; set; }

    [XmlElement("CodigoSubcantidad", Form = XmlSchemaForm.Unqualified)]
    public UnidadMedidaType CodigoSubcantidad { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the CodigoSubcantidad property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool CodigoSubcantidadSpecified { get; set; }
}