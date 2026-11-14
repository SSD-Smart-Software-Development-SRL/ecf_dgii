unit EcfDgii.Types;

interface

uses
  System.SysUtils, System.JSON;

const
  ECF_SDK_VERSION = '1.0.0';

type
  TEcfEnvironment = (eeTest, eeCert, eeProd);

  TEcfPollingOptions = record
    InitialDelayMs: Integer;
    MaxDelayMs: Integer;
    MaxAttempts: Integer;
    BackoffMultiplier: Double;
    TimeoutMs: Integer;
    class function Default: TEcfPollingOptions; static;
    procedure Validate;
  end;

  // Managed record: no Free required. RawJson preserves all response fields.
  TEcfResponse = record
    MessageId: string;
    Encf: string;
    RncEmisor: string;
    Progress: string;
    Estatus: string;
    CodSec: string;
    ImpresionUrl: string;
    FechaFirma: string;
    Mensaje: string;
    Errors: string;
    MontoTotal: Double;
    HasMontoTotal: Boolean;
    SecuenciaUtilizada: Boolean;
    HasSecuenciaUtilizada: Boolean;
    RawJson: string;
    class function FromJson(const AValue: TJSONValue): TEcfResponse; static;
    function IsTerminal: Boolean;
  end;

  EEcfError = class(Exception);
  EEcfProtocolError = class(EEcfError);
  EEcfPollingTimeout = class(EEcfError);
  EEcfPollingAttemptsExceeded = class(EEcfError);

  EEcfHttpError = class(EEcfError)
  private
    FStatusCode: Integer;
    FResponseBody: string;
  public
    constructor Create(AStatusCode: Integer; const AResponseBody: string);
    property StatusCode: Integer read FStatusCode;
    property ResponseBody: string read FResponseBody;
  end;

  EEcfProcessingError = class(EEcfError)
  private
    FResponse: TEcfResponse;
  public
    constructor Create(const AResponse: TEcfResponse);
    property Response: TEcfResponse read FResponse;
  end;

function EcfBaseUrl(AEnvironment: TEcfEnvironment): string;
function JsonText(const AObject: TJSONObject; const AName: string): string;

implementation

uses System.Math;

function EcfBaseUrl(AEnvironment: TEcfEnvironment): string;
begin
  case AEnvironment of
    eeTest: Result := 'https://api.test.ecfx.ssd.com.do';
    eeCert: Result := 'https://api.cert.ecfx.ssd.com.do';
    eeProd: Result := 'https://api.prod.ecfx.ssd.com.do';
  else
    raise EArgumentException.Create('Unknown ECF environment');
  end;
end;

function JsonText(const AObject: TJSONObject; const AName: string): string;
var
  Value: TJSONValue;
begin
  Result := '';
  if AObject = nil then Exit;
  Value := AObject.GetValue(AName);
  if (Value <> nil) and not (Value is TJSONNull) then
    Result := Value.Value;
end;

class function TEcfPollingOptions.Default: TEcfPollingOptions;
begin
  Result.InitialDelayMs := 1000;
  Result.MaxDelayMs := 30000;
  Result.MaxAttempts := 60;
  Result.BackoffMultiplier := 2;
  Result.TimeoutMs := 120000;
end;

procedure TEcfPollingOptions.Validate;
begin
  if (InitialDelayMs <= 0) or (MaxDelayMs < InitialDelayMs) or
     (MaxAttempts <= 0) or (TimeoutMs <= 0) or
     IsNan(BackoffMultiplier) or IsInfinite(BackoffMultiplier) or
     (BackoffMultiplier < 1) then
    raise EArgumentException.Create('Invalid polling options');
end;

class function TEcfResponse.FromJson(const AValue: TJSONValue): TEcfResponse;
var
  Obj: TJSONObject;
  Value: TJSONValue;
begin
  Result := System.Default(TEcfResponse);
  if not (AValue is TJSONObject) then
    raise EEcfProtocolError.Create('Expected an ECF response object');
  Obj := TJSONObject(AValue);
  Result.RawJson := Obj.ToJSON;
  Result.MessageId := JsonText(Obj, 'messageId');
  Result.Encf := JsonText(Obj, 'encf');
  Result.RncEmisor := JsonText(Obj, 'rncEmisor');
  Result.Progress := JsonText(Obj, 'progress');
  Result.Estatus := JsonText(Obj, 'estatus');
  Result.CodSec := JsonText(Obj, 'codSec');
  Result.ImpresionUrl := JsonText(Obj, 'impresionUrl');
  Result.FechaFirma := JsonText(Obj, 'fechaFirma');
  Result.Mensaje := JsonText(Obj, 'mensaje');
  Result.Errors := JsonText(Obj, 'errors');
  Value := Obj.GetValue('montoTotal');
  Result.HasMontoTotal := (Value <> nil) and not (Value is TJSONNull);
  if Result.HasMontoTotal then
    if not TryStrToFloat(Value.Value, Result.MontoTotal, TFormatSettings.Invariant) or
       IsNan(Result.MontoTotal) or IsInfinite(Result.MontoTotal) then
      raise EEcfProtocolError.Create('Invalid montoTotal in ECF response');
  Value := Obj.GetValue('secuenciaUtilizada');
  Result.HasSecuenciaUtilizada := (Value <> nil) and not (Value is TJSONNull);
  if Result.HasSecuenciaUtilizada then
  begin
    if not (Value is TJSONBool) then
      raise EEcfProtocolError.Create('Invalid secuenciaUtilizada in ECF response');
    Result.SecuenciaUtilizada := TJSONBool(Value).AsBoolean;
  end;
end;

function TEcfResponse.IsTerminal: Boolean;
begin
  Result := (Progress = 'Finished') or (Progress = 'Error');
end;

constructor EEcfHttpError.Create(AStatusCode: Integer; const AResponseBody: string);
begin
  // Keep potentially sensitive response details out of the default log message.
  inherited CreateFmt('ECF API returned HTTP %d', [AStatusCode]);
  FStatusCode := AStatusCode;
  FResponseBody := AResponseBody;
end;

constructor EEcfProcessingError.Create(const AResponse: TEcfResponse);
begin
  inherited Create('ECF processing failed; inspect Response for details');
  FResponse := AResponse;
end;

end.
