# Ruby on Rails SDK Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a 1:1 Ruby on Rails SDK (`ecf-dgii` gem) with an auto-generated OpenAPI client, a custom client wrapper with JWT authentication, exponential backoff polling, and a Rails generator.

**Architecture:** Use `openapi-generator-cli` to generate a base Ruby client namespace (`EcfDgii::Generated`), wrap it with a handwritten `EcfDgii::Client` class, implement exponential backoff polling in `EcfDgii::Polling`, and integrate with Rails using a `Railtie` and generator.

**Tech Stack:** Ruby (>= 3.0), Faraday, RSpec, openapi-generator-cli.

---

## Files to be Created or Modified

### New Files:
- `ruby/Gemfile` — Gem dependencies (faraday, rspec, webmock, vcr, railties).
- `ruby/Rakefile` — Rake tasks for testing.
- `ruby/ecf-dgii.gemspec` — Gem manifest configuration.
- `ruby/openapi-generator-config.yaml` — Generator configuration for the Ruby client.
- `ruby/generate.sh` — Script to execute the generator, move generated files, and clean up.
- `ruby/lib/ecf-dgii.rb` — Library entrypoint.
- `ruby/lib/ecf_dgii/version.rb` — SDK version definition.
- `ruby/lib/ecf_dgii/client.rb` — High-level client wrapper.
- `ruby/lib/ecf_dgii/polling.rb` — Polling with exponential backoff.
- `ruby/lib/ecf_dgii/railtie.rb` — Railtie for Rails integration.
- `ruby/lib/ecf_dgii/generators/ecf_dgii/install_generator.rb` — Rails installer generator.
- `ruby/lib/ecf_dgii/generators/ecf_dgii/templates/ecf_dgii.rb.erb` — Initializer template.
- `ruby/spec/spec_helper.rb` — RSpec testing helper.
- `ruby/spec/client_spec.rb` — Client wrapper unit tests.
- `ruby/spec/polling_spec.rb` — Polling mechanism unit tests.

### Modified Files:
- `.gitignore` — Ignore generated/ directory and local gem artifacts.
- `scripts/regenerate-all.sh` — Add Ruby target to monorepo regeneration suite.

---

## Tasks

### Task 1: Initialize Project Files and Gemspec

**Files:**
- Create: `ruby/Gemfile`
- Create: `ruby/Rakefile`
- Create: `ruby/ecf-dgii.gemspec`
- Create: `ruby/lib/ecf_dgii/version.rb`
- Create: `ruby/lib/ecf-dgii.rb`
- Modify: `.gitignore`

- [ ] **Step 1: Modify root .gitignore**
  Add lines to exclude generated files, gems, and cache.
  Add at the end of `.gitignore`:
  ```
  # Ruby
  ruby/lib/ecf_dgii/generated/
  ruby/pkg/
  ruby/.bundle/
  ruby/vendor/bundle/
  ruby/Gemfile.lock
  ruby/.rspec
  ```

- [ ] **Step 2: Create version.rb**
  Create `ruby/lib/ecf_dgii/version.rb`:
  ```ruby
  module EcfDgii
    VERSION = "1.0.0"
  end
  ```

- [ ] **Step 3: Create gemspec**
  Create `ruby/ecf-dgii.gemspec`:
  ```ruby
  require_relative "lib/ecf_dgii/version"

  Gem::Specification.new do |spec|
    spec.name          = "ecf-dgii"
    spec.version       = EcfDgii::VERSION
    spec.authors       = ["SSD Smart Software Development SRL"]
    spec.email         = ["contacto@ssd.com.do"]
    spec.summary       = "SDK de Ruby para la API de ECF DGII"
    spec.description   = "SDK para integrar la Facturación Electrónica de República Dominicana (SSD/DGII)."
    spec.homepage      = "https://github.com/SSD-Smart-Software-Development-SRL/ecf_dgii"
    spec.license       = "MIT"
    spec.required_ruby_version = ">= 3.0"

    spec.files         = Dir["lib/**/*", "README.md", "LICENSE"]
    spec.require_paths = ["lib"]

    # Dependencias de producción
    spec.add_dependency "faraday", ">= 1.0", "< 3.0"

    # Dependencias de desarrollo/pruebas
    spec.add_development_dependency "rspec", "~> 3.12"
    spec.add_development_dependency "webmock", "~> 3.18"
    spec.add_development_dependency "vcr", "~> 6.1"
    spec.add_development_dependency "railties", ">= 6.0"
  end
  ```

- [ ] **Step 4: Create Gemfile**
  Create `ruby/Gemfile`:
  ```ruby
  source "https://rubygems.org"

  gemspec
  ```

- [ ] **Step 5: Create Rakefile**
  Create `ruby/Rakefile`:
  ```ruby
  require "rspec/core/rake_task"

  RSpec::Core::RakeTask.new(:spec) do |t|
    t.pattern = "spec/**/*_spec.rb"
  end

  task default: :spec
  ```

- [ ] **Step 6: Create library entrypoint**
  Create `ruby/lib/ecf-dgii.rb`:
  ```ruby
  require_relative "ecf_dgii/version"

  module EcfDgii
  end
  ```

- [ ] **Step 7: Verify initialization**
  Run: `cd ruby && bundle install`
  Expected: Successful installation of dependencies.

- [ ] **Step 8: Commit**
  Run:
  ```bash
  git add .gitignore ruby/Gemfile ruby/Rakefile ruby/ecf-dgii.gemspec ruby/lib/ecf_dgii/version.rb ruby/lib/ecf-dgii.rb
  git commit -m "feat(ruby): initialize gem structure and dependencies"
  ```

---

### Task 2: Code Generation configuration and script

**Files:**
- Create: `ruby/openapi-generator-config.yaml`
- Create: `ruby/generate.sh`
- Modify: `scripts/regenerate-all.sh`

- [ ] **Step 1: Create openapi-generator-config.yaml**
  Create `ruby/openapi-generator-config.yaml`:
  ```yaml
  generatorName: ruby
  moduleName: EcfDgii::Generated
  gemName: ecf_dgii_generated
  additionalProperties:
    hideGenerationTimestamp: true
  ```

- [ ] **Step 2: Create generate.sh**
  Create `ruby/generate.sh`:
  ```bash
  #!/usr/bin/env bash
  set -euo pipefail

  SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
  cd "$SCRIPT_DIR"

  SPEC_PATH="${SPEC_PATH:-../ios/openapi-v1-processed.json}"
  OPENAPI_GEN_VERSION="7.14.0"
  NPX_PKG="@openapitools/openapi-generator-cli@2.32.0"

  GENERATED_DIR="lib/ecf_dgii/generated"
  TEMP_GEN_DIR="ecf_dgii_generated"

  echo "Removing old generated code..."
  rm -rf "$GENERATED_DIR"
  rm -rf "$TEMP_GEN_DIR"

  echo "Generating Ruby SDK from $SPEC_PATH..."
  JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$OPENAPI_GEN_VERSION \
    npx -y $NPX_PKG generate \
      -c openapi-generator-config.yaml \
      -i "$SPEC_PATH" \
      -o "$TEMP_GEN_DIR"

  echo "Moving generated library code..."
  mkdir -p "lib/ecf_dgii"
  mv "$TEMP_GEN_DIR/lib/ecf_dgii_generated" "$GENERATED_DIR"

  echo "Adjusting internal requires..."
  # Reemplazar requires en todos los archivos generados
  find "$GENERATED_DIR" -type f -name "*.rb" -exec sed -i 's|require '\''ecf_dgii_generated/|require '\''ecf_dgii/generated/|g' {} +

  echo "Cleaning up temporal directory..."
  rm -rf "$TEMP_GEN_DIR"

  echo "Done. Generated code is in $GENERATED_DIR/"
  ```
  Make the script executable:
  `chmod +x ruby/generate.sh`

- [ ] **Step 3: Test code generation**
  Run: `cd ruby && ./generate.sh`
  Expected: Successful run, outputting "Done. Generated code is in lib/ecf_dgii/generated/". Verify that folder is populated.

- [ ] **Step 4: Modify scripts/regenerate-all.sh**
  Add `ruby` to the main regenerate script.
  Modify `scripts/regenerate-all.sh` to include `regen_ruby` function:
  Add around line 146 (before `refresh_bruno`):
  ```bash
  regen_ruby() {
    step "ruby (openapi-generator)"
    command -v npx >/dev/null && command -v java >/dev/null || { skip "ruby" "npx or java missing"; return; }
    ( cd "$REPO_ROOT/ruby" \
        && SPEC_PATH="$SPEC_PATH" ./generate.sh \
        && bundle exec rake spec ) \
      && ok "ruby" || bad "ruby"
  }
  ```
  And modify `run_target` (around line 170) to include `ruby)` target:
  ```bash
      ruby)       regen_ruby ;;
  ```
  And add `regen_ruby` to the list of default targets in the `main` function (around line 192):
  ```bash
      regen_ios
      regen_ruby
      regen_cpp
  ```

- [ ] **Step 5: Verify global regenerate-all.sh script**
  Run: `SPEC_PATH=ios/openapi-v1-processed.json ./scripts/regenerate-all.sh ruby`
  Expected: Command completes successfully, compiling/running the ruby target specs (which will be empty but pass).

- [ ] **Step 6: Commit**
  Run:
  ```bash
  git add ruby/openapi-generator-config.yaml ruby/generate.sh scripts/regenerate-all.sh
  git commit -m "feat(ruby): add code generator config, local script, and integrate with regenerate-all.sh"
  ```

---

### Task 3: Implement Core Client Wrapper

**Files:**
- Create: `ruby/lib/ecf_dgii/client.rb`
- Modify: `ruby/lib/ecf-dgii.rb`

- [ ] **Step 1: Write client.rb implementation**
  Create `ruby/lib/ecf_dgii/client.rb`:
  ```ruby
  require "uri"

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
        config.base_path = uri.path.empty? ? "" : uri.path
        
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

- [ ] **Step 2: Update entrypoint ecf-dgii.rb**
  Modify `ruby/lib/ecf-dgii.rb` to require client and implement the global config.
  Replace content of `ruby/lib/ecf-dgii.rb` with:
  ```ruby
  require "uri"
  require_relative "ecf_dgii/version"
  require_relative "ecf_dgii/generated"
  require_relative "ecf_dgii/client"

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
  ```

- [ ] **Step 3: Commit**
  Run:
  ```bash
  git add ruby/lib/ecf_dgii/client.rb ruby/lib/ecf-dgii.rb
  git commit -m "feat(ruby): implement core client wrapper and global configurator"
  ```

---

### Task 4: Implement Polling Mechanism

**Files:**
- Create: `ruby/lib/ecf_dgii/polling.rb`
- Modify: `ruby/lib/ecf-dgii.rb`

- [ ] **Step 1: Write polling.rb implementation**
  Create `ruby/lib/ecf_dgii/polling.rb`:
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

- [ ] **Step 2: Update entrypoint ecf-dgii.rb to load polling**
  Modify `ruby/lib/ecf-dgii.rb` by adding require line:
  ```ruby
  require_relative "ecf_dgii/polling"
  ```
  Insert it right below `require_relative "ecf_dgii/client"`.

- [ ] **Step 3: Commit**
  Run:
  ```bash
  git add ruby/lib/ecf_dgii/polling.rb ruby/lib/ecf-dgii.rb
  git commit -m "feat(ruby): implement exponential backoff polling mechanism"
  ```

---

### Task 5: Implement Rails Integration (Railtie & Generators)

**Files:**
- Create: `ruby/lib/ecf_dgii/railtie.rb`
- Create: `ruby/lib/ecf_dgii/generators/ecf_dgii/install_generator.rb`
- Create: `ruby/lib/ecf_dgii/generators/ecf_dgii/templates/ecf_dgii.rb.erb`
- Modify: `ruby/lib/ecf-dgii.rb`

- [ ] **Step 1: Create railtie.rb**
  Create `ruby/lib/ecf_dgii/railtie.rb`:
  ```ruby
  module EcfDgii
    class Railtie < Rails::Railtie
      # La integración se realiza mediante la inicialización diferida o el generador.
    end
  end
  ```

- [ ] **Step 2: Create generator template**
  Create `ruby/lib/ecf_dgii/generators/ecf_dgii/templates/ecf_dgii.rb.erb`:
  ```erb
  # config/initializers/ecf_dgii.rb

  EcfDgii.configure do |config|
    # Token JWT (Bearer) proveído por SSD
    config.api_key = ENV["ECF_API_KEY"]

    # Ambiente de trabajo: :test, :cert, o :prod (por defecto es :test)
    config.environment = ENV.fetch("ECF_ENVIRONMENT", "test").to_sym

    # URL base personalizada (opcional, sobreescribe el ambiente)
    # config.base_url = ENV["ECF_API_URL"]

    # Tiempo de espera máximo para solicitudes HTTP (por defecto es 30 segundos)
    # config.timeout = 30
  end
  ```

- [ ] **Step 3: Create install_generator.rb**
  Create `ruby/lib/ecf_dgii/generators/ecf_dgii/install_generator.rb`:
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

- [ ] **Step 4: Require Railtie conditionally in ecf-dgii.rb**
  Add to the end of `ruby/lib/ecf-dgii.rb`:
  ```ruby
  require_relative "ecf_dgii/railtie" if defined?(Rails)
  ```

- [ ] **Step 5: Commit**
  Run:
  ```bash
  git add ruby/lib/ecf_dgii/railtie.rb ruby/lib/ecf_dgii/generators/
  git commit -m "feat(ruby): implement Rails Railtie and installation generator"
  ```

---

### Task 6: Set up RSpec and Write Tests

**Files:**
- Create: `ruby/spec/spec_helper.rb`
- Create: `ruby/spec/client_spec.rb`
- Create: `ruby/spec/polling_spec.rb`

- [ ] **Step 1: Create spec_helper.rb**
  Create `ruby/spec/spec_helper.rb`:
  ```ruby
  require "bundler/setup"
  require "ecf-dgii"
  require "webmock/rspec"
  require "vcr"

  WebMock.disable_net_connect!(allow_localhost: true)

  VCR.configure do |config|
    config.cassette_library_dir = "spec/fixtures/vcr_cassettes"
    config.hook_into :webmock
    config.configure_rspec_metadata!
  end

  RSpec.configure do |config|
    config.expect_with :rspec do |c|
      c.syntax = :expect
    end
  end
  ```

- [ ] **Step 2: Create client_spec.rb**
  Create `ruby/spec/client_spec.rb`:
  ```ruby
  require "spec_helper"

  RSpec.describe EcfDgii::Client do
    before do
      ENV["ECF_API_KEY"] = "test-token"
    end

    after do
      ENV.delete("ECF_API_KEY")
    end

    it "initializes with correct base URL for test environment" do
      client = described_class.new(environment: :test)
      expect(client.environment).to eq(:test)
      expect(client.api_client.config.host).to eq("api.test.ecfx.ssd.com.do")
    end

    it "initializes with correct base URL for prod environment" do
      client = described_class.new(environment: :prod)
      expect(client.environment).to eq(:prod)
      expect(client.api_client.config.host).to eq("api.prod.ecfx.ssd.com.do")
    end

    it "overrides url if base_url parameter is provided" do
      client = described_class.new(base_url: "https://custom.api.com/v1")
      expect(client.api_client.config.host).to eq("custom.api.com")
      expect(client.api_client.config.base_path).to eq("/v1")
    end

    it "raises ArgumentError if no API key is provided" do
      ENV.delete("ECF_API_KEY")
      expect { described_class.new }.to raise_error(ArgumentError)
    end

    it "exposes API classes" do
      client = described_class.new
      expect(client.ecf_api).to be_an_instance_of(EcfDgii::Generated::EcfApi)
      expect(client.dgii_api).to be_an_instance_of(EcfDgii::Generated::DgiiApi)
    end
  end
  ```

- [ ] **Step 3: Create polling_spec.rb**
  Create `ruby/spec/polling_spec.rb`:
  ```ruby
  require "spec_helper"

  RSpec.describe EcfDgii::Polling do
    it "polls until status is completed" do
      states = [
        double(progress: "InProcess"),
        double(progress: "InProcess"),
        double(progress: "Completed")
      ]

      call_count = 0
      result = described_class.poll_until_complete(
        EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.01)
      ) do
        call_count += 1
        states[call_count - 1]
      end

      expect(call_count).to eq(3)
      expect(result.progress).to eq("Completed")
    end

    it "raises PollingTimeoutError if it exceeds timeout" do
      options = EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.002, timeout: 0.005)
      
      expect {
        described_class.poll_until_complete(options) do
          double(progress: "InProcess")
        end
      }.to raise_error(EcfDgii::PollingTimeoutError)
    end

    it "raises PollingMaxRetriesError if it exceeds max retries" do
      options = EcfDgii::PollingOptions.new(initial_delay: 0.001, max_delay: 0.002, max_retries: 3)
      
      expect {
        described_class.poll_until_complete(options) do
          double(progress: "InProcess")
        end
      }.to raise_error(EcfDgii::PollingMaxRetriesError)
    end
  end
  ```

- [ ] **Step 4: Run specs**
  Run: `cd ruby && bundle exec rake spec`
  Expected: All specs pass successfully.

- [ ] **Step 5: Commit**
  Run:
  ```bash
  git add ruby/spec/
  git commit -m "test(ruby): add client wrapper and polling mechanism unit tests"
  ```
