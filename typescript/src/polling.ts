import type { PollingOptions } from './types';

export class PollingTimeoutError extends Error {
  constructor(message = 'Polling timed out') {
    super(message);
    this.name = 'PollingTimeoutError';
  }
}

export class PollingMaxRetriesError extends Error {
  constructor(retries: number) {
    super(`Polling exceeded maximum retries (${retries})`);
    this.name = 'PollingMaxRetriesError';
  }
}

/**
 * Polls a function until a condition is met, using exponential backoff.
 *
 * @param fn - Async function to call on each poll
 * @param isComplete - Predicate that returns true when polling should stop
 * @param options - Polling configuration
 * @returns The final result from `fn` when `isComplete` returns true
 */
export async function pollUntilComplete<T>(
  fn: () => Promise<T>,
  isComplete: (result: T) => boolean,
  options?: PollingOptions,
): Promise<T> {
  const {
    initialDelay = 1000,
    maxDelay = 30000,
    maxRetries = 60,
    backoffMultiplier = 2,
    timeout,
    signal,
  } = options ?? {};

  const startTime = Date.now();
  let delay = initialDelay;
  let retries = 0;

  while (true) {
    if (signal?.aborted) {
      throw new DOMException('Polling was aborted', 'AbortError');
    }

    const result = await fn();

    if (isComplete(result)) {
      return result;
    }

    retries++;

    if (retries >= maxRetries) {
      throw new PollingMaxRetriesError(maxRetries);
    }

    if (timeout !== undefined && Date.now() - startTime >= timeout) {
      throw new PollingTimeoutError();
    }

    await sleep(delay, signal);
    delay = Math.min(delay * backoffMultiplier, maxDelay);
  }
}

function sleep(ms: number, signal?: AbortSignal): Promise<void> {
  return new Promise((resolve, reject) => {
    if (signal?.aborted) {
      reject(new DOMException('Polling was aborted', 'AbortError'));
      return;
    }

    const timer = setTimeout(resolve, ms);

    signal?.addEventListener(
      'abort',
      () => {
        clearTimeout(timer);
        reject(new DOMException('Polling was aborted', 'AbortError'));
      },
      { once: true },
    );
  });
}
