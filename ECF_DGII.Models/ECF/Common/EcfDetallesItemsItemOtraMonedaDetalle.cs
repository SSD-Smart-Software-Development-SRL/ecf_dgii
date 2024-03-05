using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemOtraMonedaDetalle", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemOtraMonedaDetalle
{
    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 20.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 4.</para>
    ///     <para xml:lang="en">Pattern: (\d{1,16})(\.\d{1,4})?.</para>
    /// </summary>
    [RegularExpression("(\\d{1,16})(\\.\\d{1,4})?")]
    [XmlElement("PrecioOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal PrecioOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the PrecioOtraMoneda property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool PrecioOtraMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("DescuentoOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal DescuentoOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the DescuentoOtraMoneda property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool DescuentoOtraMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("RecargoOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal RecargoOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the RecargoOtraMoneda property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool RecargoOtraMonedaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoItemOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoItemOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoItemOtraMoneda property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoItemOtraMonedaSpecified { get; set; }
}