<?php

declare(strict_types=1);

namespace Ecfx\EcfDgii;

use Ecfx\EcfDgii\Model\EcfResponse;

/**
 * Thrown when DGII returns an error during ECF processing.
 */
class EcfProcessingException extends ApiException
{
    private ?EcfResponse $ecfResponse;

    public function __construct(string $message, ?EcfResponse $ecfResponse = null, ?\Throwable $previous = null)
    {
        $this->ecfResponse = $ecfResponse;
        parent::__construct($message, 0, null, null, $previous);
    }

    /**
     * Get the ECF response that contained the error.
     */
    public function getEcfResponse(): ?EcfResponse
    {
        return $this->ecfResponse;
    }
}
