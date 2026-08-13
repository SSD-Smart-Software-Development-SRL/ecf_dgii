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
