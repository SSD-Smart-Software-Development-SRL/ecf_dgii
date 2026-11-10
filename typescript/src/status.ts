import type { components } from './generated/v1';

type EcfResponse = components['schemas']['EcfResponse'];

/** Where the DGII transmission of an ECF stands (`EcfResponse.dgiiSubmissionState`). */
export type DgiiSubmissionState = NonNullable<components['schemas']['DgiiSubmissionState']>;

type StatusFields = Pick<EcfResponse, 'progress'> & { dgiiSubmissionState?: string | null };

/**
 * DGII's result is not confirmed yet (`progress` is `UploadedToDgii`, `estatus` is `EnProceso`).
 * Keep polling; do NOT resend the document or reuse its eNCF.
 */
export function isPendingReconciliation(response: StatusFields): boolean {
  return response.dgiiSubmissionState === 'PendingReconciliation';
}

/**
 * DGII confirmed it has no record of the document (`NotReceived`): the ECF was not accepted,
 * `secuenciaUtilizada` is false and the same eNCF may be submitted again as a new request.
 */
export function canResubmit(response: StatusFields): boolean {
  return response.dgiiSubmissionState === 'NotReceived';
}

/**
 * True when polling should stop. `PendingReconciliation` keeps polling and `NotReceived`
 * stops it regardless of `progress`; otherwise `progress` must be `Finished` or `Error`.
 * Unknown or null submission states fall back to `progress`.
 */
export function isTerminal(response: StatusFields): boolean {
  if (isPendingReconciliation(response)) return false;
  if (canResubmit(response)) return true;
  return response.progress === 'Finished' || response.progress === 'Error';
}
