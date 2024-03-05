using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF.Common;

namespace ECF_DGII.Models.ECF._41;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemRetencion", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemRetencion
{
    [Required]
    [XmlElement("IndicadorAgenteRetencionoPercepcion", Form = XmlSchemaForm.Unqualified)]
    public IndicadorAgenteRetencionoPercepcionType IndicadorAgenteRetencionoPercepcion { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoITBISRetenido", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoItbisRetenido { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoItbisRetenido property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoItbisRetenidoSpecified { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Total number of digits: 18.</para>
    ///     <para xml:lang="en">Total number of digits in fraction: 2.</para>
    ///     <para xml:lang="en">Pattern: [0-9]{1,16}(\.[0-9]{1,2})?.</para>
    /// </summary>
    [RegularExpression("[0-9]{1,16}(\\.[0-9]{1,2})?")]
    [XmlElement("MontoISRRetenido", Form = XmlSchemaForm.Unqualified)]
    public decimal MontoIsrRetenido { get; set; }

    /// <summary>
    ///     <para xml:lang="en">Gets or sets a value indicating whether the MontoIsrRetenido property is specified.</para>
    /// </summary>
    [XmlIgnore]
    public bool MontoIsrRetenidoSpecified { get; set; }
}