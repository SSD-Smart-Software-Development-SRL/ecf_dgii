using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF._46;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoTransporte", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoTransporte
{
    [XmlElement("ViaTransporte", Form = XmlSchemaForm.Unqualified)]
    public ViaTransporteType ViaTransporte { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the ViaTransporte property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool ViaTransporteSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 60.</para>
    ///     <para xml:lang="en">Pattern: (\D[^0-9]+[a-zA-ZñÑáéíóúÁÉÍÓÚ]).</para>
    /// </summary>
    [MaxLength(60)]
    [RegularExpression("(\\D[^0-9]+[a-zA-ZñÑáéíóúÁÉÍÓÚ])")]
    [XmlElement("PaisOrigen", Form = XmlSchemaForm.Unqualified)]
    public string PaisOrigen { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 100.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(100)]
    [XmlElement("DireccionDestino", Form = XmlSchemaForm.Unqualified)]
    public string DireccionDestino { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 60.</para>
    ///     <para xml:lang="en">Pattern: (\D[^0-9]+[a-zA-ZñÑáéíóúÁÉÍÓÚ]).</para>
    /// </summary>
    [MaxLength(60)]
    [RegularExpression("(\\D[^0-9]+[a-zA-ZñÑáéíóúÁÉÍÓÚ])")]
    [XmlElement("PaisDestino", Form = XmlSchemaForm.Unqualified)]
    public string PaisDestino { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("RNCIdentificacionCompaniaTransportista", Form = XmlSchemaForm.Unqualified)]
    public string RncIdentificacionCompaniaTransportista { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 150.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(150)]
    [XmlElement("NombreCompaniaTransportista", Form = XmlSchemaForm.Unqualified)]
    public string NombreCompaniaTransportista { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("NumeroViaje", Form = XmlSchemaForm.Unqualified)]
    public string NumeroViaje { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("Conductor", Form = XmlSchemaForm.Unqualified)]
    public string Conductor { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 20.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,20}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,20}")]
    [XmlElement("DocumentoTransporte", Form = XmlSchemaForm.Unqualified)]
    public decimal DocumentoTransporte { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the DocumentoTransporte property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool DocumentoTransporteSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 10.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(10)]
    [XmlElement("Ficha", Form = XmlSchemaForm.Unqualified)]
    public string Ficha { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 7.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(7)]
    [XmlElement("Placa", Form = XmlSchemaForm.Unqualified)]
    public string Placa { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("RutaTransporte", Form = XmlSchemaForm.Unqualified)]
    public string RutaTransporte { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("ZonaTransporte", Form = XmlSchemaForm.Unqualified)]
    public string ZonaTransporte { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 20.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(20)]
    [XmlElement("NumeroAlbaran", Form = XmlSchemaForm.Unqualified)]
    public string NumeroAlbaran { get; set; }
}