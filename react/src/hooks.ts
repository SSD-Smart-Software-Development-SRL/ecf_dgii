import createFetchClient from "openapi-fetch";
import createClient from "openapi-react-query";
import type { paths } from "./generated/v1";

export type Environment = 'test' | 'cert' | 'prod';

export interface EcfReactClientConfig {
  apiKey: string;
  baseUrl?: string;
  environment?: Environment;
}

const ENVIRONMENT_URLS: Record<Environment, string> = {
  test: 'https://api.test.ecfx.ssd.com.do',
  cert: 'https://api.cert.ecfx.ssd.com.do',
  prod: 'https://api.prod.ecfx.ssd.com.do',
};

export function createEcfReactClient(config: EcfReactClientConfig) {
  const baseUrl = config.baseUrl ?? ENVIRONMENT_URLS[config.environment ?? 'test'];

  const fetchClient = createFetchClient<paths>({
    baseUrl,
  });

  // Add auth middleware
  fetchClient.use({
    async onRequest({ request }) {
      request.headers.set("Authorization", `Bearer ${config.apiKey}`);
      return request;
    },
  });

  const $api = createClient(fetchClient);

  return { $api, fetchClient };
}

// --- Frontend (read-only) client ---

type PathsWithGet = {
  [K in keyof paths as paths[K] extends { get: unknown } ? K : never]: paths[K];
};

type ReadOnlyPaths = {
  [K in keyof PathsWithGet]: Pick<PathsWithGet[K], 'get' | 'parameters'> & {
    put?: never;
    post?: never;
    delete?: never;
    patch?: never;
  };
};

export function createEcfFrontendReactClient(config: EcfReactClientConfig) {
  const baseUrl = config.baseUrl ?? ENVIRONMENT_URLS[config.environment ?? 'test'];

  const fetchClient = createFetchClient<ReadOnlyPaths>({
    baseUrl,
  });

  fetchClient.use({
    async onRequest({ request }) {
      request.headers.set("Authorization", `Bearer ${config.apiKey}`);
      return request;
    },
  });

  const fullApi = createClient(fetchClient);

  const $api = {
    useQuery: fullApi.useQuery,
    useSuspenseQuery: fullApi.useSuspenseQuery,
    queryOptions: fullApi.queryOptions,
  };

  return { $api, fetchClient };
}
