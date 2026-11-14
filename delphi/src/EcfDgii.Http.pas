unit EcfDgii.Http;

interface

uses
  System.SysUtils, System.Classes, System.JSON, System.Net.URLClient,
  System.Net.HttpClient, EcfDgii.Types;

type
  // Repeated names are supported for array query parameters (Rncs, Encfs, etc.).
  TEcfQuery = TArray<TNameValuePair>;

  TEcfHttpResponse = record
    StatusCode: Integer;
    Body: string;
  end;

  IEcfTransport = interface
    ['{C938940E-D3F3-48D7-B369-159F9C54D10A}']
    function Execute(const AMethod, AUrl, AApiKey, AContentType: string;
      ABody: TStream; ATimeoutMs: Integer): TEcfHttpResponse;
  end;

  TEcfNetTransport = class(TInterfacedObject, IEcfTransport)
  private
    FHttp: THTTPClient;
  public
    constructor Create;
    destructor Destroy; override;
    function Execute(const AMethod, AUrl, AApiKey, AContentType: string;
      ABody: TStream; ATimeoutMs: Integer): TEcfHttpResponse;
  end;

  // Synchronous. Use one instance per worker thread; the client is not thread safe.
  TEcfHttpClient = class
  private
    FApiKey: string;
    FBaseUrl: string;
    FRequestTimeoutMs: Integer;
    FTransport: IEcfTransport;
    function BuildUrl(const APath: string; const AQuery: TEcfQuery): string;
    procedure SetRequestTimeoutMs(AValue: Integer);
  protected
    function Execute(const AMethod, APath, AContentType: string;
      ABody: TStream; const AQuery: TEcfQuery; ATimeoutMs: Integer = 0): string;
    function UploadFile(const AMethod, APath, AField, AFileName, AContentType: string;
      const AFields: TEcfQuery): string;
    class procedure RequireQuery(const AQuery: TEcfQuery;
      const ANames: array of string); static;
  public
    constructor Create(const AApiKey: string = '';
      AEnvironment: TEcfEnvironment = eeTest; const ABaseUrl: string = '';
      const ATransport: IEcfTransport = nil);
    // Request bodies remain caller-owned. Caller must Free returned JSON (nil on empty).
    function RequestJson(const AMethod, APath: string; ABody: TJSONValue = nil;
      const AQuery: TEcfQuery = nil; ATimeoutMs: Integer = 0): TJSONValue;
    function RequestText(const AMethod, APath: string; ABody: TJSONValue = nil;
      const AQuery: TEcfQuery = nil; ATimeoutMs: Integer = 0): string;
    class function Encode(const AValue: string): string; static;
    class function PathSegment(const AValue: string): string; static;
    property BaseUrl: string read FBaseUrl;
    property RequestTimeoutMs: Integer read FRequestTimeoutMs write SetRequestTimeoutMs;
  end;

implementation

uses System.Net.Mime, System.RegularExpressions;

constructor TEcfNetTransport.Create;
begin
  inherited Create;
  FHttp := THTTPClient.Create;
  FHttp.HandleRedirects := False;
end;

destructor TEcfNetTransport.Destroy;
begin
  FHttp.Free;
  inherited;
end;

function TEcfNetTransport.Execute(const AMethod, AUrl, AApiKey, AContentType: string;
  ABody: TStream; ATimeoutMs: Integer): TEcfHttpResponse;
var
  Headers: TNetHeaders;
  Response: IHTTPResponse;
begin
  FHttp.ConnectionTimeout := ATimeoutMs;
  FHttp.ResponseTimeout := ATimeoutMs;
  SetLength(Headers, 3);
  Headers[0] := TNameValuePair.Create('Authorization', 'Bearer ' + AApiKey);
  Headers[1] := TNameValuePair.Create('Accept', 'application/json, application/xml, text/xml');
  Headers[2] := TNameValuePair.Create('User-Agent', 'ecf-dgii-delphi/' + ECF_SDK_VERSION);
  if AContentType <> '' then
  begin
    SetLength(Headers, 4);
    Headers[3] := TNameValuePair.Create('Content-Type', AContentType);
  end;
  // The method/URL overload is inherited from TURLClient and returns IURLResponse.
  Response := FHttp.Execute(AMethod, AUrl, ABody, nil, Headers) as IHTTPResponse;
  Result.StatusCode := Response.StatusCode;
  Result.Body := Response.ContentAsString(TEncoding.UTF8);
end;

constructor TEcfHttpClient.Create(const AApiKey: string; AEnvironment: TEcfEnvironment;
  const ABaseUrl: string; const ATransport: IEcfTransport);
begin
  inherited Create;
  FApiKey := Trim(AApiKey);
  if FApiKey = '' then FApiKey := Trim(GetEnvironmentVariable('ECF_API_KEY'));
  if (FApiKey = '') or (Pos(#13, FApiKey) > 0) or (Pos(#10, FApiKey) > 0) then
    raise EArgumentException.Create('Provide an API key or set ECF_API_KEY');
  FBaseUrl := Trim(ABaseUrl);
  if FBaseUrl = '' then FBaseUrl := EcfBaseUrl(AEnvironment);
  if not TRegEx.IsMatch(FBaseUrl, '^https?://[^/?#@\s\\]+(?:/[^?#\s\\]*)?$') then
    raise EArgumentException.Create('Base URL must be an HTTP(S) URL without credentials, query or fragment');
  while FBaseUrl[Length(FBaseUrl)] = '/' do
    Delete(FBaseUrl, Length(FBaseUrl), 1);
  FRequestTimeoutMs := 30000;
  FTransport := ATransport;
  if FTransport = nil then FTransport := TEcfNetTransport.Create;
end;

procedure TEcfHttpClient.SetRequestTimeoutMs(AValue: Integer);
begin
  if AValue <= 0 then raise EArgumentException.Create('RequestTimeoutMs must be positive');
  FRequestTimeoutMs := AValue;
end;

class function TEcfHttpClient.Encode(const AValue: string): string;
var
  B: Byte;
begin
  Result := '';
  for B in TEncoding.UTF8.GetBytes(AValue) do
    if ((B >= Ord('a')) and (B <= Ord('z'))) or
       ((B >= Ord('A')) and (B <= Ord('Z'))) or
       ((B >= Ord('0')) and (B <= Ord('9'))) or
       (B = Ord('-')) or (B = Ord('_')) or (B = Ord('.')) or (B = Ord('~')) then
      Result := Result + Char(B)
    else
      Result := Result + '%' + IntToHex(B, 2);
end;

class function TEcfHttpClient.PathSegment(const AValue: string): string;
begin
  if (Trim(AValue) = '') or (AValue = '.') or (AValue = '..') then
    raise EArgumentException.Create('Path parameters must be nonempty and cannot be dot segments');
  Result := Encode(AValue);
end;

function TEcfHttpClient.BuildUrl(const APath: string; const AQuery: TEcfQuery): string;
var
  Pair: TNameValuePair;
  Separator: string;
begin
  if (APath = '') or (Copy(APath, 1, 1) <> '/') or
     (Copy(APath, 1, 2) = '//') or (Pos('\', APath) > 0) or
     (Pos('?', APath) > 0) or (Pos('#', APath) > 0) or
     (Pos(#13, APath) > 0) or (Pos(#10, APath) > 0) then
    raise EArgumentException.Create('Use an API path starting with / and pass query parameters separately');
  Result := FBaseUrl + APath;
  Separator := '?';
  for Pair in AQuery do
  begin
    Result := Result + Separator + Encode(Pair.Name) + '=' + Encode(Pair.Value);
    Separator := '&';
  end;
end;

class procedure TEcfHttpClient.RequireQuery(const AQuery: TEcfQuery;
  const ANames: array of string);
var
  Name: string;
  Pair: TNameValuePair;
  Found: Boolean;
begin
  for Name in ANames do
  begin
    Found := False;
    for Pair in AQuery do
      if (Pair.Name = Name) and (Pair.Value <> '') then Found := True;
    if not Found then
      raise EArgumentException.Create('Missing query parameter: ' + Name);
  end;
end;

function TEcfHttpClient.Execute(const AMethod, APath, AContentType: string;
  ABody: TStream; const AQuery: TEcfQuery; ATimeoutMs: Integer): string;
var
  Response: TEcfHttpResponse;
begin
  if ATimeoutMs <= 0 then ATimeoutMs := FRequestTimeoutMs;
  Response := FTransport.Execute(AMethod, BuildUrl(APath, AQuery), FApiKey,
    AContentType, ABody, ATimeoutMs);
  if (Response.StatusCode < 200) or (Response.StatusCode >= 300) then
    raise EEcfHttpError.Create(Response.StatusCode, Response.Body);
  Result := Response.Body;
end;

function TEcfHttpClient.RequestText(const AMethod, APath: string; ABody: TJSONValue;
  const AQuery: TEcfQuery; ATimeoutMs: Integer): string;
var
  Stream: TStringStream;
begin
  if ABody = nil then
    Exit(Execute(AMethod, APath, '', nil, AQuery, ATimeoutMs));
  Stream := TStringStream.Create(ABody.ToJSON, TEncoding.UTF8);
  try
    Result := Execute(AMethod, APath, 'application/json; charset=utf-8', Stream,
      AQuery, ATimeoutMs);
  finally
    Stream.Free;
  end;
end;

function TEcfHttpClient.RequestJson(const AMethod, APath: string; ABody: TJSONValue;
  const AQuery: TEcfQuery; ATimeoutMs: Integer): TJSONValue;
var
  Text: string;
begin
  Text := RequestText(AMethod, APath, ABody, AQuery, ATimeoutMs);
  if Trim(Text) = '' then Exit(nil);
  Result := TJSONObject.ParseJSONValue(Text);
  if Result = nil then raise EEcfProtocolError.Create('API returned invalid JSON');
end;

function TEcfHttpClient.UploadFile(const AMethod, APath, AField, AFileName,
  AContentType: string; const AFields: TEcfQuery): string;
var
  Form: TMultipartFormData;
  Stream: TStream;
  Pair: TNameValuePair;
begin
  Form := TMultipartFormData.Create;
  try
    Form.AddFile(AField, AFileName, AContentType);
    for Pair in AFields do Form.AddField(Pair.Name, Pair.Value);
    // Finalize the boundary and rewind before sending the complete multipart body.
    Stream := Form.Stream;
    Stream.Position := 0;
    Result := Execute(AMethod, APath, Form.MimeTypeHeader, Stream, nil);
  finally
    Form.Free;
  end;
end;

end.
