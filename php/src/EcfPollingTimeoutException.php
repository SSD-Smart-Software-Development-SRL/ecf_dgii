<?php

declare(strict_types=1);

namespace Ecfx\EcfDgii;

/**
 * Thrown when polling for ECF processing result exceeds the maximum number of attempts.
 */
class EcfPollingTimeoutException extends ApiException
{
    public function __construct(string $message, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, null, null, $previous);
    }
}
