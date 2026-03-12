# @ecfx/sdk

TypeScript SDK for the ECF DGII API (Dominican Republic electronic fiscal receipts).

Built with [openapi-typescript](https://github.com/openapi-ts/openapi-typescript) and [openapi-fetch](https://github.com/openapi-ts/openapi-typescript/tree/main/packages/openapi-fetch) for fully typed API access.

## Installation

```bash
npm install @ecfx/sdk
```

## Quick Start

```typescript
import { EcfClient } from '@ecfx/sdk';

const client = new EcfClient({
  apiKey: 'your-jwt-token',
  environment: 'test', // 'test' | 'cert' | 'prod'
});

// Send an ECF and wait for it to finish processing
const result = await client.sendEcf({
  encabezado: {
    idDoc: {
      tipoeCF: 'FacturaDeConsumoElectronica',
      encf: 'E320000000001',
      // ...
    },
    emisor: {
      rncEmisor: '123456789',
      // ...
    },
    // ...
  },
  // ...
});

console.log(result.progress); // 'Finished'
console.log(result.encf);
```

## Environment Configuration

```typescript
// Using a specific environment
const client = new EcfClient({
  apiKey: 'your-jwt-token',
  environment: 'prod',
});

// Using a custom base URL (overrides environment)
const client = new EcfClient({
  apiKey: 'your-jwt-token',
  baseUrl: 'https://custom-api.example.com',
});
```

### Environment URLs

| Environment | URL |
|-------------|-----|
| `test` | `https://api.test.ecfx.ssd.com.do` |
| `cert` | `https://api.cert.ecfx.ssd.com.do` |
| `prod` | `https://api.prod.ecfx.ssd.com.do` |

## Polling Options

The `sendEcf` method polls until the ECF is processed. You can customize polling behavior:

```typescript
const result = await client.sendEcf(ecf, {
  initialDelay: 1000,      // Start polling after 1s (default)
  maxDelay: 30000,          // Max delay between polls (default)
  maxRetries: 60,           // Max poll attempts (default)
  backoffMultiplier: 2,     // Exponential backoff multiplier (default)
  timeout: 120000,          // Total timeout in ms
  signal: abortController.signal, // AbortSignal for cancellation
});
```

## Backend / Frontend Architecture

In most real-world apps, the backend handles business logic (validation, storage, conversion) and sends the ECF. The frontend gets a read-only token to query status directly:

```typescript
// Backend: your invoice endpoint
const ecfClient = new EcfClient({
  apiKey: process.env.ECF_BACKEND_TOKEN,
  environment: 'prod',
});

app.post('/api/v1/invoices', async (req, res) => {
  // 1. Validate and save your internal invoice
  const invoice = await validateAndSave(req.body);
  // 2. Convert to ECF format
  const ecf = convertToEcf(invoice);
  // 3. Send to ECF SSD
  const { data } = await ecfClient.raw.POST('/ecf/31', { body: ecf });
  await updateInvoice(invoice.id, { messageId: data.messageId });
  res.json({ id: invoice.id, messageId: data.messageId });
});

// Separate endpoint: generate read-only token for frontend
app.get('/api/v1/ecf-token', async (req, res) => {
  const { data } = await ecfClient.createApiKey({ /* scoped to tenant/RNC */ });
  res.json({ token: data.token });
});
```

The frontend stores the token securely, renews it on `401 Unauthorized` or expiry, and queries ECF SSD directly. See the [main README](../README.md#arquitectura-backend--frontend) for the full diagram and React example.

> **`sendEcf`** wraps send + polling into a single call. Ideal for scripts or simple backends without a frontend.

## Raw Client Access

For direct access to all API endpoints with full type safety:

```typescript
// Company operations
const { data } = await client.raw.GET('/company', {
  params: { query: { Page: 1, Limit: 10 } },
});

// Query ECF status
const { data } = await client.raw.GET('/ecf/{rnc}/{encf}', {
  params: { path: { rnc: '123456789', encf: 'E320000000001' } },
});

// DGII operations
const { data } = await client.raw.GET('/dgii/{rnc}/consultaresultado/estado', {
  params: { path: { rnc: '123456789' }, query: { trackId: 'abc123' } },
});
```

## Convenience Methods

```typescript
// Company
await client.getCompanies({ Page: 1, Limit: 10 });
await client.getCompanyByRnc('123456789');
await client.upsertCompany({ /* ... */ });
await client.deleteCompany('123456789');

// Certificates
await client.getCertificate('123456789');

// ECF queries
await client.queryEcf('123456789', 'E320000000001');
await client.searchEcfs('123456789');
await client.searchAllEcfs();
await client.getEcfById('123456789', 'message-uuid');

// Aprobacion comercial
await client.aprobacionComercial('123456789', 'E320000000001', { /* ... */ });

// Anulacion rangos
await client.anulacionRangos('123456789', { /* ... */ });
await client.listAnulaciones();

// Recepcion
await client.searchEcfReceptionRequests();
await client.getEcfReceptionRequest('123456789', 'message-uuid');

// DGII
await client.consultaResultado('123456789', { trackId: 'abc' });
await client.consultaTimbre('123456789', { /* ... */ });
await client.estatusServicios('123456789');

// API Keys
await client.createApiKey({ /* ... */ });
```

## Runtime Compatibility

This SDK uses the standard `fetch` API and works with:

- Node.js 18+
- Deno
- Bun
- Modern browsers
