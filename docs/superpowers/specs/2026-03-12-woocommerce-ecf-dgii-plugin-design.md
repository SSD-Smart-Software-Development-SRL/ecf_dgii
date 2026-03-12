# WooCommerce ECF DGII Plugin — Design Spec

## Overview

A private WooCommerce plugin that automatically sends electronic fiscal documents (ECF) to the DGII via the ECF SSD API when orders are paid. The plugin acts as a **mapper** — it reads WooCommerce order data (totals, taxes, line items) and translates it into the ECF data structure. It does not recalculate taxes or totals.

**Repository:** `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/`
**SDK dependency:** `ecfx/ecf-dgii-php` via Composer path repository pointing to `../ecf_dgii_clients/php/`
**WooCommerce compatibility:** Declares HPOS (High-Performance Order Storage) compatibility via `FeaturesUtil::declare_compatibility()`

## Business Rules

### ECF Type Selection

| Condition | ECF Type | Notes |
|-----------|----------|-------|
| No RNC, total < 250,000 DOP | E32 (Consumidor Final) | Default for anonymous buyers |
| No RNC, total >= 250,000 DOP | **Blocked** | RNC/Cédula required, checkout must enforce |
| RNC provided, any amount | User selects (E31 default) | Default ECF type configurable in settings |
| Refund/credit memo | E34 (Nota de Crédito) | Triggered from WooCommerce refund flow |
| Debit note (future) | E33 (Nota de Débito) | For post-invoice charge adjustments |

### Contingencia Flow

1. Order payment confirmed → attempt to send ECF via API
2. On failure → retry with backoff (configurable max retries, e.g., 3)
3. All retries exhausted → enter contingencia mode:
   - Assign a pre-loaded B-series code to the order
   - Mark order as "contingencia"
4. Background cron job monitors recovery:
   - When API is reachable again, convert B-series orders to eNCFs
   - Send the real ECF, link it to the original B-series code
   - Update order status

## Architecture

### Plugin Structure

```
woo-ecf-dgii/
├── woo-ecf-dgii.php                  # Main plugin file, hooks registration
├── composer.json                      # Requires ecfx/ecf-dgii-php
├── uninstall.php                      # Cleanup on uninstall
├── assets/
│   ├── css/
│   │   └── admin.css                  # Admin styles
│   └── js/
│       └── admin.js                   # Admin scripts
│       └── checkout.js                # Checkout field logic
├── includes/
│   ├── class-ecf-plugin.php           # Core plugin class, initialization
│   ├── class-ecf-settings.php         # WooCommerce settings tab
│   ├── class-ecf-order-handler.php    # Order payment → ECF submission
│   ├── class-ecf-mapper.php           # WooCommerce order → ECF model mapping
│   ├── class-ecf-contingencia.php     # B-series fallback + recovery
│   ├── class-ecf-sequence-manager.php # eNCF and B-series sequence tracking
│   ├── class-ecf-checkout-fields.php  # RNC/tipo comprobante fields
│   ├── class-ecf-admin-order.php      # Admin order panel (ECF status display)
│   ├── class-ecf-certificate.php      # Certificate upload (delegación)
│   └── class-ecf-cron.php            # Background jobs (contingencia recovery)
├── templates/
│   └── admin/
│       └── order-ecf-metabox.php      # ECF status metabox in order edit
├── dev/
│   ├── podman-compose.yml             # WordPress + WooCommerce + MariaDB
│   └── setup.sh                       # Dev environment setup script
└── README.md                          # Installation and usage guide
```

### Data Flow

```
Customer places order
        │
        ▼
WooCommerce payment confirmed
  Primary hook: woocommerce_payment_complete
  Fallback hooks: woocommerce_order_status_processing,
                  woocommerce_order_status_completed
  (Needed because woocommerce_payment_complete does not fire
   for offline methods like bank transfer until admin marks paid)
        │
        ▼
EcfOrderHandler::onPaymentComplete($order_id)
        │
        ▼
EcfMapper::mapOrder($order) → ECF model
  - Reads order lines, totals, taxes
  - Maps WooCommerce tax rates → indicadorFacturacion (SDK enums)
  - Populates emisor from API-fetched company data (cached)
  - Populates comprador from checkout RNC field (if provided)
  - Assigns next eNCF from sequence
  - Sets version, fechaVencimientoSecuencia, indicadorBienoServicio
        │
        ▼
Two submission strategies depending on WooCommerce's invoice flow:

  STRATEGY A — Backend/Frontend (preferred if WC generates invoices async)
  ─────────────────────────────────────────────────────────────────────────
  Backend (PHP, on payment hook):
    1. Map order → ECF model
    2. Submit via EcfApi::recepcionEcf31/32/etc → returns messageId
    3. Store messageId on order meta, return to frontend
    4. Generate read-only ECF token via ApiKeyApi::newCompanyApiKey()
       (cached per session, scoped to tenant/RNC, read-only)

  Frontend (JS, on order confirmation/invoice page):
    1. Use the read-only token to poll ECF SSD directly
    2. GET /ecf/{rnc}/{messageId} with refetch interval
    3. When progress = Finished → display codSec, QR (impresionUrl)
    4. On 401 → request new token from backend

  This offloads polling from the PHP backend to the browser.

  STRATEGY B — Backend-only (if WC needs invoice at order completion)
  ─────────────────────────────────────────────────────────────────────
  Use EcfService::sendEcf() via WooCommerce Action Scheduler:
    1. On payment hook → schedule async action with order data
    2. Action Scheduler worker calls sendEcf() (blocks up to 60s)
    3. Store result on order meta
    4. If timeout/failure → contingencia flow

  Strategy B is simpler but heavier on the server.

  DECISION: Investigate WooCommerce's invoice/order-received page
  during Phase 1 to determine which strategy fits. If WC shows an
  order confirmation page where we can poll → Strategy A.
  If invoice must be available immediately → Strategy B.
        │
        ├── Success → store eNCF, codSec, status on order meta
        │
        └── Failure after retries → EcfContingencia::activate($order)
                - Assign B-series code
                - Queue for later conversion
```

### Database Storage

Uses WooCommerce order meta (wp_postmeta / wc_orders_meta):

| Meta Key | Description |
|----------|-------------|
| `_ecf_type` | ECF type used (E31, E32, etc.) |
| `_ecf_encf` | Assigned eNCF number |
| `_ecf_status` | Status: pending, sent, accepted, rejected, contingencia |
| `_ecf_codsec` | Security code from DGII response |
| `_ecf_message_id` | API message ID for tracking |
| `_ecf_response` | Full serialized ECF response |
| `_ecf_b_series_code` | B-series code if contingencia |
| `_ecf_errors` | Error details if rejected |
| `_ecf_rnc_comprador` | Buyer RNC/Cédula |
| `_ecf_razon_social` | Buyer business name |

Plugin settings stored via WordPress options API (`wp_options`):

| Option Key | Description |
|------------|-------------|
| `ecf_dgii_api_token` | API authentication token |
| `ecf_dgii_environment` | test / cert / prod |
| `ecf_dgii_company_rnc` | Company RNC (immutable once set) |
| `ecf_dgii_company_data` | Cached company data from API |
| `ecf_dgii_default_ecf_type` | Default ECF type when RNC present (default: E31) |
| `ecf_dgii_encf_sequences` | JSON: configured eNCF ranges per type |
| `ecf_dgii_b_series_codes` | JSON: pre-loaded B-series codes |
| `ecf_dgii_retry_max` | Max retry attempts before contingencia |
| `ecf_dgii_retry_interval` | Retry backoff interval in seconds |

### Custom DB Table: eNCF Sequences

```sql
CREATE TABLE {prefix}ecf_sequences (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    ecf_type VARCHAR(5) NOT NULL,          -- E31, E32, etc.
    serie CHAR(1) NOT NULL DEFAULT 'E',    -- E for electronic, B for contingencia
    prefix VARCHAR(13) NOT NULL,           -- e.g., "E310000000"
    current_number BIGINT NOT NULL,        -- current position in range
    range_start BIGINT NOT NULL,           -- start of assigned range
    range_end BIGINT NOT NULL,             -- end of assigned range
    expiration_date DATE NOT NULL,         -- sequence expiration
    is_active TINYINT(1) DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Concurrency: next number must be claimed atomically to prevent
-- duplicate eNCF assignment under concurrent orders:
-- UPDATE {prefix}ecf_sequences
--   SET current_number = current_number + 1
--   WHERE id = ? AND current_number < range_end AND is_active = 1
-- Check affected rows = 1; if 0, sequence is exhausted.
```

## Settings Page

Located under **WooCommerce > Settings > ECF DGII** tab.

### Sections

**1. Conexión API**
- Environment selector: Test / Certificación / Producción
- API Token (password field)
- "Test Connection" button — calls API and displays company info
- Connection status indicator

**2. Datos de la Empresa**
- RNC field (set once, disabled after save — fetches from Company API)
- Display (read-only): Razón Social, Dirección, Teléfono, etc. from Company endpoint
- Certificate upload for delegación (file input + upload button)
- Certificate status display

**3. Secuencias eNCF**
- Table of active sequences per ECF type
- Fields: ECF Type, Prefix, Range Start, Range End, Expiration, Current Position
- Add/edit/deactivate sequences

**4. Códigos B (Contingencia)**
- Input for B-series code ranges
- Display of available/used B-series codes
- Warning when stock is low

**5. Configuración General**
- Default ECF type for RNC orders (dropdown: E31, E32)
- Max retry attempts before contingencia (default: 3)
- Retry interval in seconds (default: 5)

## Checkout Fields

### Customer-Facing Fields

Added after billing fields:

1. **RNC o Cédula** — text input, optional (required if order >= 250k)
   - Validation: 9 digits (RNC) or 11 digits (Cédula)
   - Label: "RNC o Cédula (opcional)"
   - When total >= 250k: label changes to required, field is mandatory

2. **Tipo de Comprobante** — dropdown, shown only when RNC is provided
   - Options: "Crédito Fiscal (E31)", "Consumo (E32)"
   - Default: configurable from settings
   - Hidden via JS when RNC field is empty

3. **Razón Social** — text input, shown only when RNC is provided
   - Required when RNC is filled

### Validation

- If no RNC and total >= 250,000: block checkout with error message
- If RNC provided: validate format (9 or 11 digits)
- Tipo comprobante required when RNC is present

## SDK Type Reference

### ECF Type → SDK Enum

| Shorthand | SDK Constant |
|-----------|-------------|
| E31 | `TipoeCFType::FACTURA_DE_CREDITO_FISCAL_ELECTRONICA` |
| E32 | `TipoeCFType::FACTURA_DE_CONSUMO_ELECTRONICA` |
| E33 | `TipoeCFType::NOTA_DE_DEBITO_ELECTRONICA` |
| E34 | `TipoeCFType::NOTA_DE_CREDITO_ELECTRONICA` |

### Required ECF Fields (easy to miss)

These fields are required by the SDK and must always be set:

| Field | Location | Value |
|-------|----------|-------|
| `version` | `encabezado.version` | `VersionType::VERSION1_0` |
| `fechaVencimientoSecuencia` | `idDoc.fechaVencimientoSecuencia` | From sequence manager (expiration date of the eNCF range) |
| `retencion` | Each `Item.retencion` | `Retencion` object (nullable fields for ISR withholding) |
| `indicadorBienoServicio` | Each `Item.indicador_bieno_servicio` | `IndicadorBienoServicioType::BIEN` for physical products, `IndicadorBienoServicioType::SERVICIO` for virtual/downloadable |

## Tax Mapping

WooCommerce tax rates → ECF `indicadorFacturacion` (SDK enum values):

| WooCommerce Tax Rate | SDK Constant | Description |
|---------------------|-------------|-------------|
| 18% | `IndicadorFacturacionType::ITBIS1_18_PERCENT` | ITBIS 18% (standard) |
| 16% | `IndicadorFacturacionType::ITBIS2_16_PERCENT` | ITBIS 16% (reduced) |
| 0% | `IndicadorFacturacionType::ITBIS3_0_PERCENT` | ITBIS 0% |
| Tax-exempt class | `IndicadorFacturacionType::EXENTO_E` | Exempt from ITBIS |
| No tax class | `IndicadorFacturacionType::NO_FACTURABLE_18_PERCENT` | No facturable |

The plugin reads the tax applied to each WooCommerce line item and maps it to the corresponding SDK enum. Tax amounts come directly from WooCommerce — no recalculation.

**Tax subtotals:** The `Totales` model only has `montoTotal` and `montoExento`. Per-rate ITBIS subtotals go into the ECF's `subtotales[]` array (using `Subtotal` objects), not into `Totales`.

## WooCommerce Order → ECF Mapping

```
WooCommerce Order                    ECF Model
─────────────────                    ─────────
Store settings (cached from API)  →  encabezado.emisor
  - rnc, razón social, dirección
  - teléfono, email, etc.

Checkout RNC field                →  encabezado.comprador
  - razón social                      - razonSocialComprador
  NOTE: The SDK Comprador model only has `identificadorExtranjero`
  and `razonSocialComprador`. The buyer RNC for domestic transactions
  is handled by the ECF SSD API based on the eNCF type and document
  context — the plugin does not need to set it on the Comprador model.

Always set                        →  encabezado.version = VersionType::VERSION1_0

Order total (inc. tax)            →  encabezado.totales.montoTotal
Exempt amount (if any)            →  encabezado.totales.montoExento
ITBIS subtotals by rate           →  ecf.subtotales[] (Subtotal objects)

Each order line item              →  detallesItems[]
  - product name                  →    nombreItem
  - quantity                      →    cantidadItem
  - unit price (ex. tax)          →    precioUnitarioItem
  - line total (ex. tax)          →    montoItem
  - tax rate applied              →    indicadorFacturacion (SDK enum)
  - line number (1-based)         →    numeroLinea
  - physical/virtual product      →    indicadorBienoServicio (Bien/Servicio)
  - withholding (usually empty)   →    retencion (Retencion object)

Shipping line (if present)        →  detallesItems[] (as additional line, Servicio)
Fees (if present)                 →  detallesItems[] (as additional lines)

Sequence manager                  →  idDoc.encf (next available eNCF)
Sequence expiration               →  idDoc.fechaVencimientoSecuencia
Current date                      →  emisor.fechaEmision
Plugin config                     →  idDoc.tipoeCF (SDK TipoeCFType enum)
```

## Admin Order Panel

A metabox in the WooCommerce order edit screen:

**ECF DGII Status**
- Status badge: Pendiente / Enviado / Aceptado / Rechazado / Contingencia
- eNCF number (or B-series code if contingencia)
- Security code (codSec)
- DGII response timestamp
- Error details (if rejected)
- "Reenviar" button (manual retry for failed submissions)

## Refund → E34 (Credit Note)

When a WooCommerce refund is created:
1. Hook: `woocommerce_order_refunded`
2. Build E34 referencing the original eNCF via `InformacionReferencia`:
   - `ncfModificado` → original order's eNCF number
   - `fechaNCFModificado` → original invoice emission date
   - `codigoModificacion` → reason code (`CodigoModificacionType`)
3. Map refund lines (quantities, amounts) to E34 items
   - Supports partial refunds: only refunded items/amounts are included
4. Send via API (same async Action Scheduler flow)
5. Store E34 eNCF and response on the refund meta

## Dev Environment

### Podman Compose

```yaml
services:
  db:
    image: mariadb:10.11
    environment:
      MYSQL_ROOT_PASSWORD: wordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    volumes:
      - db_data:/var/lib/mysql

  wordpress:
    image: wordpress:6.4-php8.2
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DEBUG: 1
    volumes:
      - wp_data:/var/www/html
      - ./:/var/www/html/wp-content/plugins/woo-ecf-dgii
      # SDK loaded via Composer path repository (see composer.json)
      - ../../ecf_dgii_clients/php:/opt/ecf-dgii-php
    depends_on:
      - db

volumes:
  db_data:
  wp_data:
```

### Testing Workflow

1. `podman-compose up -d` from `woo-ecf-dgii/dev/`
2. Access WordPress at `localhost:8080`
3. Install WooCommerce via admin panel (or WP-CLI in container)
4. Plugin auto-mounted via volume, activate from Plugins page
5. Configure ECF settings with test environment token
6. Create test orders and verify ECF submission

## Implementation Phases

### Phase 1: Foundation + E32

- Dev environment (podman-compose)
- Plugin skeleton (main file, autoloading, activation hooks)
- Settings page (API connection, company data fetch, sequence config)
- EcfMapper: basic order → E32 mapping
- EcfOrderHandler: send on payment complete
- Admin order metabox showing ECF status
- Sequence manager for eNCF tracking
- End-to-end test: create order → ECF sent to test API → response stored

### Phase 2: RNC + E31

- Checkout fields (RNC, Razón Social, Tipo Comprobante)
- 250k validation rule
- E31 mapping with comprador data
- ECF type selection logic
- Update admin metabox to show buyer info

### Phase 3: Credit Notes (E34) + Debit Notes (E33)

- Refund hook → E34 generation
- Reference to original eNCF in credit note
- E33 support for debit notes
- Admin UI for viewing credit/debit notes per order

### Phase 4: Contingencia

- Retry mechanism with configurable backoff
- B-series sequence manager
- Contingencia activation flow
- Background cron for recovery (B-series → eNCF conversion)
- Admin dashboard: contingencia status, pending conversions
- Low B-series stock warnings

### Phase 5: Nice-to-Haves

- RNC real-time validation via DGII directory API
- Customer invoice download (My Account > Orders)
- Invoice printing template with QR code
- Bulk ECF status refresh
- Export/reporting tools
