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
