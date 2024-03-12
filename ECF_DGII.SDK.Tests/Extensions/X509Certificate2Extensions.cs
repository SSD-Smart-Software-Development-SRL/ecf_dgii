using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using Microsoft.Extensions.Configuration;

namespace ECF_DGII.SDK.Tests.Extensions;

internal static class X509Certificate2Extensions
{
    private const string RSA = "1.2.840.113549.1.1.1";
    private const string DSA = "1.2.840.10040.4.1";
    private const string ECC = "1.2.840.10045.2.1";
    private const string ECDH = "1.2.840.10045.2.1.1";

    public static X509Certificate2 ReadCertificateFromBase64(
        this IConfiguration config,
        string base64CertificateKey = "Base64Certificate",
        string passwordKey = "CertificatePassword")
    {
        var base64Certificate = config[base64CertificateKey];
        var password = config[passwordKey];
        if (string.IsNullOrWhiteSpace(base64Certificate))
            throw new InvalidOperationException($"{base64CertificateKey} configuration is null, empty or whitespace. Cannot read the certificate.");

        var certBytes = Convert.FromBase64String(base64Certificate);
        var certificate = new X509Certificate2(certBytes, password, X509KeyStorageFlags.Exportable);
        return certificate;
    }

    public static AsymmetricAlgorithm GetPrivateKey(this X509Certificate2 certificate)
    {
        ArgumentNullException.ThrowIfNull(certificate);
        var privateKey = certificate.PublicKey.Oid.Value switch
        {
            RSA => certificate.GetRSAPrivateKey() as AsymmetricAlgorithm,
            DSA => certificate.GetDSAPrivateKey(),
            ECC => certificate.GetECDsaPrivateKey(),
            ECDH => certificate.GetECDiffieHellmanPrivateKey(),
            _ => throw new Exception($"Cannot retrieve the certificate private key for the not supported public key OID: `{certificate.PublicKey.Oid.Value}`.")
        } ?? throw new Exception("Error retrieving the private key. The private key is null.");

        return privateKey;
    }
}