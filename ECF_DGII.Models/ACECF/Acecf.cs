namespace ECF_DGII.Models.ACECF;

[System.CodeDom.Compiler.GeneratedCodeAttribute("XmlSchemaClassGenerator", "2.1.1094.0")]
[System.SerializableAttribute()]
[System.Xml.Serialization.XmlTypeAttribute("versionType", Namespace = "")]
public enum VersionType
{

    [System.Xml.Serialization.XmlEnumAttribute("1.0")]
    Item10,
}

[System.CodeDom.Compiler.GeneratedCodeAttribute("XmlSchemaClassGenerator", "2.1.1094.0")]
[System.SerializableAttribute()]
[System.Xml.Serialization.XmlTypeAttribute("EstadoRechazoType", Namespace = "")]
public enum EstadoRechazoType
{

    [System.Xml.Serialization.XmlEnumAttribute("0")]
    Item0,

    [System.Xml.Serialization.XmlEnumAttribute("1")]
    Item1,

    [System.Xml.Serialization.XmlEnumAttribute("2")]
    Item2,

    [System.Xml.Serialization.XmlEnumAttribute("3")]
    Item3,

    [System.Xml.Serialization.XmlEnumAttribute("4")]
    Item4,
}

[System.CodeDom.Compiler.GeneratedCodeAttribute("XmlSchemaClassGenerator", "2.1.1094.0")]
[System.SerializableAttribute()]
[System.Xml.Serialization.XmlTypeAttribute("EstadoType", Namespace = "")]
public enum EstadoType
{

    [System.Xml.Serialization.XmlEnumAttribute("1")]
    Item1,

    [System.Xml.Serialization.XmlEnumAttribute("2")]
    Item2,
}

[System.CodeDom.Compiler.GeneratedCodeAttribute("XmlSchemaClassGenerator", "2.1.1094.0")]
[System.SerializableAttribute()]
[System.Xml.Serialization.XmlTypeAttribute("ACECF", Namespace = "", AnonymousType = true)]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlRootAttribute("ACECF", Namespace = "")]
public partial class Acecf
{

    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("DetalleAprobacionComercial", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public AcecfDetalleAprobacionComercial DetalleAprobacionComercial { get; set; }

    [System.Xml.Serialization.XmlAnyElementAttribute()]
    public System.Xml.XmlElement Any { get; set; }
}

[System.CodeDom.Compiler.GeneratedCodeAttribute("XmlSchemaClassGenerator", "2.1.1094.0")]
[System.SerializableAttribute()]
[System.Xml.Serialization.XmlTypeAttribute("AcecfDetalleAprobacionComercial", Namespace = "", AnonymousType = true)]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
public partial class AcecfDetalleAprobacionComercial
{

    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("Version", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public VersionType Version { get; set; }

    /// <summary>
    /// <para xml:lang="en">Pattern: (\d{11,11})|(\d{9,9}).</para>
    /// </summary>
    [System.ComponentModel.DataAnnotations.RegularExpressionAttribute("(\\d{11,11})|(\\d{9,9})")]
    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("RNCEmisor", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public string RncEmisor { get; set; }

    /// <summary>
    /// <para xml:lang="en">Pattern: ([a-z0-9A-Z]{13,13})|([a-z0-9A-Z]{11,11})|([a-z0-9A-Z]{9,9}).</para>
    /// </summary>
    [System.ComponentModel.DataAnnotations.RegularExpressionAttribute("([a-z0-9A-Z]{13,13})|([a-z0-9A-Z]{11,11})|([a-z0-9A-Z]{9,9})")]
    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("eNCF", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public string Encf { get; set; }

    /// <summary>
    /// <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0?[1-9])\-(1[012]|0?[1-9])\-((?:20|20)\d{2}).</para>
    /// </summary>
    [System.ComponentModel.DataAnnotations.RegularExpressionAttribute("(3[01]|[12][0-9]|0?[1-9])\\-(1[012]|0?[1-9])\\-((?:20|20)\\d{2})")]
    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("FechaEmision", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public string FechaEmision { get; set; }

    /// <summary>
    /// <para xml:lang="en">Total number of digits: 18.</para>
    /// <para xml:lang="en">Total number of digits in fraction: 2.</para>
    /// <para xml:lang="en">Pattern: [0-9]+(\.[0-9]{2}).</para>
    /// </summary>
    [System.ComponentModel.DataAnnotations.RegularExpressionAttribute("[0-9]+(\\.[0-9]{2})")]
    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("MontoTotal", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public decimal MontoTotal { get; set; }

    /// <summary>
    /// <para xml:lang="en">Pattern: (\d{11,11})|(\d{9,9}).</para>
    /// </summary>
    [System.ComponentModel.DataAnnotations.RegularExpressionAttribute("(\\d{11,11})|(\\d{9,9})")]
    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("RNCComprador", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public string RncComprador { get; set; }

    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("Estado", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public EstadoType Estado { get; set; }

    /// <summary>
    /// <para xml:lang="en">Maximum length: 250.</para>
    /// </summary>
    [System.ComponentModel.DataAnnotations.MaxLengthAttribute(250)]
    [System.Xml.Serialization.XmlElementAttribute("DetalleMotivoRechazo", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public string DetalleMotivoRechazo { get; set; }

    /// <summary>
    /// <para xml:lang="en">Pattern: (3[01]|[12][0-9]|0[1-9])-(1[0-2]|0[1-9])-[0-9]{4} (2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9]).</para>
    /// </summary>
    [System.ComponentModel.DataAnnotations.RegularExpressionAttribute("(3[01]|[12][0-9]|0[1-9])-(1[0-2]|0[1-9])-[0-9]{4} (2[0-3]|[01]?[0-9]):([0-5]?[0-9" +
        "]):([0-5]?[0-9])")]
    [System.ComponentModel.DataAnnotations.RequiredAttribute()]
    [System.Xml.Serialization.XmlElementAttribute("FechaHoraAprobacionComercial", Form = System.Xml.Schema.XmlSchemaForm.Unqualified)]
    public string FechaHoraAprobacionComercial { get; set; }
}
