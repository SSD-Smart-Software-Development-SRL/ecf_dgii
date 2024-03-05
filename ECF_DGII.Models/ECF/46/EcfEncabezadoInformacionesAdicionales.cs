using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._46;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoInformacionesAdicionales", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoInformacionesAdicionales
{
    /// <summary>
    ///     <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((19|20)\d{2}).</para>
    /// </summary>
    [RegularExpression("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((19|20)\\d{2})")]
    [XmlElement("FechaEmbarque", Form = XmlSchemaForm.Unqualified)]
    public string FechaEmbarque { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 25.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(25)]
    [XmlElement("NumeroEmbarque", Form = XmlSchemaForm.Unqualified)]
    public string NumeroEmbarque { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 100.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(100)]
    [XmlElement("NumeroContenedor", Form = XmlSchemaForm.Unqualified)]
    public string NumeroContenedor { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 20.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,20}.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,20}")]
    [XmlElement("NumeroReferencia", Form = XmlSchemaForm.Unqualified)]
    public decimal NumeroReferencia { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the NumeroReferencia property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool NumeroReferenciaSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 40.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(40)]
    [XmlElement("NombrePuertoEmbarque", Form = XmlSchemaForm.Unqualified)]
    public string NombrePuertoEmbarque { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 3.</para>
    ///     <para xml:lang="en">Pattern: \D[^0-9]+[a-zA-ZñÑáéíóúÁÉÍÓÚ].</para>
    /// </summary>
    [MaxLength(3)]
    [RegularExpression("\\D[^0-9]+[a-zA-ZñÑáéíóúÁÉÍÓÚ]")]
    [XmlElement("CondicionesEntrega", Form = XmlSchemaForm.Unqualified)]
    public string CondicionesEntrega { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("TotalFob", Form = XmlSchemaForm.Unqualified)]
    public decimal TotalFob { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TotalFob property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TotalFobSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("Seguro", Form = XmlSchemaForm.Unqualified)]
    public decimal Seguro { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the Seguro property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool SeguroSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("Flete", Form = XmlSchemaForm.Unqualified)]
    public decimal Flete { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the Flete property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool FleteSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("OtrosGastos", Form = XmlSchemaForm.Unqualified)]
    public decimal OtrosGastos { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the OtrosGastos property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool OtrosGastosSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("TotalCif", Form = XmlSchemaForm.Unqualified)]
    public decimal TotalCif { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the TotalCif property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool TotalCifSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 35.</para>
    ///     <para xml:lang="en">Pattern: (\D[^0-9]+[a-zA-ZñÑáéíóúÁÉÍÓÚ]).</para>
    /// </summary>
    [MaxLength(35)]
    [RegularExpression("(\\D[^0-9]+[a-zA-ZñÑáéíóúÁÉÍÓÚ])")]
    [XmlElement("RegimenAduanero", Form = XmlSchemaForm.Unqualified)]
    public string RegimenAduanero { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 40.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(40)]
    [XmlElement("NombrePuertoSalida", Form = XmlSchemaForm.Unqualified)]
    public string NombrePuertoSalida { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 40.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(40)]
    [XmlElement("NombrePuertoDesembarque", Form = XmlSchemaForm.Unqualified)]
    public string NombrePuertoDesembarque { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("PesoBruto", Form = XmlSchemaForm.Unqualified)]
    public decimal PesoBruto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the PesoBruto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool PesoBrutoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("PesoNeto", Form = XmlSchemaForm.Unqualified)]
    public decimal PesoNeto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the PesoNeto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool PesoNetoSpecified { get; set; }

    [XmlElement("UnidadPesoBruto", Form = XmlSchemaForm.Unqualified)]
    public UnidadMedidaType UnidadPesoBruto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the UnidadPesoBruto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool UnidadPesoBrutoSpecified { get; set; }

    [XmlElement("UnidadPesoNeto", Form = XmlSchemaForm.Unqualified)]
    public UnidadMedidaType UnidadPesoNeto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the UnidadPesoNeto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool UnidadPesoNetoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("CantidadBulto", Form = XmlSchemaForm.Unqualified)]
    public decimal CantidadBulto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the CantidadBulto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool CantidadBultoSpecified { get; set; }

    [XmlElement("UnidadBulto", Form = XmlSchemaForm.Unqualified)]
    public UnidadMedidaType UnidadBulto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the UnidadBulto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool UnidadBultoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum exclusive value: 0.</para>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("VolumenBulto", Form = XmlSchemaForm.Unqualified)]
    public decimal VolumenBulto { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the VolumenBulto property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool VolumenBultoSpecified { get; set; }

    [XmlElement("UnidadVolumen", Form = XmlSchemaForm.Unqualified)]
    public UnidadMedidaType UnidadVolumen { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the UnidadVolumen property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool UnidadVolumenSpecified { get; set; }
}