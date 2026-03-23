# @ssddo/ecf-react

Hooks de React Query para la API de ECF DGII (comprobantes fiscales electrónicos de República Dominicana). Construido sobre `openapi-react-query` y `openapi-fetch` para interacciones con la API completamente tipadas.

## Instalación

```bash
npm install @ssddo/ecf-react @tanstack/react-query
```

## Configuración

Envuelve tu aplicación con `QueryClientProvider` y crea el cliente ECF:

```tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { createEcfReactClient } from '@ssddo/ecf-react';

const queryClient = new QueryClient();

const { $api } = createEcfReactClient({
  apiKey: 'tu-api-key',
  environment: 'test', // 'test' | 'cert' | 'prod'
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <TuApp />
    </QueryClientProvider>
  );
}
```

También puedes proporcionar una URL base personalizada en lugar de usar un entorno predefinido:

```tsx
const { $api } = createEcfReactClient({
  apiKey: 'tu-api-key',
  baseUrl: 'https://api-personalizada.ejemplo.com',
});
```

## Uso

### Consultar datos

Usa el objeto `$api` para acceder a hooks tipados de React Query para cada endpoint:

```tsx
function Empresas() {
  const { data, isLoading, error } = $api.useQuery('get', '/company', {
    params: { query: { Page: 1, Limit: 10 } },
  });

  if (isLoading) return <div>Cargando...</div>;
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

### Buscar ECFs

```tsx
function BuscarEcf({ rnc }: { rnc: string }) {
  const { data } = $api.useQuery('get', '/ecf/{rnc}', {
    params: { path: { rnc } },
  });

  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
```

### Enviar ECFs (Mutaciones)

```tsx
function EnviarEcf() {
  const mutation = $api.useMutation('post', '/ecf/31');

  const handleSend = () => {
    mutation.mutate({
      body: {
        Encabezado: {
          IdDoc: {
            ENCF: "E310000051630",
            TipoeCF: "FacturaDeCreditoFiscalElectronica",
            TipoPago: "Contado",
            TipoIngresos: "01",
            TablaFormasPago: [
              { FormaPago: "Efectivo", MontoPago: 1015.25 },
            ],
            IndicadorMontoGravado: "ConITBISIncluido",
            FechaVencimientoSecuencia: "2028-12-31T00:00:00",
          },
          Emisor: {
            RNCEmisor: "131460941",
            FechaEmision: "2026-01-10",
            DireccionEmisor: "AVE. ISABEL AGUIAR NO. 269, ZONA INDUSTRIAL DE HERRERA",
            RazonSocialEmisor: "DOCUMENTOS ELECTRONICOS DE 02",
          },
          Totales: {
            ITBIS1: 18,
            MontoGravadoI1: 762.71,
            MontoGravadoTotal: 762.71,
            TotalITBIS1: 137.29,
            TotalITBIS: 137.29,
            MontoNoFacturable: 100.0,
            ImpuestosAdicionales: [
              {
                TipoImpuesto: "002",
                TasaImpuestoAdicional: 2,
                OtrosImpuestosAdicionales: 15.25,
              },
            ],
            MontoImpuestoAdicional: 15.25,
            MontoTotal: 1015.25,
            MontoPeriodo: 1015.25,
          },
          Version: "Version1_0",
          Comprador: {
            RNCComprador: "131880681",
            RazonSocialComprador: "DOCUMENTOS ELECTRONICOS DE 03",
          },
        },
        DetallesItems: [
          {
            MontoItem: 1016.95,
            NombreItem: "Iphone 18 Pro max",
            NumeroLinea: 1,
            CantidadItem: 1,
            UnidadMedida: "Unidad",
            PrecioUnitarioItem: 1016.95,
            IndicadorFacturacion: "ITBIS1_18Percent",
            IndicadorBienoServicio: "Bien",
            TablaImpuestoAdicional: [{ TipoImpuesto: "002" }],
          },
          {
            MontoItem: 100.0,
            NombreItem: "Costo de Envío",
            NumeroLinea: 2,
            CantidadItem: 1,
            UnidadMedida: "Unidad",
            PrecioUnitarioItem: 100.0,
            IndicadorFacturacion: "NoFacturable_18Percent",
            IndicadorBienoServicio: "Servicio",
          },
        ],
        DescuentosORecargos: [
          {
            TipoValor: "$",
            TipoAjuste: "D",
            NumeroLinea: 1,
            MontoDescuentooRecargo: 84.75,
            DescripcionDescuentooRecargo: "Descuento",
            IndicadorFacturacionDescuentooRecargo: "ITBIS1_18Percent",
          },
        ],
      },
    });
  };

  return (
    <div>
      <button onClick={handleSend} disabled={mutation.isPending}>
        {mutation.isPending ? 'Enviando...' : 'Enviar ECF'}
      </button>
      {mutation.isSuccess && <p>ECF enviado exitosamente!</p>}
      {mutation.isError && <p>Error: {mutation.error.message}</p>}
    </div>
  );
}
```

## Entornos

| Entorno | URL |
|---------|-----|
| `test` | `https://api.test.ecfx.ssd.com.do` |
| `cert` | `https://api.cert.ecfx.ssd.com.do` |
| `prod` | `https://api.prod.ecfx.ssd.com.do` |

## Referencia de la API

### `createEcfReactClient(config)`

Crea un cliente tipado de React Query para la API de ECF DGII.

**Opciones de configuración:**

| Opción | Tipo | Requerido | Descripción |
|--------|------|-----------|-------------|
| `apiKey` | `string` | Sí | Tu API key para autenticación |
| `environment` | `'test' \| 'cert' \| 'prod'` | No | Entorno destino (por defecto: `'test'`) |
| `baseUrl` | `string` | No | URL base personalizada (sobreescribe `environment`) |

**Retorna:** `{ $api, fetchClient }`

- `$api` - El cliente openapi-react-query con `useQuery`, `useMutation`, `useSuspenseQuery`, etc.
- `fetchClient` - El cliente openapi-fetch subyacente para uso fuera de React.

## Arquitectura Backend / Frontend

El SDK de React está diseñado para el lado del **frontend** de la arquitectura recomendada:

1. Tu **backend** valida, guarda y convierte tu factura interna al formato ECF, luego la envía a ECF SSD usando su token principal
2. Tu **backend** expone un endpoint (ej. `GET /api/v1/ecf-token`) que genera un **API key de solo lectura** con alcance al tenant/RNC a través del endpoint `/apikey` de ECF SSD
3. Tu **frontend** almacena este token de forma segura, lo renueva ante `401` o expiración, y lo usa con `@ssddo/ecf-react` para consultar el estado de los ECF directamente

```tsx
// Gestión de token — tu hook personalizado
// Llama al endpoint /api/v1/ecf-token de tu backend, almacena el token de forma segura,
// y lo renueva automáticamente cuando expira o recibe un 401
const ecfToken = useEcfToken();

const { $api } = createEcfReactClient({
  apiKey: ecfToken,  // solo lectura, con alcance al tenant/RNC
  environment: 'prod',
});

function EstadoEcf({ rnc, encf }: { rnc: string; encf: string }) {
  // Consulta ECF SSD directamente — no se necesita proxy en el backend
  const { data } = $api.useQuery('get', '/ecf/{rnc}/{encf}', {
    params: { path: { rnc, encf } },
    refetchInterval: 3000,
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

Este patrón descarga el polling de tu backend y permite que el frontend se comunique directamente con ECF SSD usando un token restringido. Consulta el [README principal](../README.md#arquitectura-backend--frontend) para el diagrama completo y ejemplo del backend.

## Uso fuera de React

Para aplicaciones del lado del servidor o sin React, usa el SDK base de TypeScript: [`@ssddo/ecf-sdk`](https://www.npmjs.com/package/@ssddo/ecf-sdk).
