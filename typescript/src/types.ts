export type { paths, components, operations } from './generated/v1';

export type Environment = 'test' | 'cert' | 'prod';

export interface EcfClientConfig {
  /** API key (JWT Bearer token) for authentication. Falls back to ECF_API_KEY env var. */
  apiKey: string;
  /** Base URL override. Takes precedence over `environment`. Falls back to ECF_API_URL env var. */
  baseUrl?: string;
  /** Target environment. Defaults to 'test'. */
  environment?: Environment;
}

export interface EcfFrontendClientConfig {
  /** Function that fetches a fresh token (e.g. calls your backend's GET /ecf-token). */
  getToken: () => Promise<string>;
  /** Function to cache the token. Defaults to localStorage.setItem('ecf-token', token). */
  cacheToken?: (token: string) => Promise<void>;
  /** Function to retrieve a cached token. Defaults to localStorage.getItem('ecf-token'). */
  getCachedToken?: () => Promise<string | null>;
  /** Base URL override. Takes precedence over `environment`. */
  baseUrl?: string;
  /** Target environment. Defaults to 'test'. */
  environment?: Environment;
}

export interface PollingOptions {
  /** Initial delay between polls in ms. Default: 1000 */
  initialDelay?: number;
  /** Maximum delay between polls in ms. Default: 30000 */
  maxDelay?: number;
  /** Maximum number of retries. Default: 60 */
  maxRetries?: number;
  /** Backoff multiplier. Default: 2 */
  backoffMultiplier?: number;
  /** Total timeout in ms. Optional. */
  timeout?: number;
  /** AbortSignal for cancellation. */
  signal?: AbortSignal;
}
