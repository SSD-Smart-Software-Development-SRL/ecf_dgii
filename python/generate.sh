#!/usr/bin/env bash
# Regenerate the Python SDK from the OpenAPI spec.
# Requires: pipx install openapi-python-client
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

SPEC_PATH="../java/api/openapi.yaml"
CONFIG_PATH="openapi-config.yaml"
GENERATED_DIR="ecf_dgii/generated"

echo "Removing old generated code..."
rm -rf "$GENERATED_DIR"
rm -rf ecf_dgii_generated

echo "Generating Python SDK from $SPEC_PATH..."
openapi-python-client generate \
  --path "$SPEC_PATH" \
  --config "$CONFIG_PATH" \
  --meta none

echo "Moving generated code into package..."
mv ecf_dgii_generated "$GENERATED_DIR"

echo "Done. Generated code is in $GENERATED_DIR/"
