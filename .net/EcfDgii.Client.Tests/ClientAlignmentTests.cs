using System;
using System.Linq;
using System.Reflection;
using Xunit;
using EcfDgii.Client;

namespace EcfDgii.Client.Tests
{
    public class ClientAlignmentTests
    {
        [Fact]
        public void EcfClient_ShouldHaveAllMethodsFromTypeScriptSDK()
        {
            var type = typeof(EcfClient);
            var methods = type.GetMethods(BindingFlags.Public | BindingFlags.Instance)
                .Select(m => m.Name)
                .Distinct()
                .ToList();

            string[] expectedMethods = new[]
            {
                "SendEcfAsync",
                "GetCompaniesAsync",
                "GetCompanyByRncAsync",
                "UpsertCompanyAsync",
                "DeleteCompanyAsync",
                "GetCertificateAsync",
                "UpdateCertificateAsync",
                "QueryEcfAsync",
                "SearchEcfsAsync",
                "SearchAllEcfsAsync",
                "GetEcfByIdAsync",
                "AnulacionRangosAsync",
                "ListAnulacionesAsync",
                "FirmarSemillaAsync",
                "SearchEcfReceptionRequestsAsync",
                "SearchAcecfReceptionRequestsAsync",
                "SearchEcfReceptionRequestsByRncAsync",
                "GetEcfReceptionRequestAsync",
                "GetAcecfReceptionRequestAsync",
                "AprobacionComercialAsync",
                "ConsultaDirectorioListadoAsync",
                "ConsultaDirectorioPorRncAsync",
                "ConsultaEstadoAsync",
                "ConsultaResultadoAsync",
                "ConsultaRFCEAsync",
                "ConsultaTimbreAsync",
                "ConsultaTimbreFCAsync",
                "ConsultaTrackIdAsync",
                "EstatusServiciosAsync",
                "VentanasMantenimientoAsync",
                "CreateApiKeyAsync"
            };

            foreach (var expected in expectedMethods)
            {
                Assert.Contains(expected, methods);
            }
        }

        [Fact]
        public void EcfFrontendClient_ShouldHaveAllMethodsFromTypeScriptSDK()
        {
            var type = typeof(EcfFrontendClient);
            var methods = type.GetMethods(BindingFlags.Public | BindingFlags.Instance)
                .Select(m => m.Name)
                .Distinct()
                .ToList();

            string[] expectedMethods = new[]
            {
                "QueryEcfAsync",
                "SearchEcfsAsync",
                "SearchAllEcfsAsync",
                "GetEcfByIdAsync",
                "GetCompaniesAsync",
                "GetCompanyByRncAsync"
            };

            foreach (var expected in expectedMethods)
            {
                Assert.Contains(expected, methods);
            }
        }
    }
}
