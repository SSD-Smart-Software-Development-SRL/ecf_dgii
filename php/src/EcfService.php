<?php

declare(strict_types=1);

namespace Ecfx\EcfDgii;

use Ecfx\EcfDgii\Api\EcfApi;
use Ecfx\EcfDgii\Model\ECF;
use Ecfx\EcfDgii\Model\EcfProgress;
use Ecfx\EcfDgii\Model\EcfResponse;
use Ecfx\EcfDgii\Model\TipoeCFType;

/**
 * High-level ECF service that simplifies sending electronic fiscal receipts.
 *
 * Handles automatic routing by ECF type, submission, and polling until
 * the DGII finishes processing the document.
 */
class EcfService
{
    private EcfApi $ecfApi;
    private int $pollingMaxAttempts;
    private int $pollingIntervalSeconds;

    /**
     * ECF type to API route mapping.
     */
    private const TIPO_ECF_ROUTE_MAP = [
        TipoeCFType::FACTURA_DE_CREDITO_FISCAL_ELECTRONICA => 'recepcionEcf31',
        TipoeCFType::FACTURA_DE_CONSUMO_ELECTRONICA => 'recepcionEcf32',
        TipoeCFType::NOTA_DE_DEBITO_ELECTRONICA => 'recepcionEcf33',
        TipoeCFType::NOTA_DE_CREDITO_ELECTRONICA => 'recepcionEcf34',
        TipoeCFType::COMPRAS_ELECTRONICO => 'recepcionEcf41',
        TipoeCFType::GASTOS_MENORES_ELECTRONICO => 'recepcionEcf43',
        TipoeCFType::REGIMENES_ESPECIALES_ELECTRONICO => 'recepcionEcf44',
        TipoeCFType::GUBERNAMENTAL_ELECTRONICO => 'recepcionEcf45',
        TipoeCFType::COMPROBANTE_DE_EXPORTACIONES_ELECTRONICO => 'recepcionEcf46',
        TipoeCFType::COMPROBANTE_PARA_PAGOS_AL_EXTERIOR_ELECTRONICO => 'recepcionEcf47',
    ];

    /**
     * @param EcfApi $ecfApi             The generated ECF API client
     * @param int    $pollingMaxAttempts  Maximum number of polling attempts (default: 30)
     * @param int    $pollingIntervalSeconds Seconds between polling attempts (default: 2)
     */
    public function __construct(
        EcfApi $ecfApi,
        int $pollingMaxAttempts = 30,
        int $pollingIntervalSeconds = 2,
    ) {
        $this->ecfApi = $ecfApi;
        $this->pollingMaxAttempts = $pollingMaxAttempts;
        $this->pollingIntervalSeconds = $pollingIntervalSeconds;
    }

    /**
     * Send an ECF document with automatic routing, submission, and polling.
     *
     * This method:
     * 1. Reads the ECF type from encabezado->idDoc->tipoeCF
     * 2. Routes to the correct API endpoint (e.g., /ecf/31, /ecf/32, etc.)
     * 3. Submits the ECF
     * 4. Polls using the returned messageId until processing is Finished or Error
     * 5. Returns the final EcfResponse
     *
     * @param ECF      $ecf               The ECF document to send
     * @param int|null $maxAttempts        Override max polling attempts
     * @param int|null $intervalSeconds    Override polling interval
     *
     * @return EcfResponse The final response after DGII processing
     *
     * @throws ApiException           On API communication errors
     * @throws \RuntimeException      If ECF type is unsupported
     * @throws EcfPollingTimeoutException If polling exceeds max attempts
     * @throws EcfProcessingException     If DGII returns an error during processing
     */
    public function sendEcf(
        ECF $ecf,
        ?int $maxAttempts = null,
        ?int $intervalSeconds = null,
    ): EcfResponse {
        $maxAttempts ??= $this->pollingMaxAttempts;
        $intervalSeconds ??= $this->pollingIntervalSeconds;

        // 1. Determine the ECF type and route
        $tipoeCF = $ecf->getEncabezado()->getIdDoc()->getTipoeCf();
        $method = self::TIPO_ECF_ROUTE_MAP[$tipoeCF] ?? null;

        if ($method === null) {
            throw new \RuntimeException(
                "Unsupported ECF type: {$tipoeCF}. Supported types: "
                . implode(', ', array_keys(self::TIPO_ECF_ROUTE_MAP))
            );
        }

        // 2. Submit the ECF
        $response = $this->ecfApi->{$method}($ecf);
        $messageId = $response->getMessageId();
        $rnc = $ecf->getEncabezado()->getEmisor()->getRncEmisor();

        // 3. Poll until Finished or Error
        for ($attempt = 0; $attempt < $maxAttempts; $attempt++) {
            sleep($intervalSeconds);

            $results = $this->ecfApi->getEcfById($rnc, $messageId);

            if (empty($results)) {
                continue;
            }

            $latest = $results[0];
            $progress = $latest->getProgress();

            if ($progress === EcfProgress::FINISHED) {
                return $latest;
            }

            if ($progress === EcfProgress::ERROR) {
                throw new EcfProcessingException(
                    "ECF processing failed: "
                    . ($latest->getErrors() ?? $latest->getMensaje() ?? 'Unknown error'),
                    $latest
                );
            }
        }

        throw new EcfPollingTimeoutException(
            "ECF polling timed out after {$maxAttempts} attempts for message {$messageId}"
        );
    }

    /**
     * Resolve which API method to call for a given ECF type.
     *
     * @param string $tipoeCF The ECF type value
     * @return string|null The API method name, or null if unsupported
     */
    public static function resolveMethod(string $tipoeCF): ?string
    {
        return self::TIPO_ECF_ROUTE_MAP[$tipoeCF] ?? null;
    }
}
