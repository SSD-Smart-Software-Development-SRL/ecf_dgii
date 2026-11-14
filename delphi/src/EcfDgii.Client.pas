unit EcfDgii.Client;

interface

uses
  System.SysUtils, System.JSON, EcfDgii.Types, EcfDgii.Http, EcfDgii.Api;

type
  TEcfClient = class(TEcfApi)
  private
    class procedure ReadIdentity(AEcf: TJSONObject;
      out ARoute, ARnc, AEncf: string); static;
    class function CheckResult(const AResponse: TEcfResponse): TEcfResponse; static;
  protected
    // Virtual timing hooks allow deterministic offline tests.
    function NowMs: Int64; virtual;
    procedure WaitMs(ADelayMs: Integer); virtual;
  public
    class function RouteForType(const ATipoEcf: string): string; static;
    // POST exactly once, return the queued response without polling.
    function SubmitEcf(AEcf: TJSONObject): TEcfResponse;
    function SendEcf(AEcf: TJSONObject): TEcfResponse; overload;
    function SendEcf(AEcf: TJSONObject;
      const AOptions: TEcfPollingOptions): TEcfResponse; overload;
    // Resume after a timeout using the saved messageId. Never resubmits the ECF.
    function PollEcf(const ARnc, AEncf, AMessageId: string): TEcfResponse; overload;
    function PollEcf(const ARnc, AEncf, AMessageId: string;
      const AOptions: TEcfPollingOptions): TEcfResponse; overload;
  end;

implementation

uses System.Classes, System.Diagnostics, System.Math;

class function TEcfClient.RouteForType(const ATipoEcf: string): string;
begin
  if ATipoEcf = 'FacturaDeCreditoFiscalElectronica' then Exit('/ecf/31');
  if ATipoEcf = 'FacturaDeConsumoElectronica' then Exit('/ecf/32');
  if ATipoEcf = 'NotaDeDebitoElectronica' then Exit('/ecf/33');
  if ATipoEcf = 'NotaDeCreditoElectronica' then Exit('/ecf/34');
  if ATipoEcf = 'ComprasElectronico' then Exit('/ecf/41');
  if ATipoEcf = 'GastosMenoresElectronico' then Exit('/ecf/43');
  if ATipoEcf = 'RegimenesEspecialesElectronico' then Exit('/ecf/44');
  if ATipoEcf = 'GubernamentalElectronico' then Exit('/ecf/45');
  if ATipoEcf = 'ComprobanteDeExportacionesElectronico' then Exit('/ecf/46');
  if ATipoEcf = 'ComprobanteParaPagosAlExteriorElectronico' then Exit('/ecf/47');
  raise EArgumentException.Create('Unknown encabezado.idDoc.tipoeCF');
end;

function RequireObject(AParent: TJSONObject; const AName: string): TJSONObject;
var
  Value: TJSONValue;
begin
  Value := AParent.GetValue(AName);
  if not (Value is TJSONObject) then
    raise EArgumentException.Create('ECF requires object: ' + AName);
  Result := TJSONObject(Value);
end;

class procedure TEcfClient.ReadIdentity(AEcf: TJSONObject;
  out ARoute, ARnc, AEncf: string);
var
  Header, IdDoc, Emisor: TJSONObject;
begin
  if AEcf = nil then raise EArgumentException.Create('ECF is required');
  Header := RequireObject(AEcf, 'encabezado');
  IdDoc := RequireObject(Header, 'idDoc');
  Emisor := RequireObject(Header, 'emisor');
  ARoute := RouteForType(JsonText(IdDoc, 'tipoeCF'));
  ARnc := JsonText(Emisor, 'rncEmisor');
  AEncf := JsonText(IdDoc, 'encf');
  PathSegment(ARnc);
  PathSegment(AEncf);
end;

class function TEcfClient.CheckResult(const AResponse: TEcfResponse): TEcfResponse;
begin
  if AResponse.Progress = 'Error' then raise EEcfProcessingError.Create(AResponse);
  Result := AResponse;
end;

function TEcfClient.SubmitEcf(AEcf: TJSONObject): TEcfResponse;
var
  Route, Rnc, Encf: string;
  Value: TJSONValue;
begin
  ReadIdentity(AEcf, Route, Rnc, Encf);
  Value := RequestJson('POST', Route, AEcf);
  try
    Result := TEcfResponse.FromJson(Value);
    if Result.MessageId = '' then
      raise EEcfProtocolError.Create('Submission response is missing messageId');
  finally
    Value.Free;
  end;
  Result := CheckResult(Result);
end;

function TEcfClient.SendEcf(AEcf: TJSONObject): TEcfResponse;
begin
  Result := SendEcf(AEcf, TEcfPollingOptions.Default);
end;

function TEcfClient.SendEcf(AEcf: TJSONObject;
  const AOptions: TEcfPollingOptions): TEcfResponse;
var
  Route, Rnc, Encf: string;
begin
  // Validate before the POST, so invalid options cannot submit a document.
  AOptions.Validate;
  ReadIdentity(AEcf, Route, Rnc, Encf);
  Result := SubmitEcf(AEcf);
  if not Result.IsTerminal then
    Result := PollEcf(Rnc, Encf, Result.MessageId, AOptions);
end;

function TEcfClient.NowMs: Int64;
begin
  Result := Trunc(TStopwatch.GetTimeStamp * (1000.0 / TStopwatch.Frequency));
end;

procedure TEcfClient.WaitMs(ADelayMs: Integer);
begin
  TThread.Sleep(ADelayMs);
end;

function TEcfClient.PollEcf(const ARnc, AEncf, AMessageId: string): TEcfResponse;
begin
  Result := PollEcf(ARnc, AEncf, AMessageId, TEcfPollingOptions.Default);
end;

function TEcfClient.PollEcf(const ARnc, AEncf, AMessageId: string;
  const AOptions: TEcfPollingOptions): TEcfResponse;
var
  Start, Remaining: Int64;
  Attempt, Delay, I: Integer;
  Path: string;
  Value: TJSONValue;
  Candidate: TEcfResponse;
begin
  AOptions.Validate;
  if Trim(AMessageId) = '' then raise EArgumentException.Create('messageId is required');
  Path := '/ecf/' + PathSegment(ARnc) + '/' + PathSegment(AEncf);
  Start := NowMs;
  Delay := AOptions.InitialDelayMs;
  for Attempt := 1 to AOptions.MaxAttempts do
  begin
    Remaining := AOptions.TimeoutMs - (NowMs - Start);
    if Remaining <= 0 then raise EEcfPollingTimeout.Create('ECF polling timed out');
    Value := nil;
    try
      try
        Value := RequestJson('GET', Path, nil, nil,
          Integer(Min(Int64(RequestTimeoutMs), Remaining)));
      except
        on E: EEcfHttpError do
          // The just-enqueued record may not be visible yet. Other failures surface.
          if E.StatusCode <> 404 then raise;
      end;
      if NowMs - Start >= AOptions.TimeoutMs then
        raise EEcfPollingTimeout.Create('ECF polling timed out');
      if Value <> nil then
      begin
        if not (Value is TJSONArray) then
          raise EEcfProtocolError.Create('Expected an array from the ECF query');
        for I := 0 to TJSONArray(Value).Count - 1 do
        begin
          Candidate := TEcfResponse.FromJson(TJSONArray(Value).Items[I]);
          // Do not return an earlier submission with the same RNC/eNCF.
          if SameText(Candidate.MessageId, AMessageId) and Candidate.IsTerminal then
            Exit(CheckResult(Candidate));
        end;
      end;
    finally
      Value.Free;
    end;
    if Attempt = AOptions.MaxAttempts then Break;
    Remaining := AOptions.TimeoutMs - (NowMs - Start);
    if Remaining <= 0 then raise EEcfPollingTimeout.Create('ECF polling timed out');
    WaitMs(Integer(Min(Int64(Delay), Remaining)));
    // Clamp as floating point before converting, avoiding integer overflow.
    Delay := Integer(Trunc(Min(Double(AOptions.MaxDelayMs),
      Delay * AOptions.BackoffMultiplier)));
  end;
  raise EEcfPollingAttemptsExceeded.Create('ECF polling exhausted MaxAttempts');
end;

end.
