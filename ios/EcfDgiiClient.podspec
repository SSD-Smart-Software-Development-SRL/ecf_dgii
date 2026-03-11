Pod::Spec.new do |s|
  s.name = 'EcfDgiiClient'
  s.version = '0.1.0'
  s.summary = 'Swift SDK for the ECF DGII API (Dominican Republic electronic fiscal receipts)'
  s.description = <<-DESC
    Swift client for the ECF DGII API. Provides typed models, auto-generated API endpoints,
    and a high-level EcfClient with automatic ECF routing, polling, and error handling.
    Certified by DGII for electronic fiscal receipt processing in the Dominican Republic.
  DESC
  s.homepage = 'https://github.com/puntoos/ecf-dgii-swift'
  s.license = { :type => 'MIT', :file => 'LICENSE' }
  s.authors = { 'Puntoos' => 'info@ssd.com.do' }
  s.source = { :git => 'https://github.com/puntoos/ecf-dgii-swift.git', :tag => s.version.to_s }

  s.ios.deployment_target = '13.0'
  s.osx.deployment_target = '10.15'
  s.tvos.deployment_target = '13.0'
  s.watchos.deployment_target = '6.0'

  s.swift_versions = ['6.0']
  s.source_files = 'Sources/EcfDgiiClient/**/*.swift'
  s.frameworks = 'Foundation'
end
