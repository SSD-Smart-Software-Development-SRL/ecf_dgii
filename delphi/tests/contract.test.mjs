import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
import { execFileSync } from 'node:child_process';

const root = fileURLToPath(new URL('../', import.meta.url));
const specPath = process.env.SPEC_PATH || resolve(root, 'openapi-v1.json');
const spec = JSON.parse(readFileSync(specPath, 'utf8'));

test('checked-in Delphi methods match every operation in the API contract', () => {
  execFileSync(process.execPath, [resolve(root, 'scripts/generate.mjs'), '--check'], {
    env: { ...process.env, SPEC_PATH: specPath },
  });
});

test('high-level ECF routing covers the contract enum and all submission paths', () => {
  const source = readFileSync(resolve(root, 'src/EcfDgii.Client.pas'), 'utf8');
  const routes = [...source.matchAll(/if ATipoEcf = '([^']+)' then Exit\('([^']+)'\)/g)];
  assert.deepEqual(routes.map(r => r[1]).sort(), [...spec.components.schemas.TipoeCFType.enum].sort());
  const paths = Object.entries(spec.paths)
    .filter(([path, item]) => /^\/ecf\/\d{2}$/.test(path) && item.post).map(([path]) => path);
  assert.deepEqual(routes.map(r => r[2]).sort(), paths.sort());
  // Enum/route pairing is a domain codebook, independent from the Pascal implementation.
  assert.deepEqual(Object.fromEntries(routes.map(r => [r[1], r[2].slice(-2)])), {
    FacturaDeCreditoFiscalElectronica: '31', FacturaDeConsumoElectronica: '32',
    NotaDeDebitoElectronica: '33', NotaDeCreditoElectronica: '34', ComprasElectronico: '41',
    GastosMenoresElectronico: '43', RegimenesEspecialesElectronico: '44',
    GubernamentalElectronico: '45', ComprobanteDeExportacionesElectronico: '46',
    ComprobanteParaPagosAlExteriorElectronico: '47',
  });
});

test('multipart fields and response properties still match the handwritten client', () => {
  const upload = spec.paths['/company/{rnc}/certificate'].put.requestBody.content['multipart/form-data'].schema;
  assert.deepEqual([...upload.required].sort(), ['certificate', 'password']);
  const seed = spec.paths['/ecf/FirmarSemilla/{rnc}'].post.requestBody.content['multipart/form-data'].schema;
  assert.deepEqual(seed.required, ['xml']);
  const source = readFileSync(resolve(root, 'src/EcfDgii.Types.pas'), 'utf8');
  for (const [, field] of source.matchAll(/(?:JsonText\(Obj, |Obj.GetValue\()'([^']+)'/g)) {
    assert.ok(spec.components.schemas.EcfResponse.properties[field], `Missing response property ${field}`);
  }
  assert.ok(spec.components.schemas.EcfProgress.enum.includes('Finished'));
  assert.ok(spec.components.schemas.EcfProgress.enum.includes('Error'));
});
