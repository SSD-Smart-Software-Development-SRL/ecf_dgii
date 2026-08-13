using EcfDgii.Client.Generated.Models;

namespace EcfDgii.Client
{
    /// <summary>
    /// Public interface to unify Kiota-generated ECF models.
    /// </summary>
    public interface IEcfDocument
    {
        TipoeCFType? TipoeCF { get; }
        string? RncEmisor { get; }
        string? Encf { get; }
    }
}
