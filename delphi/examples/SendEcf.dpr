program SendEcf;

{$APPTYPE CONSOLE}

uses
  System.SysUtils, System.JSON, System.IOUtils,
  EcfDgii.Types, EcfDgii.Client;

procedure Run;
var
  Client: TEcfClient;
  Payload: TJSONValue;
  Response: TEcfResponse;
begin
  if ParamCount <> 1 then
    raise EArgumentException.Create('Usage: SendEcf invoice.json (set ECF_API_KEY first)');
  Payload := TJSONObject.ParseJSONValue(TFile.ReadAllText(ParamStr(1), TEncoding.UTF8));
  try
    if not (Payload is TJSONObject) then
      raise EArgumentException.Create('The invoice file must contain a JSON object');
    Client := TEcfClient.Create('', eeTest);
    try
      // Save this messageId before polling. PollEcf can resume without another POST.
      Response := Client.SubmitEcf(TJSONObject(Payload));
      Writeln('messageId: ', Response.MessageId);
      if not Response.IsTerminal then
        Response := Client.PollEcf(
          TJSONObject(Payload).GetValue<string>('encabezado.emisor.rncEmisor'),
          TJSONObject(Payload).GetValue<string>('encabezado.idDoc.encf'),
          Response.MessageId);
      Writeln('Progress: ', Response.Progress);
      // Finished means processing completed. Always inspect the DGII status too.
      Writeln('Estatus: ', Response.Estatus);
      Writeln('CodSec: ', Response.CodSec);
      Writeln('ImpresionUrl: ', Response.ImpresionUrl);
    finally
      Client.Free;
    end;
  finally
    Payload.Free;
  end;
end;

begin
  try
    Run;
  except
    on E: Exception do
    begin
      Writeln(E.ClassName, ': ', E.Message);
      ExitCode := 1;
    end;
  end;
end.
