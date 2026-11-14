import test from 'node:test';
import assert from 'node:assert/strict';
import { validateRelease } from '../scripts/check-release.mjs';

const manifest = {
  name: 'ecf-dgii-delphi', version: '1.0.0', mainsrc: 'delphi/src/',
  browsingpath: 'delphi/src/', license: 'Apache-2.0', projects: [], dependencies: {},
};
const source = "const ECF_SDK_VERSION = '1.0.0';";

test('branch builds and matching Delphi releases are accepted', () => {
  assert.equal(validateRelease(source, manifest), '1.0.0');
  assert.equal(validateRelease(source, manifest, 'delphi-v1.0.0'), '1.0.0');
});

test('a release cannot publish a differently versioned or unrelated package', () => {
  for (const tag of ['delphi-v2.0.0', 'dotnet-v1.0.0', 'v1.0.0', 'delphi-v1.0.0-beta.1', 'delphi-v1.0.0\n']) {
    assert.throws(() => validateRelease(source, manifest, tag), /Release tag/);
  }
  assert.throws(() => validateRelease(source, { ...manifest, version: '2.0.0' }), /does not match/);
});

test('invalid versions and Boss source paths fail before packaging', () => {
  for (const version of ['01.0.0', '1.0', '1.0.0-beta.1', '1.0.0\n', '']) {
    assert.throws(() => validateRelease(`ECF_SDK_VERSION = '${version}';`, { ...manifest, version }));
  }
  assert.throws(() => validateRelease(source, { ...manifest, mainsrc: 'src/' }), /Boss manifest/);
  assert.throws(() => validateRelease(source, { ...manifest, projects: ['unrelated.dproj'] }), /Boss manifest/);
});
