import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { readFileSync, readdirSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateRelease } from './check-release.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
const manifest = JSON.parse(readFileSync(resolve(root, '../boss.json'), 'utf8'));
const version = validateRelease(readFileSync(resolve(root, 'src/EcfDgii.Types.pas'), 'utf8'), manifest);
const name = `ecf-dgii-delphi-${version}`;
const archive = resolve(root, `dist/${name}.zip`);
const expected = ['EcfDgii.dpk', 'LICENSE', 'README.md', 'PUBLISHING.md', 'logo.png', 'openapi-v1.json'];
for (const [directory, extension] of [['src', '.pas'], ['examples', '.dpr'], ['tests', null], ['scripts', null]]) {
  for (const file of readdirSync(resolve(root, directory))) {
    if (extension ? file.endsWith(extension) : /\.(mjs|cmd|sh|dpr)$/.test(file)) {
      expected.push(`${directory}/${file}`);
    }
  }
}
const entries = execFileSync('unzip', ['-Z1', archive], { encoding: 'utf8' }).trim().split('\n')
  .filter(path => !path.endsWith('/'));
assert.deepEqual(entries.sort(), [...expected, 'boss.json'].map(path => `${name}/${path}`).sort(),
  'Unexpected or missing archive files');
for (const path of expected) {
  const packed = execFileSync('unzip', ['-p', archive, `${name}/${path}`]);
  assert.deepEqual(packed, readFileSync(resolve(root, path)), `Archive differs from source: ${path}`);
}
const packedManifest = JSON.parse(execFileSync('unzip', ['-p', archive, `${name}/boss.json`], { encoding: 'utf8' }));
assert.deepEqual(packedManifest, { ...manifest, mainsrc: 'src/', browsingpath: 'src/' });
const digest = createHash('sha256').update(readFileSync(archive)).digest('hex');
assert.equal(readFileSync(`${archive}.sha256`, 'utf8'), `${digest}  ${name}.zip\n`);
execFileSync('unzip', ['-tq', archive]);
console.log(`Verified ${entries.length} packaged files, Boss source paths and SHA-256 checksum.`);
