using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._32;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemMineria", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemMineria
{
    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 19.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 3.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(.[0-9]{1,3})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(.[0-9]{1,3})?")]
    [XmlElement("PesoNetoKilogramo", Form = XmlSchemaForm.Unqualified)]
    public decimal PesoNetoKilogramo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the PesoNetoKilogramo property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool PesoNetoKilogramoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 19.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 3.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(.[0-9]{1,3})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(.[0-9]{1,3})?")]
    [XmlElement("PesoNetoMineria", Form = XmlSchemaForm.Unqualified)]
    public decimal PesoNetoMineria { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the PesoNetoMineria property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool PesoNetoMineriaSpecified { get; set; }

    [XmlElement("TipoAfiliacion", Form = XmlSchemaForm.Unqualified)]
    public TipoAfiliacionType TipoAfiliacion { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TipoAfiliacion property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TipoAfiliacionSpecified { get; set; }

    [XmlElement("Liquidacion", Form = XmlSchemaForm.Unqualified)]
    public LiquidacionType Liquidacion { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the Liquidacion property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool LiquidacionSpecified { get; set; }
}