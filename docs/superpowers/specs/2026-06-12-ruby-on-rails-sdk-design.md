# Especificación de Diseño: SDK de Ruby on Rails para ECF DGII

Este documento describe la arquitectura, diseño y plan de implementación para el SDK de Ruby on Rails del cliente de Facturación Electrónica (ECF) de la República Dominicana para SSD / DGII.

---

## 1. Contexto y Objetivos

El SDK debe integrarse al monorepo multipropósito existente y proporcionar un cliente 1:1 con la API de ECF DGII.

### Objetivos clave:
- **Generación Automática:** Usar el archivo OpenAPI spec (`v1.json`) para generar el cliente base y los modelos.
- **Aislamiento de Código:** No modificar el código generado. El código personalizado se colocará en clases/módulos independientes que envuelvan al generado.
- **Fácil uso en Rails (DX Premium):** Proveer un inicializador, configuración global limpia y detección automática mediante un `Railtie`.
- **Lógica de Polling:** Soportar polling automático de comprobantes con retroceso exponencial (exponential backoff) para manejar estados de procesamiento asíncronos.

---

## 2. Estructura de Directorios Propuesta

El SDK residirá en un directorio `ruby/` a nivel de raíz del monorepo:

```
ruby/
├── .gitignore
├── Gemfile
├── Rakefile
├── ecf-dgii.gemspec
├── README.md
├── generate.sh                 # Script local para llamar a openapi-generator
├── openapi-generator-config.yaml
├── lib/
│   ├── ecf-dgii.rb            # Entrypoint principal de la gema
│   ├── ecf_dgii/
│   │   ├── version.rb         # Versión semántica de la gema
│   │   ├── client.rb          # Custom wrapper del cliente de API (DX, Auth, Polling)
│   │   ├── polling.rb         # Utilidades de polling con exponential backoff
│   │   ├── railtie.rb         # Integración automática con Rails
│   │   ├── generators/        # Generadores de Rails
│   │   │   └── ecf_dgii/
│   │   │       ├── install_generator.rb
│   │   │       └── templates/
│   │   │           └── ecf_dgii.rb.erb  # Plantilla de initializer
│   │   └── generated/         # Código autogenerado (excluido de git)
```

---

## 3. Flujo de Generación de Código

Utilizaremos `openapi-generator-cli` para generar el cliente en Ruby de forma determinista y reproducible.

### `openapi-generator-config.yaml`
```yaml
generatorName: ruby
moduleName: EcfDgii::Generated
gemName: ecf_dgii_generated
additionalProperties:
  hideGenerationTimestamp: true
```

### `generate.sh`
Un script en bash encargado de:
1. Eliminar código generado previamente (`lib/ecf_dgii/generated/`).
2. Generar el SDK intermedio en un directorio temporal (`ecf_dgii_generated`).
3. Mover la carpeta de librerías `lib/ecf_dgii_generated/` a `lib/ecf_dgii/generated/`.
4. Reemplazar los `require 'ecf_dgii_generated/...'` internos por `require 'ecf_dgii/generated/...'`.
5. Limpiar archivos innecesarios de tests, docs o configuración del SDK intermedio.

---

## 4. Cliente Wrapper Custom (`EcfDgii::Client`)

El cliente personalizado actuará como fachada simplificada, administrando la URL base correspondiente al ambiente y aplicando la autenticación Bearer de forma transparente.

```ruby
module EcfDgii
  class Client
    ENVIRONMENT_URLS = {
      test: "https://api.test.ecfx.ssd.com.do",
      cert: "https://api.cert.ecfx.ssd.com.do",
      prod: "https://api.prod.ecfx.ssd.com.do"
    }.freeze

    attr_reader :api_client, :environment

    def initialize(api_key: nil, base_url: nil, environment: :test, timeout: 30)
      token = api_key || ENV["ECF_API_KEY"]
      resolved_url = base_url || ENV["ECF_API_URL"] || ENVIRONMENT_URLS[environment.to_sym]
      raise ArgumentError, "Se requiere un api_key o la variable de entorno ECF_API_KEY" if token.nil? || token.empty?

      config = EcfDgii::Generated::Configuration.new
      uri = URI.parse(resolved_url)
      
      config.scheme = uri.scheme
      config.host = uri.host
      config.base_path = uri.path.empty? ? "/" : uri.path
      
      config.api_key["Authorization"] = "Bearer #{token}"
      config.timeout = timeout

      @api_client = EcfDgii::Generated::ApiClient.new(config)
      @environment = environment.to_sym
    end

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
  end
end
```

---

## 5. Lógica de Polling

Para consultas asíncronas de progreso de ECF, implementaremos polling con retraso exponencial configurable.

```ruby
module EcfDgii
  class PollingError < StandardError; end
  class PollingTimeoutError < PollingError; end
  class PollingMaxRetriesError < PollingError; end

  class PollingOptions
    attr_accessor :initial_delay, :max_delay, :max_retries, :backoff_multiplier, :timeout

    def initialize(initial_delay: 2.0, max_delay: 30.0, max_retries: 0, backoff_multiplier: 1.5, timeout: 300.0)
      @initial_delay = initial_delay
      @max_delay = max_delay
      @max_retries = max_retries
      @backoff_multiplier = backoff_multiplier
      @timeout = timeout
    end
  end

  module Polling
    TERMINAL_PROGRESS = %w[Completed Failed Rejected].freeze

    def self.poll_until_complete(options = nil)
      opts = options || PollingOptions.new
      delay = opts.initial_delay
      retries = 0
      start_time = Process.clock_gettime(Process::CLOCK_MONOTONIC)

      loop do
        result = yield

        progress = nil
        if result.respond_to?(:progress)
          progress = result.progress
        elsif result.is_a?(Hash)
          progress = result[:progress] || result["progress"]
        end

        progress_value = progress.respond_to?(:value) ? progress.value : progress.to_s

        return result if TERMINAL_PROGRESS.include?(progress_value)

        elapsed = Process.clock_gettime(Process::CLOCK_MONOTONIC) - start_time
        if opts.timeout && opts.timeout > 0 && elapsed >= opts.timeout
          raise PollingTimeoutError, "El polling excedió el tiempo límite de #{opts.timeout}s (último progreso: #{progress_value})"
        end

        retries += 1
        if opts.max_retries && opts.max_retries > 0 && retries >= opts.max_retries
          raise PollingMaxRetriesError, "El polling excedió el máximo de #{opts.max_retries} intentos (último progreso: #{progress_value})"
        end

        sleep(delay)
        delay = [delay * opts.backoff_multiplier, opts.max_delay].min
      end
    end
  end
end
```

---

## 6. Configuración e Integración con Rails

### `lib/ecf-dgii.rb`
```ruby
require "uri"
require "ecf_dgii/version"
require "ecf_dgii/generated"
require "ecf_dgii/client"
require "ecf_dgii/polling"

module EcfDgii
  class << self
    attr_accessor :configuration
  end

  def self.configure
    self.configuration ||= Configuration.new
    yield(configuration)
  end

  def self.client
    @client ||= Client.new(
      api_key: configuration&.api_key,
      base_url: configuration&.base_url,
      environment: configuration&.environment || :test,
      timeout: configuration&.timeout || 30
    )
  end

  class Configuration
    attr_accessor :api_key, :base_url, :environment, :timeout

    def initialize
      @api_key = ENV["ECF_API_KEY"]
      @base_url = ENV["ECF_API_URL"]
      @environment = :test
      @timeout = 30
    end
  end
end

require "ecf_dgii/railtie" if defined?(Rails)
```

### `lib/ecf_dgii/railtie.rb`
```ruby
module EcfDgii
  class Railtie < Rails::Railtie
    # Registra ganchos o integraciones automáticas con el framework Rails si fuera necesario.
  end
end
```

### Generador de Instalación (`lib/ecf_dgii/generators/ecf_dgii/install_generator.rb`)
```ruby
require 'rails/generators'

module EcfDgii
  module Generators
    class InstallGenerator < Rails::Generators::Base
      source_root File.expand_path('templates', __dir__)

      desc 'Crea el archivo de inicialización de ecf_dgii para tu aplicación Rails.'

      def copy_initializer
        template 'ecf_dgii.rb.erb', 'config/initializers/ecf_dgii.rb'
      end
    end
  end
end
```

---

## 7. Estrategia de Pruebas

- **Unit Tests:** Utilizaremos `RSpec` como framework de pruebas.
- **Mocking:** Utilizaremos `WebMock` y `VCR` para grabar e imitar peticiones HTTP de la API de SSD / DGII, evitando realizar llamadas reales durante la suite de pruebas automatizadas en CI.
- **Pruebas de Polling:** Validar el comportamiento de retardo exponencial simulando respuestas HTTP sucesivas con estados de progreso cambiantes (`InProcess` -> `Completed`).
