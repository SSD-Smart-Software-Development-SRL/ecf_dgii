using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._33;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDescuentosORecargosDescuentoORecargo", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDescuentosORecargosDescuentoORecargo
{
    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,2}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,2}")]
    [Required]
    [XmlElement("NumeroLinea", Form = XmlSchemaForm.Unqualified)]
    public sbyte NumeroLinea { get; set; }

    [Required]
    [XmlElement("TipoAjuste", Form = XmlSchemaForm.Unqualified)]
    public TipoAjusteType TipoAjuste { get; set; }

    [XmlElement("IndicadorNorma1007", Form = XmlSchemaForm.Unqualified)]
    public IndicadorNorma1007Type IndicadorNorma1007 { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the IndicadorNorma1007 property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool IndicadorNorma1007Specified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 45.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(45)]
    [XmlElement("DescripcionDescuentooRecargo", Form = XmlSchemaForm.Unqualified)]
    public string DescripcionDescuentooRecargo { get; set; }

    [XmlElement("TipoValor", Form = XmlSchemaForm.Unqualified)]
    public TipoDescuentoRecargoType TipoValor { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TipoValor property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TipoValorSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 5.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,3}(.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,3}(.[0-9]{1,2})?")]
    [XmlElement("ValorDescuentooRecargo", Form = XmlSchemaForm.Unqualified)]
    public decimal ValorDescuentooRecargo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the ValorDescuentooRecargo property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool ValorDescuentooRecargoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoDescuentooRecargo", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoDescuentooRecargo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoDescuentooRecargo property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoDescuentooRecargoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoDescuentooRecargoOtraMoneda", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoDescuentooRecargoOtraMoneda { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the MontoDescuentooRecargoOtraMoneda property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool MontoDescuentooRecargoOtraMonedaSpecified { get; set; }

    [XmlElement("IndicadorFacturacionDescuentooRecargo", Form = XmlSchemaForm.Unqualified)]
    public IndicadorFacturacionDrType IndicadorFacturacionDescuentooRecargo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">
    ///         Gets or sets a value indicating whether the IndicadorFacturacionDescuentooRecargo property is
    ///         specified.
    ///     </para>
    /// </summary>
    [XmlIgnore]
    public bool IndicadorFacturacionDescuentooRecargoSpecified { get; set; }
}