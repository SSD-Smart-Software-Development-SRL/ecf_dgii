import createClient, { type Client, type Middleware } from 'openapi-fetch';
import type { paths, components, EcfClientConfig, PollingOptions } from './types';
import { pollUntilComplete } from './polling';

const ENVIRONMENT_URLS = {
  test: 'https://api.test.ecfx.ssd.com.do',
  cert: 'https://api.cert.ecfx.ssd.com.do',
  prod: 'https://api.prod.ecfx.ssd.com.do',
} as const;

const ECF_TYPE_ROUTE_MAP: Record<string, string> = {
  FacturaDeCreditoFiscalElectronica: '31',
  FacturaDeConsumoElectronica: '32',
  NotaDeDebitoElectronica: '33',
  NotaDeCreditoElectronica: '34',
  ComprasElectronico: '41',
  GastosMenoresElectronico: '43',
  RegimenesEspecialesElectronico: '44',
  GubernamentalElectronico: '45',
  ComprobanteDeExportacionesElectronico: '46',
  ComprobanteParaPagosAlExteriorElectronico: '47',
};

type ECF = components['schemas']['ECF'];
type EcfResponse = components['schemas']['EcfResponse'];
type AllTipoECFTypes = components['schemas']['AllTipoECFTypes'];
type ECFType = components['schemas']['ECFType'];

export class EcfError extends Error {
  public readonly response: EcfResponse;
  constructor(message: string, response: EcfResponse) {
    super(message);
    this.name = 'EcfError';
    this.response = response;
  }
}

/**
 * High-level client for the ECF DGII API.
 */
export class EcfClient {
  /** The underlying openapi-fetch client for direct endpoint access. */
  public readonly raw: Client<paths>;

  constructor(config: EcfClientConfig) {
    const baseUrl =
      config.baseUrl ??
      ENVIRONMENT_URLS[config.environment ?? 'test'];

    const authMiddleware: Middleware = {
      async onRequest({ request }) {
        request.headers.set('Authorization', `Bearer ${config.apiKey}`);
        return request;
      },
    };

    this.raw = createClient<paths>({ baseUrl });
    this.raw.use(authMiddleware);
  }

  // ---------------------------------------------------------------------------
  // ECF send + poll
  // ---------------------------------------------------------------------------

  /**
   * Send an ECF and poll until processing completes.
   *
   * Determines the correct endpoint from `ecf.encabezado.idDoc.tipoeCF`,
   * posts the ECF, then polls until `progress` is `Finished` or `Error`.
   */
  async sendEcf(ecf: ECF, pollingOptions?: PollingOptions): Promise<EcfResponse> {
    const tipoeCF = ecf.encabezado?.idDoc?.tipoeCF;
    if (!tipoeCF) {
      throw new Error('ECF must have encabezado.idDoc.tipoeCF');
    }

    const route = ECF_TYPE_ROUTE_MAP[tipoeCF];
    if (!route) {
      throw new Error(`Unknown tipoeCF: ${tipoeCF}`);
    }

    const rnc = ecf.encabezado?.emisor?.rncEmisor;
    if (!rnc) {
      throw new Error('ECF must have encabezado.emisor.rncEmisor');
    }

    const encf = ecf.encabezado?.idDoc?.encf;
    if (!encf) {
      throw new Error('ECF must have encabezado.idDoc.encf');
    }

    // POST to the typed endpoint
    const response = await this.postEcf(route, ecf);

    // Poll until complete
    const result = await pollUntilComplete(
      async () => {
        const { data: queryData, error: queryError } = await this.raw.GET('/ecf/{rnc}/{encf}', {
          params: { path: { rnc, encf } },
        });
        if (queryError) {
          throw new Error(`Failed to query ECF status: ${JSON.stringify(queryError)}`);
        }
        const results = queryData as EcfResponse[];
        const match = results.find((r) => r.messageId === response.messageId) ?? results[0];
        if (!match) {
          throw new Error('No ECF response found for the given rnc/encf');
        }
        return match;
      },
      (r) => r.progress === 'Finished' || r.progress === 'Error',
      pollingOptions,
    );

    if (result.progress === 'Error') {
      throw new EcfError(
        result.errors ?? result.mensaje ?? 'ECF processing failed',
        result,
      );
    }

    return result;
  }

  private async postEcf(route: string, body: ECF): Promise<EcfResponse> {
    type EcfPath = '/ecf/31' | '/ecf/32' | '/ecf/33' | '/ecf/34' | '/ecf/41' | '/ecf/43' | '/ecf/44' | '/ecf/45' | '/ecf/46' | '/ecf/47';
    const path = `/ecf/${route}` as EcfPath;
    const { data, error } = await this.raw.POST(path, { body });
    if (error) {
      throw new Error(`Failed to send ECF: ${JSON.stringify(error)}`);
    }
    return data as unknown as EcfResponse;
  }

  // ---------------------------------------------------------------------------
  // Company operations
  // ---------------------------------------------------------------------------

  /** List companies with optional filters. */
  async getCompanies(params?: {
    Rncs?: string[];
    Names?: string[];
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/company', { params: { query: params } });
  }

  /** Get a company by RNC. */
  async getCompanyByRnc(rnc: string) {
    return this.raw.GET('/company/{rnc}', { params: { path: { rnc } } });
  }

  /** Create or update a company. */
  async upsertCompany(body: components['schemas']['UpsertCompanyRequest']) {
    return this.raw.PUT('/company', { body });
  }

  /** Delete a company by RNC. */
  async deleteCompany(rnc: string) {
    return this.raw.DELETE('/company/{rnc}', { params: { path: { rnc } } });
  }

  // ---------------------------------------------------------------------------
  // Certificate operations
  // ---------------------------------------------------------------------------

  /** Get the current certificate for a company. */
  async getCertificate(rnc: string) {
    return this.raw.GET('/company/{rnc}/certificate', { params: { path: { rnc } } });
  }

  /** Update a company's certificate. Pass a FormData with 'certificate' file and 'password' field. */
  async updateCertificate(rnc: string, body: { certificate: Blob; password: string }) {
    const formData = new FormData();
    formData.append('certificate', body.certificate);
    formData.append('password', body.password);
    return this.raw.PUT('/company/{rnc}/certificate', {
      params: { path: { rnc } },
      body: formData as unknown as { certificate: string } & { password: string },
      bodySerializer: (b) => b as unknown as BodyInit,
    });
  }

  // ---------------------------------------------------------------------------
  // ECF query operations
  // ---------------------------------------------------------------------------

  /** Query ECFs by RNC and eNCF. */
  async queryEcf(rnc: string, encf: string) {
    return this.raw.GET('/ecf/{rnc}/{encf}', { params: { path: { rnc, encf } } });
  }

  /** Search ECFs for a specific RNC. */
  async searchEcfs(rnc: string, params?: {
    Encfs?: string[];
    Ids?: string[];
    TiposEcfs?: AllTipoECFTypes[];
    IncludeEcfContent?: boolean;
    FromFechaEmision?: string;
    ToFechaEmision?: string;
    AmountFrom?: number | string;
    AmountTo?: number | string;
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/ecf/{rnc}', {
      params: { path: { rnc }, query: params },
    });
  }

  /** Search all ECFs across all companies. */
  async searchAllEcfs(params?: {
    Encfs?: string[];
    Ids?: string[];
    TiposEcfs?: AllTipoECFTypes[];
    IncludeEcfContent?: boolean;
    FromFechaEmision?: string;
    ToFechaEmision?: string;
    AmountFrom?: number | string;
    AmountTo?: number | string;
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/ecf', { params: { query: params } });
  }

  /** Get a specific ECF by message ID. */
  async getEcfById(rnc: string, id: string) {
    return this.raw.GET('/ecf/{rnc}/message/{id}', { params: { path: { rnc, id } } });
  }

  // ---------------------------------------------------------------------------
  // Aprobacion comercial
  // ---------------------------------------------------------------------------

  /** Send aprobacion comercial for an ECF. */
  async aprobacionComercial(
    rnc: string,
    encf: string,
    body: components['schemas']['SendAcecfRequest'],
  ) {
    return this.raw.POST('/ecf/aprobacioncomercial/{rnc}/{encf}', {
      params: { path: { rnc, encf } },
      body,
    });
  }

  // ---------------------------------------------------------------------------
  // Anulacion rangos
  // ---------------------------------------------------------------------------

  /** Request range annulment. */
  async anulacionRangos(rnc: string, body: components['schemas']['AnulacionRequest']) {
    return this.raw.POST('/ecf/anularrango/{rnc}', {
      params: { path: { rnc } },
      body,
    });
  }

  /** List annulments. */
  async listAnulaciones(params?: {
    TipoEcf?: ECFType[];
    Rncs?: string[];
    FechaDesde?: string;
    FechaHasta?: string;
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/ecf/anulaciones', { params: { query: params } });
  }

  // ---------------------------------------------------------------------------
  // Firmar semilla
  // ---------------------------------------------------------------------------

  /** Sign a seed for a company. */
  async firmarSemilla(rnc: string, body: { xml: Blob }) {
    const formData = new FormData();
    formData.append('xml', body.xml);
    return this.raw.POST('/ecf/FirmarSemilla/{rnc}', {
      params: { path: { rnc } },
      body: formData as unknown as { xml: string },
      bodySerializer: (b) => b as unknown as BodyInit,
    });
  }

  // ---------------------------------------------------------------------------
  // Recepcion operations
  // ---------------------------------------------------------------------------

  /** Search ECF reception requests. */
  async searchEcfReceptionRequests(params?: {
    MessageIds?: string[];
    Encfs?: string[];
    Rncs?: string[];
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/recepcion/ecf', { params: { query: params } });
  }

  /** Search ACECF reception requests. */
  async searchAcecfReceptionRequests(params?: {
    MessageIds?: string[];
    Encfs?: string[];
    Rncs?: string[];
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/recepcion/acecf', { params: { query: params } });
  }

  /** Search ECF reception requests by RNC. */
  async searchEcfReceptionRequestsByRnc(rnc: string, params?: {
    MessageIds?: string[];
    Encfs?: string[];
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/recepcion/{rnc}/ecf', {
      params: { path: { rnc }, query: params },
    });
  }

  /** Get a specific ECF reception request. */
  async getEcfReceptionRequest(rnc: string, messageId: string) {
    return this.raw.GET('/recepcion/{rnc}/ecf/{messageId}', {
      params: { path: { rnc, messageId } },
    });
  }

  /** Search ACECF reception requests by RNC. */
  async searchAcecfReceptionRequestsByRnc(rnc: string, params?: {
    MessageIds?: string[];
    Encfs?: string[];
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/recepcion/{rnc}/acecf', {
      params: { path: { rnc }, query: params },
    });
  }

  /** Get a specific ACECF reception request. */
  async getAcecfReceptionRequest(rnc: string, messageId: string) {
    return this.raw.GET('/recepcion/{rnc}/acecf/{messageId}', {
      params: { path: { rnc, messageId } },
    });
  }

  // ---------------------------------------------------------------------------
  // DGII operations
  // ---------------------------------------------------------------------------

  /** Consulta directorio - listado. */
  async consultaDirectorioListado(rnc: string) {
    return this.raw.GET('/dgii/{rnc}/consultadirectorio/listado', {
      params: { path: { rnc } },
    });
  }

  /** Consulta directorio - obtener directorio por RNC. */
  async consultaDirectorioPorRnc(rnc: string, query: { RNC: string }) {
    return this.raw.GET('/dgii/{rnc}/consultadirectorio/obtener-directorio-por-rnc', {
      params: { path: { rnc }, query },
    });
  }

  /** Consulta estado. */
  async consultaEstado(rnc: string, query: {
    rncEmisor: string;
    ncfElectronico: string;
    rncComprador: string;
    codigoSeguridad: string;
  }) {
    return this.raw.GET('/dgii/{rnc}/consultaestado/estado', {
      params: { path: { rnc }, query },
    });
  }

  /** Consulta resultado. */
  async consultaResultado(rnc: string, query: { trackId: string }) {
    return this.raw.GET('/dgii/{rnc}/consultaresultado/estado', {
      params: { path: { rnc }, query },
    });
  }

  /** Consulta RFCE. */
  async consultaRFCE(rnc: string, query: {
    RNC_Emisor: string;
    ENCF: string;
    Cod_Seguridad_eCF: string;
  }) {
    return this.raw.GET('/dgii/{rnc}/consultarfce/consulta', {
      params: { path: { rnc }, query },
    });
  }

  /** Consulta timbre. */
  async consultaTimbre(rnc: string, query: {
    rncemisor: string;
    encf: string;
    montototal: string;
    codigoseguridad: string;
  }) {
    return this.raw.GET('/dgii/{rnc}/consultatimbre', {
      params: { path: { rnc }, query },
    });
  }

  /** Consulta timbre FC. */
  async consultaTimbreFC(rnc: string, query: {
    rncemisor: string;
    encf: string;
    montototal: string;
    codigoseguridad: string;
  }) {
    return this.raw.GET('/dgii/{rnc}/consultatimbrefc', {
      params: { path: { rnc }, query },
    });
  }

  /** Consulta track IDs. */
  async consultaTrackId(rnc: string, query: {
    rncEmisor: string;
    encf: string;
  }) {
    return this.raw.GET('/dgii/{rnc}/consultatrackids/consulta', {
      params: { path: { rnc }, query },
    });
  }

  /** Estatus servicios - obtener estatus. */
  async estatusServicios(rnc: string) {
    return this.raw.GET('/dgii/{rnc}/estatusservicios/obtener-estatus', {
      params: { path: { rnc } },
    });
  }

  /** Estatus servicios - obtener ventanas de mantenimiento. */
  async ventanasMantenimiento(rnc: string) {
    return this.raw.GET('/dgii/{rnc}/estatusservicios/obtener-ventanas-mantenimiento', {
      params: { path: { rnc } },
    });
  }

  // ---------------------------------------------------------------------------
  // ApiKey operations
  // ---------------------------------------------------------------------------

  /** Create a new API key. */
  async createApiKey(body: components['schemas']['NewCompanyApiKey']) {
    return this.raw.POST('/apiKey', { body });
  }
}

// ---------------------------------------------------------------------------
// Frontend-safe read-only client
// ---------------------------------------------------------------------------

/**
 * A restricted, read-only client that only exposes GET endpoints.
 * Suitable for use in frontend / browser code where write operations
 * should not be available.
 */
export class EcfFrontendClient {
  /** The underlying openapi-fetch client for direct endpoint access. */
  private readonly raw: Client<paths>;

  constructor(config: EcfClientConfig) {
    const baseUrl =
      config.baseUrl ??
      ENVIRONMENT_URLS[config.environment ?? 'test'];

    const authMiddleware: Middleware = {
      async onRequest({ request }) {
        request.headers.set('Authorization', `Bearer ${config.apiKey}`);
        return request;
      },
    };

    this.raw = createClient<paths>({ baseUrl });
    this.raw.use(authMiddleware);
  }

  /** Query ECFs by RNC and eNCF. */
  async queryEcf(rnc: string, encf: string) {
    return this.raw.GET('/ecf/{rnc}/{encf}', { params: { path: { rnc, encf } } });
  }

  /** Search ECFs for a specific RNC. */
  async searchEcfs(rnc: string, params?: {
    Encfs?: string[];
    Ids?: string[];
    TiposEcfs?: AllTipoECFTypes[];
    IncludeEcfContent?: boolean;
    FromFechaEmision?: string;
    ToFechaEmision?: string;
    AmountFrom?: number | string;
    AmountTo?: number | string;
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/ecf/{rnc}', {
      params: { path: { rnc }, query: params },
    });
  }

  /** Search all ECFs across all companies. */
  async searchAllEcfs(params?: {
    Encfs?: string[];
    Ids?: string[];
    TiposEcfs?: AllTipoECFTypes[];
    IncludeEcfContent?: boolean;
    FromFechaEmision?: string;
    ToFechaEmision?: string;
    AmountFrom?: number | string;
    AmountTo?: number | string;
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/ecf', { params: { query: params } });
  }

  /** Get a specific ECF by message ID. */
  async getEcfById(rnc: string, id: string) {
    return this.raw.GET('/ecf/{rnc}/message/{id}', { params: { path: { rnc, id } } });
  }

  /** List companies with optional filters. */
  async getCompanies(params?: {
    Rncs?: string[];
    Names?: string[];
    Page?: number | string;
    Limit?: number | string;
  }) {
    return this.raw.GET('/company', { params: { query: params } });
  }

  /** Get a company by RNC. */
  async getCompanyByRnc(rnc: string) {
    return this.raw.GET('/company/{rnc}', { params: { path: { rnc } } });
  }
}

/**
 * Factory that creates a restricted read-only client suitable for frontend use.
 * Only GET endpoints are exposed.
 */
export function createFrontendClient(config: EcfClientConfig): EcfFrontendClient {
  return new EcfFrontendClient(config);
}
