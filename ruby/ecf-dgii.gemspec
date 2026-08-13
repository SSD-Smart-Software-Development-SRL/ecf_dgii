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
  spec.add_dependency "faraday-multipart", ">= 1.0", "< 3.0"
  spec.add_dependency "marcel", ">= 1.0", "< 2.0"



  # Dependencias de desarrollo/pruebas
  spec.add_development_dependency "rspec", "~> 3.12"
  spec.add_development_dependency "webmock", "~> 3.18"
  spec.add_development_dependency "vcr", "~> 6.1"
  spec.add_development_dependency "railties", ">= 6.0", "< 9.0"
end
