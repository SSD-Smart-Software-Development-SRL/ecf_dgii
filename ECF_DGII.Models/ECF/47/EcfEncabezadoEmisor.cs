using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._47;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoEmisor", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoEmisor
{
    [XmlIgnore] private Collection<string> _tablaTelefonoEmisor;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfEncabezadoEmisor" /> class.</para>
    /// </summary>
    public EcfEncabezadoEmisor()
    {
        _tablaTelefonoEmisor = new Collection<string>();
    }

    /// <summary>
    ///     <para xml:lang="en">Pattern: [0-9]{11}|[0-9]{9}.</para>
    /// </summary>
    [RegularExpression("[0-9]{11}|[0-9]{9}")]
    [Required]
    [XmlElement("RNCEmisor", Form = XmlSchemaForm.Unqualified)]
    public string RncEmisor { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 150.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(150)]
    [Required]
    [XmlElement("RazonSocialEmisor", Form = XmlSchemaForm.Unqualified)]
    public string RazonSocialEmisor { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 150.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(150)]
    [XmlElement("NombreComercial", Form = XmlSchemaForm.Unqualified)]
    public string NombreComercial { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("Sucursal", Form = XmlSchemaForm.Unqualified)]
    public string Sucursal { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 100.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(100)]
    [Required]
    [XmlElement("DireccionEmisor", Form = XmlSchemaForm.Unqualified)]
    public string DireccionEmisor { get; set; }

    [XmlElement("Municipio", Form = XmlSchemaForm.Unqualified)]
    public ProvinciaMunicipioType Municipio { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the Municipio property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MunicipioSpecified { get; set; }

    [XmlElement("Provincia", Form = XmlSchemaForm.Unqualified)]
    public ProvinciaMunicipioType Provincia { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the Provincia property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool ProvinciaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 12.</para>
    ///     <para xml:lang="en">Pattern: \d{3}-\d{3}-\d{4}.</para>
    /// </summary>
    [MaxLength(12)]
    [RegularExpression("\\d{3}-\\d{3}-\\d{4}")]
    [XmlArray("TablaTelefonoEmisor", Form = XmlSchemaForm.Unqualified)]
    [XmlArrayItem("TelefonoEmisor", Form = XmlSchemaForm.Unqualified)]
    public Collection<string> TablaTelefonoEmisor
    {
        get => _tablaTelefonoEmisor;
        private set => _tablaTelefonoEmisor = value;
    }

    /// <summary>
    ///     <para xml:lang="en">Gets a value indicating whether the TablaTelefonoEmisor collection is empty.</para>
    /// </summary>
    [XmlIgnore]
    public bool TablaTelefonoEmisorSpecified => TablaTelefonoEmisor.Count != 0;

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 80.</para>
    ///     <para xml:lang="en">Pattern: \w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*.</para>
    /// </summary>
    [MaxLength(80)]
    [RegularExpression("\\w+([-+.]\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*")]
    [XmlElement("CorreoEmisor", Form = XmlSchemaForm.Unqualified)]
    public string CorreoEmisor { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 50.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(50)]
    [XmlElement("WebSite", Form = XmlSchemaForm.Unqualified)]
    public string WebSite { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 100.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(100)]
    [XmlElement("ActividadEconomica", Form = XmlSchemaForm.Unqualified)]
    public string ActividadEconomica { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("NumeroFacturaInterna", Form = XmlSchemaForm.Unqualified)]
    public string NumeroFacturaInterna { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 20.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,20}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,20}")]
    [XmlElement("NumeroPedidoInterno", Form = XmlSchemaForm.Unqualified)]
    public decimal NumeroPedidoInterno { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the NumeroPedidoInterno property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool NumeroPedidoInternoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 250.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(250)]
    [XmlElement("InformacionAdicionalEmisor", Form = XmlSchemaForm.Unqualified)]
    public string InformacionAdicionalEmisor { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [Required]
    [XmlElement("FechaEmision", Form = XmlSchemaForm.Unqualified)]
    public string FechaEmision { get; set; }
}