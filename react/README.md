# @ecfx/react

React Query hooks for the ECF DGII API (Dominican Republic electronic fiscal receipts). Built on top of `openapi-react-query` and `openapi-fetch` for fully typed API interactions.

## Installation

```bash
npm install @ecfx/react @tanstack/react-query
```

## Setup

Wrap your application with `QueryClientProvider` and create the ECF client:

```tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { createEcfReactClient } from '@ecfx/react';

const queryClient = new QueryClient();

const { $api } = createEcfReactClient({
  apiKey: 'your-api-key',
  environment: 'test', // 'test' | 'cert' | 'prod'
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <YourApp />
    </QueryClientProvider>
  );
}
```

You can also provide a custom base URL instead of using a preset environment:

```tsx
const { $api } = createEcfReactClient({
  apiKey: 'your-api-key',
  baseUrl: 'https://custom-api.example.com',
});
```

## Usage

### Querying Data

Use the `$api` object to access typed React Query hooks for every endpoint:

```tsx
function Companies() {
  const { data, isLoading, error } = $api.useQuery('get', '/company', {
    params: { query: { Page: 1, Limit: 10 } },
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <ul>
      {data?.data?.map((company) => (
        <li key={company.rnc}>{company.name}</li>
      ))}
    </ul>
  );
}
```

### Searching ECFs

```tsx
function EcfSearch({ rnc }: { rnc: string }) {
  const { data } = $api.useQuery('get', '/ecf/{rnc}', {
    params: { path: { rnc } },
  });

  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
```

### Sending ECFs (Mutations)

```tsx
function SendEcf() {
  const mutation = $api.useMutation('post', '/ecf/32');

  const handleSend = () => {
    mutation.mutate({
      body: {
        // Your ECF payload here
      },
    });
  };

  return (
    <div>
      <button onClick={handleSend} disabled={mutation.isPending}>
        {mutation.isPending ? 'Sending...' : 'Send ECF'}
      </button>
      {mutation.isSuccess && <p>ECF sent successfully!</p>}
      {mutation.isError && <p>Error: {mutation.error.message}</p>}
    </div>
  );
}
```

## Environments

| Environment | URL |
|-------------|-----|
| `test` | `https://api.test.ecfx.ssd.com.do` |
| `cert` | `https://api.cert.ecfx.ssd.com.do` |
| `prod` | `https://api.prod.ecfx.ssd.com.do` |

## API Reference

### `createEcfReactClient(config)`

Creates a typed React Query client for the ECF DGII API.

**Config options:**

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| `apiKey` | `string` | Yes | Your API key for authentication |
| `environment` | `'test' \| 'cert' \| 'prod'` | No | Target environment (default: `'test'`) |
| `baseUrl` | `string` | No | Custom base URL (overrides `environment`) |

**Returns:** `{ $api, fetchClient }`

- `$api` - The openapi-react-query client with `useQuery`, `useMutation`, `useSuspenseQuery`, etc.
- `fetchClient` - The underlying openapi-fetch client for non-React usage.

## Backend / Frontend Architecture

The React SDK is designed for the **frontend** side of the recommended architecture:

1. Your **backend** sends the e-CF using its main token (via `@ecfx/sdk` or any other SDK) and receives a `messageId`
2. Your **backend** generates a **read-only API key** scoped to the tenant/RNC via the `/apikey` endpoint
3. Your **frontend** uses this read-only token with `@ecfx/react` to query ECF status directly — without going through your backend

```tsx
// Get the read-only token from your backend
const { token: frontendToken } = await fetch('/api/ecf-token').then(r => r.json());

// Create the React client with the read-only token
const { $api } = createEcfReactClient({
  apiKey: frontendToken,  // read-only, scoped to tenant/RNC
  environment: 'prod',
});

function EcfStatus({ rnc, encf }: { rnc: string; encf: string }) {
  const { data } = $api.useQuery('get', '/ecf/{rnc}/{encf}', {
    params: { path: { rnc, encf } },
    refetchInterval: 3000,  // poll every 3s until finished
  });

  if (data?.progress === 'Finished') {
    return (
      <div>
        <p>Comprobante aceptado</p>
        <p>Código seguridad: {data.codSec}</p>
        <QRCode value={data.impresionUrl} />
      </div>
    );
  }

  return <p>Procesando... ({data?.progress})</p>;
}
```

This pattern offloads polling from your backend and lets the frontend talk directly to ECF SSD with a restricted token. See the [main README](../README.md#arquitectura-backend--frontend) for the full diagram.

## Non-React Usage

For server-side or non-React applications, use the base TypeScript SDK: [`@ecfx/sdk`](https://www.npmjs.com/package/@ecfx/sdk).
