using System.CodeDom.Compiler;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;
using ECF_DGII.Models.ECF._47;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfPaginacion", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfPaginacion
{
    [XmlIgnore] private Collection<EcfPaginacionPagina> _pagina;

    /// <summary>
    ///     <para xml:lang="en">Initializes a new instance of the <see cref="EcfPaginacion" /> class.</para>
    /// </summary>
    public EcfPaginacion()
    {
        _pagina = new Collection<EcfPaginacionPagina>();
    }

    [Required]
    [XmlElement("Pagina", Form = XmlSchemaForm.Unqualified)]
    public Collection<EcfPaginacionPagina> Pagina
    {
        get => _pagina;
        private set => _pagina = value;
    }
}