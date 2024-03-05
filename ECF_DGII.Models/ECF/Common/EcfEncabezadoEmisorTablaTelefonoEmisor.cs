using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfEncabezadoEmisorTablaTelefonoEmisor", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfEncabezadoEmisorTablaTelefonoEmisor
{
    [XmlIgnore] private Collection<string> _telefonoEmisor;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfEncabezadoEmisorTablaTelefonoEmisor" /> class.</para>
    /// </summary>
    public EcfEncabezadoEmisorTablaTelefonoEmisor()
    {
        _telefonoEmisor = new Collection<string>();
    }

    /// <summary>
    ///     <para xml:lang="en">Maximum length: 12.</para>
    ///     <para xml:lang="en">Pattern: \d{3}-\d{3}-\d{4}.</para>
    /// </summary>
    [MaxLength(12)]
    [RegularExpression("\\d{3}-\\d{3}-\\d{4}")]
    [Required]
    [XmlElement("TelefonoEmisor", Form = XmlSchemaForm.Unqualified)]
    public Collection<string> TelefonoEmisor
    {
        get => _telefonoEmisor;
        private set => _telefonoEmisor = value;
    }
}