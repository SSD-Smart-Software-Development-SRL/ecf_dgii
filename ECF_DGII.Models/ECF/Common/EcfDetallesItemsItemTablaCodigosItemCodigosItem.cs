using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemTablaCodigosItemCodigosItem", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaCodigosItemCodigosItem
{
    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 14.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(14)]
    [Required]
    [XmlElement("TipoCodigo", Form = XmlSchemaForm.Unqualified)]
    public string TipoCodigo { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Minimum length: 1.</para>
    ///     <para xml:lang="en">Maximum length: 35.</para>
    /// </summary>
    [MinLength(1)]
    [MaxLength(35)]
    [Required]
    [XmlElement("CodigoItem", Form = XmlSchemaForm.Unqualified)]
    public string CodigoItem { get; set; }
}