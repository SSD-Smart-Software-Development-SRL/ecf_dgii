<?php

declare(strict_types=1);

namespace Ecfx\EcfDgii;

use GuzzleHttp\ClientInterface;
use Ecfx\EcfDgii\Api\CompanyApi;
use Ecfx\EcfDgii\Api\EcfApi;
use Ecfx\EcfDgii\Model\CompanyResponse;
use Ecfx\EcfDgii\Model\EcfResponse;
use Ecfx\EcfDgii\Model\PaginatedApiResultOfCompanyResponse;
use Ecfx\EcfDgii\Model\PaginatedApiResultOfEcfResponse;

/**
 * Read-only frontend client for the ECF DGII API.
 *
 * Only exposes GET endpoints for querying ECFs and companies.
 * Intended for frontend/dashboard usage where write operations are not needed.
 *
 * Usage:
 * ```php
 * $config = Configuration::getDefaultConfiguration()
 *     ->setHost('https://api.prod.ecfx.ssd.com.do')
 *     ->setAccessToken('your-read-only-token');
 *
 * $frontendClient = new EcfFrontendClient(new \GuzzleHttp\Client(), $config);
 *
 * $results = $frontendClient->queryEcf('123456789', 'E310000000001');
 * $company = $frontendClient->getCompanyByRnc('123456789');
 * ```
 */
class EcfFrontendClient
{
    private EcfApi $ecfApi;
    private CompanyApi $companyApi;

    public function __construct(?ClientInterface $client = null, ?Configuration $config = null)
    {
        $this->ecfApi = new EcfApi($client, $config);
        $this->companyApi = new CompanyApi($client, $config);
    }

    // -------------------------------------------------------------------------
    // ECF GET endpoints
    // -------------------------------------------------------------------------

    /**
     * Query ECFs by RNC and eNCF.
     *
     * @param string $rnc  The company RNC
     * @param string $encf The eNCF identifier
     * @param bool   $includeEcfContent Whether to include full ECF content
     * @return EcfResponse[]
     * @throws ApiException
     */
    public function queryEcf(string $rnc, string $encf, bool $includeEcfContent = false): array
    {
        return $this->ecfApi->queryEcf($rnc, $encf, $includeEcfContent);
    }

    /**
     * Search ECFs for a specific RNC.
     *
     * @param string     $rnc               The company RNC
     * @param array|null $encfs             Filter by eNCFs
     * @param array|null $ids               Filter by IDs
     * @param array|null $tiposEcfs         Filter by ECF types
     * @param bool       $includeEcfContent Whether to include ECF content
     * @param string|null $fromFechaEmision Filter from emission date
     * @param string|null $toFechaEmision   Filter to emission date
     * @param mixed      $amountFrom        Filter by minimum amount
     * @param mixed      $amountTo          Filter by maximum amount
     * @param int        $page              Page number
     * @param int        $limit             Page size
     * @return PaginatedApiResultOfEcfResponse
     * @throws ApiException
     */
    public function searchEcfs(
        string $rnc,
        ?array $encfs = null,
        ?array $ids = null,
        ?array $tiposEcfs = null,
        bool $includeEcfContent = false,
        ?string $fromFechaEmision = null,
        ?string $toFechaEmision = null,
        mixed $amountFrom = null,
        mixed $amountTo = null,
        int $page = 1,
        int $limit = 25,
    ): PaginatedApiResultOfEcfResponse {
        return $this->ecfApi->searchEcfs(
            $rnc, $encfs, $ids, $tiposEcfs, $includeEcfContent,
            $fromFechaEmision, $toFechaEmision, $amountFrom, $amountTo, $page, $limit
        );
    }

    /**
     * Search ECFs across all companies.
     *
     * @param array|null  $encfs             Filter by eNCFs
     * @param array|null  $ids               Filter by IDs
     * @param array|null  $tiposEcfs         Filter by ECF types
     * @param bool        $includeEcfContent Whether to include ECF content
     * @param string|null $fromFechaEmision  Filter from emission date
     * @param string|null $toFechaEmision    Filter to emission date
     * @param mixed       $amountFrom        Filter by minimum amount
     * @param mixed       $amountTo          Filter by maximum amount
     * @param int         $page              Page number
     * @param int         $limit             Page size
     * @return PaginatedApiResultOfEcfResponse
     * @throws ApiException
     */
    public function searchAllEcfs(
        ?array $encfs = null,
        ?array $ids = null,
        ?array $tiposEcfs = null,
        bool $includeEcfContent = false,
        ?string $fromFechaEmision = null,
        ?string $toFechaEmision = null,
        mixed $amountFrom = null,
        mixed $amountTo = null,
        int $page = 1,
        int $limit = 25,
    ): PaginatedApiResultOfEcfResponse {
        return $this->ecfApi->searchAllEcfs(
            $encfs, $ids, $tiposEcfs, $includeEcfContent,
            $fromFechaEmision, $toFechaEmision, $amountFrom, $amountTo, $page, $limit
        );
    }

    /**
     * Get a specific ECF by RNC and message ID.
     *
     * @param string $rnc The company RNC
     * @param string $id  The message ID
     * @param bool   $includeEcfContent Whether to include full ECF content
     * @return EcfResponse[]
     * @throws ApiException
     */
    public function getEcfById(string $rnc, string $id, bool $includeEcfContent = false): array
    {
        return $this->ecfApi->getEcfById($rnc, $id, $includeEcfContent);
    }

    // -------------------------------------------------------------------------
    // Company GET endpoints
    // -------------------------------------------------------------------------

    /**
     * Get companies with optional filters.
     *
     * @param array|null $rncs  Filter by RNCs
     * @param array|null $names Filter by names
     * @param int        $page  Page number
     * @param int        $limit Page size
     * @return PaginatedApiResultOfCompanyResponse
     * @throws ApiException
     */
    public function getCompanies(
        ?array $rncs = null,
        ?array $names = null,
        int $page = 1,
        int $limit = 25,
    ): PaginatedApiResultOfCompanyResponse {
        return $this->companyApi->getCompanies($rncs, $names, $page, $limit);
    }

    /**
     * Get a single company by its RNC.
     *
     * @param string $rnc The company RNC
     * @return CompanyResponse
     * @throws ApiException
     */
    public function getCompanyByRnc(string $rnc): CompanyResponse
    {
        return $this->companyApi->getCompanyByRnc($rnc);
    }
}
