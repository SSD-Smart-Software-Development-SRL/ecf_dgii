# .NET SDK Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align the .NET SDK with the TypeScript SDK (1:1 parity) using .NET best practices like `IDistributedCache`, Dependency Injection, and generic routing.

**Architecture:** 
- Use `partial classes` to implement a common `IEcfDocument` interface on Kiota-generated models.
- Refactor `EcfClient` to use a generic `SendEcfAsync<T>` method with internal routing.
- Refactor `EcfFrontendClient` to use `IDistributedCache` and a `DelegatingHandler` for transparent token refresh.
- Add missing methods to reach 1:1 parity with the TS SDK.

**Tech Stack:** .NET (Standard 2.0+), Kiota, Microsoft.Extensions.Caching.Abstractions, Microsoft.Extensions.DependencyInjection.Abstractions.

---

### Task 1: Project Dependencies & Core Interfaces

**Files:**
- Modify: `.net/EcfDgii.Client/EcfDgii.Client.csproj`
- Create: `.net/EcfDgii.Client/IEcfDocument.cs`
- Create: `.net/EcfDgii.Client/Generated/Models/ModelsExtensions.cs`

- [ ] **Step 1: Add required NuGet packages**
Add `Microsoft.Extensions.Caching.Abstractions` and `Microsoft.Extensions.DependencyInjection.Abstractions`.

- [ ] **Step 2: Define IEcfDocument interface**
```csharp
namespace EcfDgii.Client
{
    internal interface IEcfDocument
    {
        string? TipoeCF { get; }
        string? RncEmisor { get; }
        string? Encf { get; }
    }
}
```

- [ ] **Step 3: Implement IEcfDocument in partial classes**
Create `ModelsExtensions.cs` and implement the interface for all 10 ECF types (31, 32, 33, 34, 41, 43, 44, 45, 46, 47).
Example for 31:
```csharp
namespace EcfDgii.Client.Generated.Models
{
    public partial class Ecf31ECF : IEcfDocument
    {
        string? IEcfDocument.TipoeCF => Encabezado?.IdDoc?.TipoeCF;
        string? IEcfDocument.RncEmisor => Encabezado?.Emisor?.RncEmisor;
        string? IEcfDocument.Encf => Encabezado?.IdDoc?.Encf;
    }
}
```

- [ ] **Step 4: Commit**
```bash
git add .net/EcfDgii.Client/EcfDgii.Client.csproj .net/EcfDgii.Client/IEcfDocument.cs .net/EcfDgii.Client/Generated/Models/ModelsExtensions.cs
git commit -m "feat: add IEcfDocument and implement in partial classes"
```

---

### Task 2: EcfClient Refactor (Generic Send & Routing)

**Files:**
- Modify: `.net/EcfDgii.Client/EcfClient.cs`

- [ ] **Step 1: Implement generic SendEcfAsync<T>**
Replace the 10 overloads with a single generic method and a routing dictionary.
```csharp
private readonly Dictionary<string, string> _routeMap = new Dictionary<string, string>
{
    ["FacturaDeCreditoFiscalElectronica"] = "31",
    // ... add all 10
};

public async Task<EcfResponse> SendEcfAsync<T>(T ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default) where T : IEcfDocument
{
    var doc = (IEcfDocument)ecf;
    var tipoeCF = doc.TipoeCF;
    if (string.IsNullOrEmpty(tipoeCF) || !_routeMap.TryGetValue(tipoeCF, out var route))
        throw new ArgumentException($"Unknown or missing TipoeCF: {tipoeCF}");

    return await SendInternalAsync(
        doc.RncEmisor,
        doc.Encf,
        ct => PostToRouteAsync(route, ecf, ct),
        pollingOptions,
        cancellationToken);
}

private Task<EcfResponse?> PostToRouteAsync<T>(string route, T body, CancellationToken ct)
{
    return route switch
    {
        "31" => Api.Ecf.ThreeOne.PostAsync((Ecf31ECF)(object)body, cancellationToken: ct),
        // ... switch for all 10
        _ => throw new NotSupportedException()
    };
}
```

- [ ] **Step 2: Commit**
```bash
git add .net/EcfDgii.Client/EcfClient.cs
git commit -m "refactor: implement generic SendEcfAsync with internal routing"
```

---

### Task 3: EcfClient Parity (Missing Methods)

**Files:**
- Modify: `.net/EcfDgii.Client/EcfClient.cs`

- [ ] **Step 1: Add missing methods from TS SDK**
Implement:
- `GetCompaniesAsync(params)`
- `UpsertCompanyAsync(body)`
- `DeleteCompanyAsync(rnc)`
- `GetCertificateAsync(rnc)`
- `UpdateCertificateAsync(rnc, certificate, password)`
- `FirmarSemillaAsync(rnc, xml)`
- `AnulacionRangosAsync(rnc, body)`
- `ListAnulacionesAsync(params)`
- `SearchEcfReceptionRequestsAsync(params)`
- `AprobacionComercialAsync(messageId, body)`
- `ConsultaDirectorioListadoAsync(rnc)`
- `EstatusServiciosAsync(rnc)`
- `CreateApiKeyAsync(body)`

- [ ] **Step 2: Commit**
```bash
git add .net/EcfDgii.Client/EcfClient.cs
git commit -m "feat: add missing methods to EcfClient for TS parity"
```

---

### Task 4: EcfFrontendClient Refactor (IDistributedCache)

**Files:**
- Modify: `.net/EcfDgii.Client/EcfFrontendClient.cs`
- Create: `.net/EcfDgii.Client/TokenAuthHandler.cs`

- [ ] **Step 1: Update EcfFrontendClientOptions**
Replace `CacheToken` and `GetCachedToken` callbacks with `IDistributedCache`.

- [ ] **Step 2: Implement TokenAuthHandler**
Create a `DelegatingHandler` that handles 401 retries and token caching using `IDistributedCache`.

- [ ] **Step 3: Update EcfFrontendClient**
Expose only GET methods and use the new `TokenAuthHandler`.

- [ ] **Step 4: Commit**
```bash
git add .net/EcfDgii.Client/EcfFrontendClient.cs .net/EcfDgii.Client/TokenAuthHandler.cs
git commit -m "refactor: use IDistributedCache and TokenAuthHandler in EcfFrontendClient"
```

---

### Task 5: Dependency Injection Extensions

**Files:**
- Create: `.net/EcfDgii.Client/ServiceCollectionExtensions.cs`

- [ ] **Step 1: Implement AddEcfClient and AddEcfFrontendClient**
Add extension methods for `IServiceCollection` to register the clients.

- [ ] **Step 2: Commit**
```bash
git add .net/EcfDgii.Client/ServiceCollectionExtensions.cs
git commit -m "feat: add IServiceCollection extensions for easy DI integration"
```

---

### Task 6: Verification & Tests

**Files:**
- Create: `.net/EcfDgii.Client.Tests/ClientAlignmentTests.cs`

- [ ] **Step 1: Write unit tests for generic routing**
Verify that `SendEcfAsync` routes to the correct internal Kiota call.

- [ ] **Step 2: Verify all methods exist**
Reflection-based test to ensure parity with TS method names (mapped to PascalCase).

- [ ] **Step 3: Commit**
```bash
git add .net/EcfDgii.Client.Tests/ClientAlignmentTests.cs
git commit -m "test: verify SDK alignment and generic routing"
```
