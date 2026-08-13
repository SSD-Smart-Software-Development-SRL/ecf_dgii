require "uri"
require_relative "exceptions"
require_relative "polling"

module EcfDgii
  # High-level client for the ECF DGII API.
  #
  # Mirrors the TypeScript {EcfClient} 1:1 — same method names (snake_case),
  # same validation, same error semantics.
  class Client
    ENVIRONMENT_URLS = {
      test: "https://api.test.ecfx.ssd.com.do",
      cert: "https://api.cert.ecfx.ssd.com.do",
      prod: "https://api.prod.ecfx.ssd.com.do"
    }.freeze

    ECF_TYPE_ROUTE_MAP = {
      "FacturaDeCreditoFiscalElectronica" => "31",
      "FacturaDeConsumoElectronica"       => "32",
      "NotaDeDebitoElectronica"           => "33",
      "NotaDeCreditoElectronica"          => "34",
      "ComprasElectronico"                => "41",
      "GastosMenoresElectronico"          => "43",
      "RegimenesEspecialesElectronico"    => "44",
      "GubernamentalElectronico"          => "45",
      "ComprobanteDeExportacionesElectronico"  => "46",
      "ComprobanteParaPagosAlExteriorElectronico" => "47"
    }.freeze

    # @return [EcfDgii::Generated::ApiClient] The underlying API client.
    attr_reader :api_client

    # @return [Symbol] The configured environment (:test, :cert, or :prod).
    attr_reader :environment

    def initialize(api_key: nil, base_url: nil, environment: :test, timeout: 30)
      token = api_key || ENV["ECF_API_KEY"]
      resolved_url = base_url || ENV["ECF_API_URL"] || ENVIRONMENT_URLS[environment.to_sym]

      raise ArgumentError, "Se requiere un api_key o la variable de entorno ECF_API_KEY" if token.nil? || token.empty?
      raise ArgumentError, "El entorno especificado o la URL base no son válidos" if resolved_url.nil? || resolved_url.empty?

      config = EcfDgii::Generated::Configuration.new
      uri = URI.parse(resolved_url)

      config.scheme = uri.scheme
      config.host = uri.host
      config.base_path = uri.path.empty? ? "" : uri.path

      config.access_token = token
      config.timeout = timeout

      @api_client = EcfDgii::Generated::ApiClient.new(config)
      @environment = environment.to_sym
    end

    # ---------------------------------------------------------------------------
    # Base API clients
    # ---------------------------------------------------------------------------

    def ecf_api
      @ecf_api ||= EcfDgii::Generated::EcfApi.new(api_client)
    end

    def dgii_api
      @dgii_api ||= EcfDgii::Generated::DgiiApi.new(api_client)
    end

    def recepcion_api
      @recepcion_api ||= EcfDgii::Generated::RecepcionApi.new(api_client)
    end

    def company_api
      @company_api ||= EcfDgii::Generated::CompanyApi.new(api_client)
    end

    def aprobacion_comercial_api
      @aprobacion_comercial_api ||= EcfDgii::Generated::AprobacionComercialApi.new(api_client)
    end

    def api_key_api
      @api_key_api ||= EcfDgii::Generated::ApiKeyApi.new(api_client)
    end

    # ---------------------------------------------------------------------------
    # ECF send + poll (mirrors TypeScript EcfClient.sendEcf)
    # ---------------------------------------------------------------------------

    # Send an ECF and poll until processing completes.
    #
    # Determines the correct endpoint from +ecf.encabezado.idDoc.tipoeCF+,
    # posts the ECF, then polls until +progress+ is +Finished+ or +Error+.
    #
    # @param ecf [Object] Any ECF object (Ecf31ECF … Ecf47ECF) or Hash
    # @param polling_options [PollingOptions, nil] Polling configuration
    # @return [Object] The final EcfResponse when processing is complete
    # @raise [ArgumentError] If required fields (tipoeCF, rncEmisor, encf) are missing
    # @raise [EcfError] If the ECF type is unknown
    # @raise [EcfError] If processing finishes with progress "Error"
    # @raise [PollingTimeoutError] If total timeout is exceeded
    # @raise [PollingMaxRetriesError] If max retries is exceeded
    def send_ecf(ecf, polling_options = nil)
      # 1. Extract tipoeCF
      tipoe_cf = extract_tipoe_cf(ecf)
      raise ArgumentError, "ECF must have encabezado.idDoc.tipoeCF" if tipoe_cf.nil? || tipoe_cf.to_s.empty?

      # 2. Resolve route
      route = ECF_TYPE_ROUTE_MAP[tipoe_cf.to_s]
      raise ArgumentError, "Unknown tipoeCF: #{tipoe_cf}" if route.nil?

      # 3. Extract rncEmisor (for polling)
      rnc = extract_rncemisor(ecf)
      raise ArgumentError, "ECF must have encabezado.emisor.rncEmisor" if rnc.nil? || rnc.to_s.empty?

      # 4. Extract encf (for polling)
      encf = extract_encf(ecf)
      raise ArgumentError, "ECF must have encabezado.idDoc.encf" if encf.nil? || encf.to_s.empty?

      # 5. POST to the correct endpoint
      response = post_ecf(route, ecf)

      # 6. Poll until complete
      result = poll_until_complete(response, rnc, encf, polling_options)

      # 7. Throw EcfError if progress is Error (matching TS behavior)
      progress = extract_progress_value(result)
      if progress == "Error"
        error_msg = nil
        if result.respond_to?(:errors)
          error_msg = result.errors
        elsif result.respond_to?(:mensaje)
          error_msg = result.mensaje
        end
        error_msg ||= result[:errors] || result[:mensaje] || result["errors"] || result["mensaje"] || "ECF processing failed"
        raise EcfError.new(error_msg, result)
      end

      result
    end

    # ---------------------------------------------------------------------------
    # Individual ECF type send methods

    def send_ecf31(ecf)
      ecf_api.recepcion_ecf_31(ecf)
    end

    def send_ecf32(ecf)
      ecf_api.recepcion_ecf_32(ecf)
    end

    def send_ecf33(ecf)
      ecf_api.recepcion_ecf_33(ecf)
    end

    def send_ecf34(ecf)
      ecf_api.recepcion_ecf_34(ecf)
    end

    def send_ecf41(ecf)
      ecf_api.recepcion_ecf_41(ecf)
    end

    def send_ecf43(ecf)
      ecf_api.recepcion_ecf_43(ecf)
    end

    def send_ecf44(ecf)
      ecf_api.recepcion_ecf_44(ecf)
    end

    def send_ecf45(ecf)
      ecf_api.recepcion_ecf_45(ecf)
    end

    def send_ecf46(ecf)
      ecf_api.recepcion_ecf_46(ecf)
    end

    def send_ecf47(ecf)
      ecf_api.recepcion_ecf_47(ecf)
    end

    # ---------------------------------------------------------------------------
    # Company operations
    # ---------------------------------------------------------------------------

    # List companies with optional filters.
    def get_companies(opts = {})
      company_api.get_companies(opts)
    end

    # Get a company by RNC.
    def get_company_by_rnc(rnc)
      company_api.get_company_by_rnc(rnc)
    end

    # Create or update a company.
    def upsert_company(body)
      company_api.upsert_company(body)
    end

    # Delete a company by RNC.
    def delete_company(rnc)
      company_api.delete_company(rnc)
    end

    # ---------------------------------------------------------------------------
    # Certificate operations
    # ---------------------------------------------------------------------------

    # Get the current certificate for a company.
    def get_certificate(rnc)
      company_api.get_current_certificate(rnc)
    end

    # Update a company's certificate.
    #
    # @param rnc [String] Company RNC
    # @param certificate [String, File] Path to the .p12 file or a File object
    # @param password [String] Certificate password
    def update_certificate(rnc, certificate, password)
      company_api.update_certificate_company(rnc, certificate, password)
    end

    # ---------------------------------------------------------------------------
    # ECF query & search operations
    # ---------------------------------------------------------------------------

    # Query ECFs by RNC and eNCF.
    def query_ecf(rnc, encf, opts = {})
      ecf_api.query_ecf(rnc, encf, opts)
    end

    # Search ECFs for a specific RNC.
    def search_ecfs(rnc, opts = {})
      ecf_api.search_ecfs(rnc, opts)
    end

    # Search all ECFs across all companies.
    def search_all_ecfs(opts = {})
      ecf_api.search_all_ecfs(opts)
    end

    # Get a specific ECF by RNC and message ID.
    def get_ecf_by_id(rnc, id)
      ecf_api.get_ecf_by_id(rnc, id)
    end

    # ---------------------------------------------------------------------------
    # Anulación rangos
    # ---------------------------------------------------------------------------

    # Request range annulment.
    def anulacion_rangos(rnc, body)
      ecf_api.anulacion_rangos(rnc, body)
    end

    # List annulments.
    def list_anulaciones(opts = {})
      ecf_api.list_anulaciones(opts)
    end

    # ---------------------------------------------------------------------------
    # Firmar semilla
    # ---------------------------------------------------------------------------

    # Sign a seed for a company.
    def firmar_semilla(rnc, body)
      ecf_api.firmar_semilla(rnc, body)
    end

    # ---------------------------------------------------------------------------
    # Reception operations
    # ---------------------------------------------------------------------------

    # Search ECF reception requests.
    def search_ecf_reception_requests(opts = {})
      recepcion_api.search_ecf_reception_requests(opts)
    end

    # Search ACECF reception requests.
    def search_acecf_reception_requests(opts = {})
      aprobacion_comercial_api.search_acecf_reception_requests(opts)
    end

    # Search ECF reception requests by RNC.
    def search_ecf_reception_requests_by_rnc(rnc, opts = {})
      recepcion_api.search_ecf_reception_requests_by_rnc(rnc, opts)
    end

    # Get a specific ECF reception request by RNC and messageId.
    def get_ecf_reception_request(rnc, message_id)
      recepcion_api.get_ecf_reception_request(rnc, message_id)
    end

    # Get a specific ACECF reception request by messageId.
    def get_acecf_reception_request(message_id)
      aprobacion_comercial_api.get_acecf_reception_request(message_id)
    end

    # ---------------------------------------------------------------------------
    # Aprobación comercial
    # ---------------------------------------------------------------------------

    # Send aprobación comercial (ACECF) for a given ECF reception messageId.
    def aprobacion_comercial(message_id, body)
      recepcion_api.aprobacion_comercial(message_id, body)
    end

    # ---------------------------------------------------------------------------
    # ApiKey operations
    # ---------------------------------------------------------------------------

    # Create a new API key (read-only, scoped token for frontend use).
    def create_api_key(body)
      api_key_api.new_company_api_key(body)
    end

    # ---------------------------------------------------------------------------
    # DGII operations
    # ---------------------------------------------------------------------------

    # Consulta directorio — listado.
    def consulta_directorio_listado(rnc)
      dgii_api.consulta_directorio_listado(rnc)
    end

    # Consulta directorio — obtener directorio por RNC.
    def consulta_directorio_por_rnc(rnc, target_rnc)
      dgii_api.consulta_directorio_obtener_directorio_por_rnc(rnc, target_rnc)
    end

    # Consulta estado.
    def consulta_estado(rnc, rnc_emisor, ncf_electronico, rnc_comprador, codigo_seguridad)
      dgii_api.consulta_estado(rnc, rnc_emisor, ncf_electronico, rnc_comprador, codigo_seguridad)
    end

    # Consulta resultado.
    def consulta_resultado(rnc, track_id)
      dgii_api.consulta_resultado(rnc, track_id)
    end

    # Consulta RFCE.
    def consulta_rfce(rnc, rnc_emisor, encf, codigo_seguridad)
      dgii_api.consulta_rfce(rnc, rnc_emisor, encf, codigo_seguridad)
    end

    # Consulta timbre.
    def consulta_timbre(rnc, rnc_emisor, ncf_electronico, rnc_comprador, codigo_seguridad, fecha_emision, monto_total, uid_timbre)
      dgii_api.consulta_timbre(rnc, rnc_emisor, ncf_electronico, rnc_comprador, codigo_seguridad, fecha_emision, monto_total, uid_timbre)
    end

    # Consulta timbre FC.
    def consulta_timbre_fc(rnc, rnc_emisor, ncf_electronico, rnc_comprador, fecha_emision, monto_total)
      dgii_api.consulta_timbre_fc(rnc, rnc_emisor, ncf_electronico, rnc_comprador, fecha_emision, monto_total)
    end

    # Consulta track IDs.
    def consulta_track_id(rnc, rnc_emisor, encf)
      dgii_api.consulta_track_id(rnc, rnc_emisor, encf)
    end

    # Estatus servicios — obtener estatus.
    def estatus_servicios(rnc)
      dgii_api.estatus_servicios_obtener_estatus(rnc)
    end

    # Estatus servicios — obtener ventanas de mantenimiento.
    def ventanas_mantenimiento(rnc)
      dgii_api.estatus_servicios_obtener_ventanas_mantenimiento(rnc)
    end

    private

    # Extract tipoeCF from ecf object or hash.
    def extract_tipoe_cf(ecf)
      if ecf.respond_to?(:encabezado) && ecf.encabezado.respond_to?(:id_doc)
        id_doc = ecf.encabezado.id_doc
        return id_doc.tipoe_cf if id_doc.respond_to?(:tipoe_cf)
        return id_doc.tipoeCF if id_doc.respond_to?(:tipoeCF)
      elsif ecf.is_a?(Hash)
        return ecf.dig(:encabezado, :id_doc, :tipoe_cf) ||
               ecf.dig(:encabezado, :idDoc, :tipoeCF) ||
               ecf.dig("encabezado", "idDoc", "tipoeCF")
      end
      nil
    end

    # Extract rncEmisor from ecf object or hash.
    def extract_rncemisor(ecf)
      if ecf.respond_to?(:encabezado) && ecf.encabezado.respond_to?(:emisor)
        emisor = ecf.encabezado.emisor
        return emisor.rnc_emisor if emisor.respond_to?(:rnc_emisor)
        return emisor.rncEmisor if emisor.respond_to?(:rncEmisor)
      elsif ecf.is_a?(Hash)
        return ecf.dig(:encabezado, :emisor, :rnc_emisor) ||
               ecf.dig(:encabezado, :emisor, :rncEmisor) ||
               ecf.dig("encabezado", "emisor", "rncEmisor")
      end
      nil
    end

    # Extract encf from ecf object or hash.
    def extract_encf(ecf)
      if ecf.respond_to?(:encabezado) && ecf.encabezado.respond_to?(:id_doc)
        id_doc = ecf.encabezado.id_doc
        return id_doc.encf if id_doc.respond_to?(:encf)
      elsif ecf.is_a?(Hash)
        return ecf.dig(:encabezado, :id_doc, :encf) ||
               ecf.dig(:encabezado, :idDoc, :encf) ||
               ecf.dig("encabezado", "idDoc", "encf")
      end
      nil
    end

    # Extract progress value from a response object.
    def extract_progress_value(result)
      if result.respond_to?(:progress)
        p = result.progress
        p = p.value if p.respond_to?(:value)
        return p.to_s
      elsif result.is_a?(Hash)
        p = result[:progress] || result["progress"]
        return p.to_s if p
      end
      ""
    end

    # Internal: POST to the correct /ecf/{route} endpoint.
    def post_ecf(route, body)
      case route
      when "31" then ecf_api.recepcion_ecf_31(body)
      when "32" then ecf_api.recepcion_ecf_32(body)
      when "33" then ecf_api.recepcion_ecf_33(body)
      when "34" then ecf_api.recepcion_ecf_34(body)
      when "41" then ecf_api.recepcion_ecf_41(body)
      when "43" then ecf_api.recepcion_ecf_43(body)
      when "44" then ecf_api.recepcion_ecf_44(body)
      when "45" then ecf_api.recepcion_ecf_45(body)
      when "46" then ecf_api.recepcion_ecf_46(body)
      when "47" then ecf_api.recepcion_ecf_47(body)
      else raise ArgumentError, "Unknown ECF route: #{route}"
      end
    end

    # Internal: poll until the ECF reaches a terminal state.
    #
    # rubocop:disable Metrics/MethodLength
    def poll_until_complete(initial_response, rnc, encf, polling_options)
      opts = polling_options || EcfDgii::PollingOptions.new

      EcfDgii::Polling.poll_until_complete(opts) do
        results = query_ecf(rnc, encf, include_ecf_content: false)
        if results.respond_to?(:first)
          results.first
        elsif results.is_a?(Array)
          results.first
        else
          results
        end
      end
    end
    # rubocop:enable Metrics/MethodLength
  end
end
