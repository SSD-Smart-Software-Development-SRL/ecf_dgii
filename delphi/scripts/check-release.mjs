import { appendFileSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

export function validateRelease(source, manifest, tag = '') {
  const version = source.match(/\bECF_SDK_VERSION\s*=\s*'([^']+)'\s*;/)?.[1];
  if (!version || !/^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/.test(version)) {
    throw new Error('ECF_SDK_VERSION must be a stable semantic version (X.Y.Z)');
  }
  if (manifest.version !== version) throw new Error('boss.json version does not match ECF_SDK_VERSION');
  if (manifest.name !== 'ecf-dgii-delphi' || manifest.mainsrc !== 'delphi/src/' ||
      manifest.browsingpath !== 'delphi/src/' || manifest.license !== 'Apache-2.0' ||
      !Array.isArray(manifest.projects) || manifest.projects.length !== 0 ||
      !manifest.dependencies || Object.keys(manifest.dependencies).length !== 0) {
    throw new Error('Invalid repository-root Boss manifest');
  }
  if (tag && tag !== `delphi-v${version}`) {
    throw new Error(`Release tag must be delphi-v${version}, received ${tag}`);
  }
  return version;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const root = fileURLToPath(new URL('../', import.meta.url));
  const version = validateRelease(
    readFileSync(resolve(root, 'src/EcfDgii.Types.pas'), 'utf8'),
    JSON.parse(readFileSync(resolve(root, '../boss.json'), 'utf8')),
    process.env.RELEASE_TAG || '',
  );
  if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `version=${version}\n`);
  console.log(`Delphi package version validated: ${version}`);
}
