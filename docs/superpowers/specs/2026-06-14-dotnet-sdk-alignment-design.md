# Design Spec: .NET SDK Alignment with TypeScript SDK

**Date:** 2026-06-14  
**Status:** Draft  
**Topic:** Aligning the .NET ECF DGII SDK with the TypeScript reference implementation.

## 1. Purpose
The current .NET SDK is missing several high-level features present in the TypeScript SDK (the "source of truth"). This alignment ensures a consistent developer experience (DX) across platforms while following .NET best practices (Strong typing, Dependency Injection, `IDistributedCache`).

## 2. Architecture & Core Interfaces

### 2.1. Unified Document Interface (`IEcfDocument`)
To support a generic `SendEcfAsync<T>` method, we will introduce an internal interface using `partial classes` for the Kiota-generated models.

```csharp
internal interface IEcfDocument
{
    string? TipoeCF { get; }
    string? RncEmisor { get; }
    string? Encf { get; }
}
```

Each generated model (e.g., `Ecf31ECF`) will implement this interface in a separate `ModelsExtensions.cs` file.

### 2.2. Dependency Injection
The SDK will provide extension methods for `IServiceCollection` to facilitate integration:
- `AddEcfClient(options)`
- `AddEcfFrontendClient(options)`

## 3. EcfClient & Polling Logic

### 3.1. Generic Send Method
Instead of 10 separate methods, `EcfClient` will expose:
```csharp
public async Task<EcfResponse> SendEcfAsync<T>(T ecf, PollingOptions? options = null, CancellationToken ct = default) where T : IEcfDocument;
```
It will internally route to the correct Kiota endpoint based on `TipoeCF`.

### 3.2. Polling Alignment
- Terminal states: `Finished`, `Error`.
- Throws `EcfException` on `Error`, containing the full `EcfResponse`.
- Uses exponential backoff (defaulting to TS values).

### 3.3. Missing Methods
Implement 1:1 parity with TS for:
- `FirmarSemillaAsync`
- `AnulacionRangosAsync`
- `ConsultaDirectorioAsync`
- `SearchEcfReceptionRequestsAsync`
- `AprobacionComercialAsync` (ACECF)

## 4. EcfFrontendClient & IDistributedCache

### 4.1. Token Management
- Replaces custom AES file cache with `Microsoft.Extensions.Caching.Abstractions.IDistributedCache`.
- Agnostic to the underlying provider (Redis, Memory, etc.).

### 4.2. Transparent Auto-Refresh
- Implemented via `DelegatingHandler`.
- Intercepts `401 Unauthorized`.
- Calls user-provided `GetTokenAsync` callback.
- Updates cache and retries the request once.

### 4.3. Read-Only Enforcement
- Only exposes `GET` methods.
- Does not expose the raw Kiota `Api` property to prevent accidental mutations.

## 5. Success Criteria
- All 31 methods from `EcfClient` (TS) have a .NET equivalent.
- All 6 methods from `EcfFrontendClient` (TS) have a .NET equivalent.
- Unit tests verify the generic routing and polling logic.
- Integration with ASP.NET Core is seamless via `IServiceCollection`.
