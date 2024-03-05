using System.CodeDom.Compiler;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics;
using System.Xml.Schema;
using System.Xml.Serialization;

namespace ECF_DGII.Models.ECF.Common;

[GeneratedCode("XmlSchemaClassGenerator", "2.1.1094.0")]
[Serializable]
[XmlType("EcfDetallesItemsItemTablaImpuestoAdicionalImpuestoAdicional", Namespace = "", AnonymousType = true)]
[DebuggerStepThrough]
[DesignerCategory("code")]
public class EcfDetallesItemsItemTablaImpuestoAdicionalImpuestoAdicional
{
    [Required]
    [XmlElement("TipoImpuesto", Form = XmlSchemaForm.Unqualified)]
    public CodificacionTipoImpuestosType TipoImpuesto { get; set; }
}