using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._34;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoComprador", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoComprador
{
    /// <summary>
    ///     <para xml:lang="en">Pattern: [0-9]{11}|[0-9]{9}.</para>
    /// </summary>
    [RegularExpression("[0-9]{11}|[0-9]{9}")]
    [XmlElement("RNCComprador", Form = XmlSchemaForm.Unqualified)]
    public string RncComprador { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("IdentificadorExtranjero", Form = XmlSchemaForm.Unqualified)]
    public string IdentificadorExtranjero { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 150.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(150)]
    [XmlElement("RazonSocialComprador", Form = XmlSchemaForm.Unqualified)]
    public string RazonSocialComprador { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 80.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(80)]
    [XmlElement("ContactoComprador", Form = XmlSchemaForm.Unqualified)]
    public string ContactoComprador { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 80.</para>
    ///     <para xml:lang="en">Pattern: \w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*.</para>
    /// </summary>
    [MaxLength(80)]
    [RegularExpression("\\w+([-+.]\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*")]
    [XmlElement("CorreoComprador", Form = XmlSchemaForm.Unqualified)]
    public string CorreoComprador { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 100.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(100)]
    [XmlElement("DireccionComprador", Form = XmlSchemaForm.Unqualified)]
    public string DireccionComprador { get; set; }

    [XmlElement("MunicipioComprador", Form = XmlSchemaForm.Unqualified)]
    public ProvinciaMunicipioType MunicipioComprador { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MunicipioComprador property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MunicipioCompradorSpecified { get; set; }

    [XmlElement("ProvinciaComprador", Form = XmlSchemaForm.Unqualified)]
    public ProvinciaMunicipioType ProvinciaComprador { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the ProvinciaComprador property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool ProvinciaCompradorSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaEntrega", Form = XmlSchemaForm.Unqualified)]
    public string FechaEntrega { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 100.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(100)]
    [XmlElement("ContactoEntrega", Form = XmlSchemaForm.Unqualified)]
    public string ContactoEntrega { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 100.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(100)]
    [XmlElement("DireccionEntrega", Form = XmlSchemaForm.Unqualified)]
    public string DireccionEntrega { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 12.</para>
    ///     <para xml:lang="en">Pattern: \d{3}-\d{3}-\d{4}.</para>
    /// </summary>
    [MaxLength(12)]
    [RegularExpression("\\d{3}-\\d{3}-\\d{4}")]
    [XmlElement("TelefonoAdicional", Form = XmlSchemaForm.Unqualified)]
    public string TelefonoAdicional { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaOrdenCompra", Form = XmlSchemaForm.Unqualified)]
    public string FechaOrdenCompra { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("NumeroOrdenCompra", Form = XmlSchemaForm.Unqualified)]
    public string NumeroOrdenCompra { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("CodigoInternoComprador", Form = XmlSchemaForm.Unqualified)]
    public string CodigoInternoComprador { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    ///     <para xml:lang="en">Pattern: ^[a-zA-ZñÑáéíóúÁÉÍÓÚ,\s]*$.</para>
    /// </summary>
    [MaxLength(20)]
    [RegularExpression("^[a-zA-ZñÑáéíóúÁÉÍÓÚ,\\s]*$")]
    [XmlElement("ResponsablePago", Form = XmlSchemaForm.Unqualified)]
    public string ResponsablePago { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 150.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(150)]
    [XmlElement("InformacionAdicionalComprador", Form = XmlSchemaForm.Unqualified)]
    public string InformacionAdicionalComprador { get; set; }
}