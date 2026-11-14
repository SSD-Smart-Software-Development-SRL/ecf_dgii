#!/usr/bin/env bash
# Create the source archive and checksum published by publish-delphi.yml.
set -euo pipefail
sdk_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
node "$sdk_root/scripts/check-release.mjs"
sdk_version="$(sed -n "s/.*ECF_SDK_VERSION = '\([^']*\)';/\1/p" "$sdk_root/src/EcfDgii.Types.pas")"
[[ "$sdk_version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo 'Invalid SDK version' >&2; exit 1; }
sdk_stage="$(mktemp -d)"
trap 'rm -rf "$sdk_stage"' EXIT
sdk_name="ecf-dgii-delphi-$sdk_version"
mkdir -p "$sdk_stage/$sdk_name" "$sdk_root/dist"
cp -R "$sdk_root/src" "$sdk_root/examples" "$sdk_root/tests" "$sdk_root/scripts" "$sdk_stage/$sdk_name/"
cp "$sdk_root/EcfDgii.dpk" "$sdk_root/README.md" "$sdk_root/PUBLISHING.md" "$sdk_root/LICENSE" "$sdk_root/logo.png" "$sdk_root/openapi-v1.json" "$sdk_stage/$sdk_name/"
node --input-type=module - "$sdk_root/../boss.json" "$sdk_stage/$sdk_name/boss.json" <<'JS'
import { readFileSync, writeFileSync } from 'node:fs';
const manifest = JSON.parse(readFileSync(process.argv[2], 'utf8'));
manifest.mainsrc = 'src/';
manifest.browsingpath = 'src/';
writeFileSync(process.argv[3], JSON.stringify(manifest, null, 2) + '\n');
JS
# Never copy build output or credentials into the source distribution.
(cd "$sdk_stage" && zip -q -r "$sdk_name.zip" "$sdk_name" -x '*.dcu' '*.exe' '*.bpl' '*.dcp' '*.local' '*.identcache' '*.stat' '*/__history/*' '*/__recovery/*')
mv "$sdk_stage/$sdk_name.zip" "$sdk_root/dist/$sdk_name.zip"
node --input-type=module - "$sdk_root/dist/$sdk_name.zip" <<'JS'
import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';
import { basename } from 'node:path';
const path = process.argv[2];
const digest = createHash('sha256').update(readFileSync(path)).digest('hex');
writeFileSync(path + '.sha256', `${digest}  ${basename(path)}\n`);
JS
echo "$sdk_root/dist/$sdk_name.zip"
