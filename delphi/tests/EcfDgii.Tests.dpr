program EcfDgiiTests;

{$APPTYPE CONSOLE}

uses
  System.SysUtils, System.Classes, System.JSON, System.IOUtils,
  System.Net.URLClient, System.Generics.Collections,
  EcfDgii.Types, EcfDgii.Http, EcfDgii.Client;

type
  TRecordedRequest = record
    Method, Url, ApiKey, ContentType, Body: string;
    TimeoutMs: Integer;
  end;

  TFakeTransport = class(TInterfacedObject, IEcfTransport)
  public
    Responses: TQueue<TEcfHttpResponse>;
    Requests: TList<TRecordedRequest>;
    constructor Create;
    destructor Destroy; override;
    procedure Add(AStatus: Integer; const ABody: string);
    function Execute(const AMethod, AUrl, AApiKey, AContentType: string;
      ABody: TStream; ATimeoutMs: Integer): TEcfHttpResponse;
  end;

  TTestClient = class(TEcfClient)
  public
    Clock: Int64;
    Sleeps: TArray<Integer>;
    function NowMs: Int64; override;
    procedure WaitMs(ADelayMs: Integer); override;
  end;

procedure Check(ACondition: Boolean; const AMessage: string);
begin
  if not ACondition then raise Exception.Create(AMessage);
end;

procedure ExpectError(AClass: ExceptClass; const AAction: TProc);
begin
  try
    AAction();
  except
    on E: Exception do
    begin
      if not E.InheritsFrom(AClass) then raise;
      Exit;
    end;
  end;
  raise Exception.Create('Expected ' + AClass.ClassName);
end;

constructor TFakeTransport.Create;
begin
  inherited;
  Responses := TQueue<TEcfHttpResponse>.Create;
  Requests := TList<TRecordedRequest>.Create;
end;

destructor TFakeTransport.Destroy;
begin
  Requests.Free;
  Responses.Free;
  inherited;
end;

procedure TFakeTransport.Add(AStatus: Integer; const ABody: string);
var R: TEcfHttpResponse;
begin
  R.StatusCode := AStatus;
  R.Body := ABody;
  Responses.Enqueue(R);
end;

function TFakeTransport.Execute(const AMethod, AUrl, AApiKey, AContentType: string;
  ABody: TStream; ATimeoutMs: Integer): TEcfHttpResponse;
var
  Request: TRecordedRequest;
  Bytes: TBytes;
begin
  Request.Method := AMethod;
  Request.Url := AUrl;
  Request.ApiKey := AApiKey;
  Request.ContentType := AContentType;
  Request.TimeoutMs := ATimeoutMs;
  if ABody <> nil then
  begin
    SetLength(Bytes, ABody.Size - ABody.Position);
    if Length(Bytes) > 0 then ABody.ReadBuffer(Bytes[0], Length(Bytes));
    Request.Body := TEncoding.UTF8.GetString(Bytes);
  end;
  Requests.Add(Request);
  Check(Responses.Count > 0, 'Unexpected HTTP request');
  Result := Responses.Dequeue;
end;

function TTestClient.NowMs: Int64;
begin
  Result := Clock;
end;

procedure TTestClient.WaitMs(ADelayMs: Integer);
begin
  SetLength(Sleeps, Length(Sleeps) + 1);
  Sleeps[High(Sleeps)] := ADelayMs;
  Inc(Clock, ADelayMs);
end;

function Invoice(const AType: string = 'FacturaDeCreditoFiscalElectronica'): TJSONObject;
begin
  Result := TJSONObject.ParseJSONValue(
    '{"encabezado":{"idDoc":{"tipoeCF":"' + AType + '","encf":"E310000000001"},' +
    '"emisor":{"rncEmisor":"131000000"}},"detallesItems":[]}') as TJSONObject;
end;

function FastOptions: TEcfPollingOptions;
begin
  Result := TEcfPollingOptions.Default;
  Result.InitialDelayMs := 10;
  Result.MaxDelayMs := 25;
  Result.MaxAttempts := 6;
  Result.TimeoutMs := 100;
end;

procedure TestRoutesAndOwnership;
const
  Types: array[0..9] of string = ('FacturaDeCreditoFiscalElectronica',
    'FacturaDeConsumoElectronica', 'NotaDeDebitoElectronica', 'NotaDeCreditoElectronica',
    'ComprasElectronico', 'GastosMenoresElectronico', 'RegimenesEspecialesElectronico',
    'GubernamentalElectronico', 'ComprobanteDeExportacionesElectronico',
    'ComprobanteParaPagosAlExteriorElectronico');
  Codes: array[0..9] of string = ('31', '32', '33', '34', '41', '43', '44', '45', '46', '47');
var
  Fake: TFakeTransport;
  Client: TTestClient;
  Payload: TJSONObject;
  R: TEcfResponse;
  I: Integer;
begin
  Fake := TFakeTransport.Create;
  Client := TTestClient.Create('test-key', eeCert, '', Fake);
  try
    for I := 0 to High(Types) do
    begin
      Fake.Add(200, '{"messageId":"m1","progress":"New"}');
      Payload := Invoice(Types[I]);
      try
        R := Client.SubmitEcf(Payload);
        Check(R.MessageId = 'm1', 'Submission messageId');
        Check(Fake.Requests[I].Method = 'POST', 'Submit uses POST');
        Check(Fake.Requests[I].Url = 'https://api.cert.ecfx.ssd.com.do/ecf/' + Codes[I], 'Route');
        Check(Fake.Requests[I].ApiKey = 'test-key', 'Token passed to transport');
        Check(Fake.Requests[I].Body = Payload.ToJSON, 'Input ownership or serialization');
      finally
        Payload.Free;
      end;
    end;
    ExpectError(EArgumentException, procedure begin Client.RouteForType('invalid'); end);
  finally
    Client.Free;
  end;
end;

procedure TestPollingMatchesMessage;
var
  Fake: TFakeTransport;
  Client: TTestClient;
  Payload: TJSONObject;
  R: TEcfResponse;
begin
  Fake := TFakeTransport.Create;
  Client := TTestClient.Create('key', eeTest, '', Fake);
  Payload := Invoice;
  try
    Fake.Add(200, '{"messageId":"m1","progress":"New"}');
    Fake.Add(404, 'not visible');
    Fake.Add(200, '[]');
    Fake.Add(200, '[{"messageId":"old","progress":"Finished"}]');
    Fake.Add(200, '[{"messageId":"m1","progress":"Processing"}]');
    Fake.Add(200, '[{"messageId":"old","progress":"Error"},' +
      '{"messageId":"M1","progress":"Finished","estatus":"Rechazado",' +
      '"montoTotal":118.5,"secuenciaUtilizada":false,"codSec":null}]');
    R := Client.SendEcf(Payload, FastOptions);
    Check(R.MessageId = 'M1', 'Must correlate messageId, including GUID case');
    Check(R.Estatus = 'Rechazado', 'Finished does not imply accepted');
    Check(R.HasMontoTotal and (Abs(R.MontoTotal - 118.5) < 0.00001), 'Numeric amount');
    Check(R.HasSecuenciaUtilizada and not R.SecuenciaUtilizada, 'Nullable boolean');
    Check(R.CodSec = '', 'Nullable string');
    Check((Length(Client.Sleeps) = 4) and (Client.Sleeps[0] = 10) and
      (Client.Sleeps[1] = 20) and (Client.Sleeps[2] = 25) and (Client.Sleeps[3] = 25), 'Backoff cap');
    Check(Fake.Requests.Count = 6, 'One POST plus five GETs');
    Check(Fake.Requests[5].TimeoutMs = 20, 'Request timeout follows remaining budget');
  finally
    Payload.Free;
    Client.Free;
  end;
end;

procedure TestFailuresAndBounds;
var
  Fake: TFakeTransport;
  Client: TTestClient;
  Payload: TJSONObject;
  Options: TEcfPollingOptions;
  Before: Integer;
begin
  Fake := TFakeTransport.Create;
  Client := TTestClient.Create('key', eeTest, '', Fake);
  Payload := Invoice;
  try
    Options := FastOptions;
    Options.MaxAttempts := 0;
    ExpectError(EArgumentException, procedure begin Client.SendEcf(Payload, Options); end);
    Check(Fake.Requests.Count = 0, 'Invalid options must not submit');
    Fake.Add(200, '{"messageId":"m1","progress":"Error","errors":"invalid invoice"}');
    try
      Client.SubmitEcf(Payload);
      raise Exception.Create('Expected processing error');
    except
      on E: EEcfProcessingError do Check(E.Response.Errors = 'invalid invoice', 'Keep error response');
    end;
    Fake.Add(401, '{"detail":"sensitive"}');
    try
      Client.PollEcf('rnc', 'encf', 'm1', FastOptions);
      raise Exception.Create('Expected HTTP error');
    except
      on E: EEcfHttpError do
      begin
        Check(E.StatusCode = 401, 'HTTP status');
        Check(Pos('sensitive', E.ResponseBody) > 0, 'Preserve response details');
        Check(Pos('sensitive', E.Message) = 0, 'Default message must not contain response');
      end;
    end;
    Fake.Add(200, 'not json');
    ExpectError(EEcfProtocolError, procedure begin Client.SubmitEcf(Payload); end);
    Fake.Add(200, '{}');
    ExpectError(EEcfProtocolError, procedure begin Client.SubmitEcf(Payload); end);
    Fake.Add(200, '{}');
    ExpectError(EEcfProtocolError, procedure begin Client.PollEcf('r', 'e', 'm1', FastOptions); end);
    Options := FastOptions;
    Options.MaxAttempts := 2;
    Fake.Add(200, '[]');
    Fake.Add(200, '[]');
    Before := Fake.Requests.Count;
    ExpectError(EEcfPollingAttemptsExceeded, procedure begin Client.PollEcf('r', 'e', 'm1', Options); end);
    Check(Fake.Requests.Count - Before = 2, 'Exact attempt bound');
    Options := FastOptions;
    Options.TimeoutMs := 5;
    Fake.Add(200, '[]');
    Before := Fake.Requests.Count;
    ExpectError(EEcfPollingTimeout, procedure begin Client.PollEcf('r', 'e', 'm1', Options); end);
    Check(Fake.Requests.Count - Before = 1, 'No requests after timeout');
    Check(Client.Sleeps[High(Client.Sleeps)] = 5, 'Sleep limited by timeout');
    ExpectError(EArgumentException, procedure begin Client.PollEcf('r', 'e', '', FastOptions); end);
  finally
    Payload.Free;
    Client.Free;
  end;
end;

procedure TestEncodingAndHelpers;
var
  Fake: TFakeTransport;
  Client: TTestClient;
  Value: TJSONValue;
begin
  Fake := TFakeTransport.Create;
  Client := TTestClient.Create('key', eeProd, 'https://example.invalid/api/', Fake);
  try
    Fake.Add(200, '[]');
    Value := Client.GetCompanies(TEcfQuery.Create(
      TNameValuePair.Create('Names', 'a & b'), TNameValuePair.Create('Names', 'c+d')));
    Value.Free;
    Check(Fake.Requests[0].Url = 'https://example.invalid/api/company?Names=a%20%26%20b&Names=c%2Bd', 'Repeated encoded query');
    Fake.Add(200, '[]');
    Value := Client.QueryEcf('a/b', 'e?f');
    Value.Free;
    Check(Fake.Requests[1].Url = 'https://example.invalid/api/ecf/a%2Fb/e%3Ff', 'Encoded path');
    Fake.Add(204, '');
    Value := Client.DeleteCompany('rnc');
    Check(Value = nil, '204 returns nil');
    ExpectError(EArgumentException, procedure begin Client.ConsultaResultado('rnc'); end);
    ExpectError(EArgumentException, procedure begin Client.GetCompanyByRnc('..'); end);
    ExpectError(EArgumentException, procedure begin Client.RequestJson('GET', '//other.example'); end);
    Check(Fake.Requests.Count = 3, 'Invalid calls must not reach transport');
  finally
    Client.Free;
  end;
end;

procedure TestMultipart;
var
  Fake: TFakeTransport;
  Client: TTestClient;
  FileName, Output: string;
begin
  FileName := TPath.GetTempFileName;
  try
    TFile.WriteAllText(FileName, 'fake-certificate-data', TEncoding.UTF8);
    Fake := TFakeTransport.Create;
    Client := TTestClient.Create('key', eeTest, '', Fake);
    try
      Fake.Add(204, '');
      Output := Client.UpdateCertificateCompany('rnc', FileName, 'test-password');
      Check(Output = '', 'Empty upload response');
      Check(Fake.Requests[0].Method = 'PUT', 'Certificate upload is PUT');
      Check(Pos('multipart/form-data; boundary=', Fake.Requests[0].ContentType) = 1, 'Boundary header');
      Check(Pos('name="certificate"', Fake.Requests[0].Body) > 0, 'Certificate field');
      Check(Pos('name="password"', Fake.Requests[0].Body) > 0, 'Password field');
      Check(Pos('fake-certificate-data', Fake.Requests[0].Body) > 0, 'File body');
      Check(Pos('test-password', Fake.Requests[0].Body) > 0, 'Password body');
      Fake.Add(200, '<Semilla>signed</Semilla>');
      Output := Client.FirmarSemilla('rnc', FileName);
      Check(Output = '<Semilla>signed</Semilla>', 'XML response is not parsed as JSON');
      Check(Pos('name="xml"', Fake.Requests[1].Body) > 0, 'XML field');
    finally
      Client.Free;
    end;
  finally
    TFile.Delete(FileName);
  end;
end;

begin
  ReportMemoryLeaksOnShutdown := True;
  try
    TestRoutesAndOwnership;
    TestPollingMatchesMessage;
    TestFailuresAndBounds;
    TestEncodingAndHelpers;
    TestMultipart;
    Writeln('PASS: 5 offline suites (routing, polling, failures, encoding, multipart)');
  except
    on E: Exception do
    begin
      Writeln('FAIL: ', E.ClassName, ': ', E.Message);
      ExitCode := 1;
    end;
  end;
end.
