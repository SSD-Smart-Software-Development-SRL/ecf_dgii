module EcfDgii
  class Railtie < Rails::Railtie
    # Make EcfDgii.client available in Rails console and controllers.
    console do
      EcfDgii.client
    end
  end
end
