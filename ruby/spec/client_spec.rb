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

  describe "#send_ecf" do
    it "validates that tipoeCF is present" do
      client = described_class.new
      expect { client.send_ecf(double("ecf")) }.to raise_error(ArgumentError, /tipoeCF/)
    end

    it "validates that rncEmisor is present" do
      client = described_class.new
      id_doc = double(tipoe_cf: "FacturaDeCreditoFiscalElectronica", encf: "E310000051630")
      encabezado = double(id_doc: id_doc, emisor: double("no_emisor"))
      ecf = double(encabezado: encabezado)

      expect(ecf.encabezado.emisor).to receive(:respond_to?).with(:rnc_emisor).and_return(false)
      expect(ecf.encabezado.emisor).to receive(:respond_to?).with(:rncEmisor).and_return(false)

      expect { client.send_ecf(ecf) }.to raise_error(ArgumentError, /rncEmisor/)
    end

    it "validates that encf is present" do
      client = described_class.new
      emisor = double("emisor", rnc_emisor: "131460941")
      id_doc = double("id_doc")
      allow(id_doc).to receive(:respond_to?).with(:tipoe_cf).and_return(true)
      allow(id_doc).to receive(:tipoe_cf).and_return("FacturaDeCreditoFiscalElectronica")
      allow(id_doc).to receive(:respond_to?).with(:encf).and_return(false)
      allow(id_doc).to receive(:respond_to?).with(:tipoeCF).and_return(false)
      encabezado = double("encabezado", id_doc: id_doc, emisor: emisor)
      ecf = double("ecf", encabezado: encabezado)

      expect { client.send_ecf(ecf) }.to raise_error(ArgumentError, /encf/)
    end

    it "raises error for unknown tipoeCF" do
      client = described_class.new
      emisor = double(rnc_emisor: "131460941")
      id_doc = double(tipoe_cf: "UnknownType", encf: "E310000051630")
      encabezado = double(id_doc: id_doc, emisor: emisor)
      ecf = double(encabezado: encabezado)

      expect { client.send_ecf(ecf) }.to raise_error(ArgumentError, /Unknown/)
    end
  end

  describe "company operations" do
    it "delegates get_company_by_rnc to company_api" do
      client = described_class.new
      expect(client.company_api).to receive(:get_company_by_rnc).with("123456789").and_return(:company)
      expect(client.get_company_by_rnc("123456789")).to eq(:company)
    end

    it "delegates get_companies to company_api" do
      client = described_class.new
      expect(client.company_api).to receive(:get_companies).with(hash_including(page: 1, limit: 10)).and_return(:companies)
      expect(client.get_companies(page: 1, limit: 10)).to eq(:companies)
    end

    it "delegates upsert_company to company_api" do
      client = described_class.new
      body = double("UpsertCompanyRequest")
      expect(client.company_api).to receive(:upsert_company).with(body).and_return(:result)
      expect(client.upsert_company(body)).to eq(:result)
    end

    it "delegates delete_company to company_api" do
      client = described_class.new
      expect(client.company_api).to receive(:delete_company).with("123456789").and_return(:result)
      expect(client.delete_company("123456789")).to eq(:result)
    end
  end

  describe "certificate operations" do
    it "delegates get_certificate to company_api" do
      client = described_class.new
      expect(client.company_api).to receive(:get_current_certificate).with("123456789").and_return(:cert)
      expect(client.get_certificate("123456789")).to eq(:cert)
    end

  end

  describe "ECF query operations" do
    it "delegates query_ecf to ecf_api" do
      client = described_class.new
      expect(client.ecf_api).to receive(:query_ecf).with("131460941", "E310000051630", {}).and_return(:result)
      expect(client.query_ecf("131460941", "E310000051630")).to eq(:result)
    end

    it "delegates search_ecfs to ecf_api" do
      client = described_class.new
      expect(client.ecf_api).to receive(:search_ecfs).with("131460941", hash_including(page: 1)).and_return(:result)
      expect(client.search_ecfs("131460941", page: 1)).to eq(:result)
    end

    it "delegates get_ecf_by_id with rnc and id" do
      client = described_class.new
      expect(client.ecf_api).to receive(:get_ecf_by_id).with("131460941", "msg_123").and_return(:result)
      expect(client.get_ecf_by_id("131460941", "msg_123")).to eq(:result)
    end
  end

  describe "anulación rangos" do
    it "delegates anulacion_rangos with rnc and body" do
      client = described_class.new
      body = double("AnulacionRequest")
      expect(client.ecf_api).to receive(:anulacion_rangos).with("131460941", body).and_return(:result)
      expect(client.anulacion_rangos("131460941", body)).to eq(:result)
    end
  end

  describe "firmar semilla" do
    it "delegates firmar_semilla with rnc and body" do
      client = described_class.new
      body = double("xml_body")
      expect(client.ecf_api).to receive(:firmar_semilla).with("131460941", body).and_return(:result)
      expect(client.firmar_semilla("131460941", body)).to eq(:result)
    end
  end

  describe "aprobación comercial" do
    it "delegates aprobacion_comercial with message_id and body" do
      client = described_class.new
      body = double("SendAcecfRequest")
      expect(client.recepcion_api).to receive(:aprobacion_comercial).with("msg_123", body).and_return(:result)
      expect(client.aprobacion_comercial("msg_123", body)).to eq(:result)
    end
  end

  describe "DGII operations" do
    it "delegates consulta_estado to dgii_api" do
      client = described_class.new
      expect(client.dgii_api).to receive(:consulta_estado)
        .with("101001010", "101001010", "E310000051630", "131880681", "ABC123")
        .and_return(:result)
      expect(client.consulta_estado("101001010", "101001010", "E310000051630", "131880681", "ABC123")).to eq(:result)
    end

    it "delegates consulta_rfce with codigo_seguridad" do
      client = described_class.new
      expect(client.dgii_api).to receive(:consulta_rfce)
        .with("101001010", "101001010", "E310000051630", "SEC123")
        .and_return(:result)
      expect(client.consulta_rfce("101001010", "101001010", "E310000051630", "SEC123")).to eq(:result)
    end
  end
end
