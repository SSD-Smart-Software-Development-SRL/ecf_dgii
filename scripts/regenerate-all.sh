#!/usr/bin/env bash
#
# regenerate-all.sh
#
# Regenerate every language SDK in this monorepo from the canonical
# OpenAPI spec, then build each one to verify the regen.
#
# Does NOT bump versions, commit, push, or publish — those are manual.
#
# Usage:
#   ./scripts/regenerate-all.sh                  # regen all
#   ./scripts/regenerate-all.sh dotnet typescript  # regen specific SDKs
#
# Environment overrides:
#   SPEC_PATH            absolute path to ECF_DGII.EcfApi v1.json (default: sibling repo)
#   RECEPTOR_SPEC_PATH   absolute path to ECF_DGII.ReceptorApi v1.json (default: sibling repo)
#   OPENAPI_GEN_VERSION  openapi-generator JAR version for java (pinned in java/openapitools.json: 7.14.0)
#   KOTLIN_GEN_VERSION / IOS_GEN_VERSION / CPP_GEN_VERSION
#                        generator versions for kotlin/ios/cpp (default: 7.20.0 / 7.20.0 / 7.14.0)
#
# Exit code: 0 if all attempted SDKs passed; 1 if any failed (skipped does not count).
#
set -o pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

SPEC_PATH="${SPEC_PATH:-$HOME/Developer/ssd/saas_ecf_dgii/src/Apis/ECF_DGII.EcfApi/wwwroot/openapi/v1.json}"
RECEPTOR_SPEC_PATH="${RECEPTOR_SPEC_PATH:-$HOME/Developer/ssd/saas_ecf_dgii/src/Apis/ECF_DGII.ReceptorApi/wwwroot/openapi/v1.json}"
OPENAPI_GEN_VERSION="${OPENAPI_GEN_VERSION:-7.14.0}"
KOTLIN_GEN_VERSION="${KOTLIN_GEN_VERSION:-7.20.0}"
IOS_GEN_VERSION="${IOS_GEN_VERSION:-7.20.0}"
CPP_GEN_VERSION="${CPP_GEN_VERSION:-7.14.0}"
NPX_PKG="@openapitools/openapi-generator-cli@2.32.0"

PASS=()
FAIL=()
SKIP=()

step() { printf "\n==[ %s ]======================================\n" "$1"; }
ok()   { echo "  PASS: $1"; PASS+=("$1"); }
bad()  { echo "  FAIL: $1"; FAIL+=("$1"); }
skip() { echo "  SKIP: $1 ($2)"; SKIP+=("$1: $2"); }

require_spec() {
  if [[ ! -f "$SPEC_PATH" ]]; then
    echo "Spec not found at $SPEC_PATH" >&2
    echo "Set SPEC_PATH env var to the absolute path of v1.json" >&2
    exit 2
  fi
}

# The API omits null values, so nullable properties marked `required` are often
# missing; the JVM parsers reject that. Generate them from a relaxed copy.
make_relaxed_spec() {
  RELAXED_SPEC="$(mktemp -t ecf-openapi-relaxed.XXXXXX)"
  python3 "$REPO_ROOT/python/relax_spec.py" "$SPEC_PATH" "$RELAXED_SPEC" >/dev/null
}

# openapi-generator-cli ignores OPENAPI_GENERATOR_VERSION and reads the JAR
# version from ./openapitools.json; write a temporary one for the run.
pin_generator() {  # <dir> <version>; leaves an existing openapitools.json alone
  [[ -f "$1/openapitools.json" ]] && return
  printf '{ "generator-cli": { "version": "%s" } }\n' "$2" > "$1/openapitools.json"
  PINNED_DIR="$1"
}
unpin_generator() {
  [[ -n "${PINNED_DIR:-}" ]] && rm -f "$PINNED_DIR/openapitools.json"
  PINNED_DIR=""
}
cleanup() { unpin_generator; rm -f "${RELAXED_SPEC:-}"; }
trap cleanup EXIT

regen_dotnet() {
  step "dotnet (kiota)"
  command -v kiota >/dev/null || { skip "dotnet" "kiota not installed"; return; }
  command -v dotnet >/dev/null || { skip "dotnet" "dotnet not installed"; return; }
  ( cd "$REPO_ROOT" && kiota update -o .net/EcfDgii.Client/Generated --clean-output ) \
    && ( cd "$REPO_ROOT/.net" && dotnet build EcfDgii.Client/EcfDgii.Client.csproj -c Release -nologo ) \
    && ok "dotnet" || bad "dotnet"
}

regen_typescript() {
  step "typescript (openapi-typescript)"
  command -v pnpm >/dev/null || { skip "typescript" "pnpm not installed"; return; }
  ( cd "$REPO_ROOT/typescript" \
      && pnpm install --frozen-lockfile \
      && pnpm run generate \
      && pnpm run build ) \
    && ok "typescript" || bad "typescript"
}

regen_react() {
  step "react (openapi-typescript)"
  command -v pnpm >/dev/null || { skip "react" "pnpm not installed"; return; }
  ( cd "$REPO_ROOT/react" \
      && pnpm install --frozen-lockfile \
      && pnpm run generate \
      && pnpm run build ) \
    && ok "react" || bad "react"
}

regen_python() {
  step "python (openapi-python-client)"
  command -v openapi-python-client >/dev/null || { skip "python" "openapi-python-client not installed (pipx install openapi-python-client)"; return; }
  ( cd "$REPO_ROOT/python" && SPEC_PATH="$SPEC_PATH" ./generate.sh ) \
    && ( cd "$REPO_ROOT/python" && python3 -c "import ecf_dgii" ) \
    && ok "python" || bad "python"
}

regen_java() {
  step "java (openapi-generator java/okhttp-gson)"
  command -v npx >/dev/null && command -v java >/dev/null || { skip "java" "npx or java missing"; return; }
  make_relaxed_spec
  ( cd "$REPO_ROOT/java" \
      && JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$OPENAPI_GEN_VERSION \
         npx -y $NPX_PKG generate -c openapi-generator-config.yaml -i "$RELAXED_SPEC" ) \
    && ( cd "$REPO_ROOT/java" && ./mvnw -B -q -DskipTests=false test ) \
    && ok "java" || bad "java"
}

regen_kotlin() {
  step "kotlin (openapi-generator kotlin/jvm-okhttp4)"
  command -v npx >/dev/null && command -v java >/dev/null || { skip "kotlin" "npx or java missing"; return; }
  make_relaxed_spec
  pin_generator "$REPO_ROOT" "$KOTLIN_GEN_VERSION"
  ( cd "$REPO_ROOT" \
      && JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$KOTLIN_GEN_VERSION \
         npx -y $NPX_PKG generate \
           -i "$RELAXED_SPEC" \
           -g kotlin \
           -o kotlin/ \
           --library jvm-okhttp4 \
           --additional-properties=groupId=do.com.ssd.ecfx,artifactId=ecf-dgii-sdk-kotlin,packageName=dom.com.ssd.ecfx.sdk,serializationLibrary=kotlinx_serialization,dateLibrary=java8 )
  local rc=$?
  unpin_generator
  [[ $rc -eq 0 ]] \
    && "$REPO_ROOT/kotlin/postprocess.sh" \
    && ( cd "$REPO_ROOT/kotlin" && ./gradlew -q build ) \
    && ok "kotlin" || bad "kotlin"
}

regen_ios() {
  step "ios (openapi-generator swift6)"
  if [[ "$(uname -s)" != "Darwin" ]]; then
    skip "ios" "macOS-only (swift toolchain)"
    return
  fi
  command -v swift >/dev/null || { skip "ios" "swift not installed"; return; }
  command -v npx >/dev/null && command -v java >/dev/null || { skip "ios" "npx or java missing"; return; }
  cp "$SPEC_PATH" "$REPO_ROOT/ios/openapi-v1-processed.json"
  pin_generator "$REPO_ROOT/ios" "$IOS_GEN_VERSION"
  ( cd "$REPO_ROOT/ios" \
      && JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$IOS_GEN_VERSION \
         npx -y $NPX_PKG generate \
           -i ./openapi-v1-processed.json \
           -g swift6 \
           -o . \
           --additional-properties=projectName=EcfDgiiClient,responseAs=AsyncAwait,useSPMFileStructure=true,swiftPackagePath=Sources/EcfDgiiClient )
  local rc=$?
  unpin_generator
  [[ $rc -eq 0 ]] \
    && "$REPO_ROOT/ios/postprocess.sh" \
    && ( cd "$REPO_ROOT/ios" && swift build ) \
    && ok "ios" || bad "ios"
}

regen_cpp() {
  step "cpp (openapi-generator cpp-restsdk) — regen only, no build"
  command -v npx >/dev/null && command -v java >/dev/null || { skip "cpp" "npx or java missing"; return; }
  rm -rf "$REPO_ROOT/C++/include/ecf-dgii-client/api" \
         "$REPO_ROOT/C++/include/ecf-dgii-client/model" \
         "$REPO_ROOT/C++/src/api" \
         "$REPO_ROOT/C++/src/model"
  pin_generator "$REPO_ROOT" "$CPP_GEN_VERSION"
  ( cd "$REPO_ROOT" \
      && JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$CPP_GEN_VERSION \
         npx -y $NPX_PKG generate \
           -i "$SPEC_PATH" \
           -g cpp-restsdk \
           -o C++ \
           --additional-properties=packageName=ecf-dgii-client ) \
    && ok "cpp" || bad "cpp"
  unpin_generator
}

regen_delphi() {
  step "delphi (native RTL client / generated API routes)"
  command -v node >/dev/null || { skip "delphi" "node missing"; return; }
  if [[ "$SPEC_PATH" != "$REPO_ROOT/delphi/openapi-v1.json" ]]; then
    cp "$SPEC_PATH" "$REPO_ROOT/delphi/openapi-v1.json" || { bad "delphi contract snapshot"; return; }
  fi
  node "$REPO_ROOT/delphi/scripts/generate.mjs" \
    && ok "delphi generation" || bad "delphi generation"
  skip "delphi compilation" "run delphi/scripts/test.cmd dcc32 and dcc64 in a RAD Studio Command Prompt"
}

refresh_bruno() {
  step "bruno (bru import openapi)"
  command -v bru >/dev/null || { skip "bruno" "bru CLI not installed (pnpm add -g @usebruno/cli)"; return; }
  if [[ ! -f "$RECEPTOR_SPEC_PATH" ]]; then
    skip "bruno" "RECEPTOR_SPEC_PATH not found ($RECEPTOR_SPEC_PATH)"
    return
  fi
  bru import openapi -s "$SPEC_PATH" -f "$REPO_ROOT/bruno/ecf-dgii-api.json" -n "ECF DGII API" >/dev/null \
    && bru import openapi -s "$RECEPTOR_SPEC_PATH" -f "$REPO_ROOT/bruno/ecf-recepcion-api.json" -n "ECF Recepcion API" >/dev/null \
    && ok "bruno" || bad "bruno"
}

run_target() {
  case "$1" in
    dotnet)     regen_dotnet ;;
    typescript) regen_typescript ;;
    react)      regen_react ;;
    python)     regen_python ;;
    java)       regen_java ;;
    kotlin)     regen_kotlin ;;
    ios)        regen_ios ;;
    cpp|c++)    regen_cpp ;;
    delphi)     regen_delphi ;;
    bruno)      refresh_bruno ;;
    *)          echo "Unknown target: $1" >&2; exit 2 ;;
  esac
}

main() {
  require_spec
  echo "Repo root:      $REPO_ROOT"
  echo "Spec:           $SPEC_PATH"
  echo "Receptor spec:  $RECEPTOR_SPEC_PATH"
  echo "Generator:      $NPX_PKG  (java $OPENAPI_GEN_VERSION, kotlin $KOTLIN_GEN_VERSION, ios $IOS_GEN_VERSION, cpp $CPP_GEN_VERSION)"

  if [[ $# -gt 0 ]]; then
    for t in "$@"; do run_target "$t"; done
  else
    regen_dotnet
    regen_typescript
    regen_react
    regen_python
    regen_java
    regen_kotlin
    regen_ios
    regen_cpp
    regen_delphi
    refresh_bruno
  fi

  echo
  echo "============ SUMMARY ============"
  printf "PASS (%d):\n" "${#PASS[@]}";  for x in "${PASS[@]}";  do echo "  $x"; done
  printf "SKIP (%d):\n" "${#SKIP[@]}";  for x in "${SKIP[@]}";  do echo "  $x"; done
  printf "FAIL (%d):\n" "${#FAIL[@]}";  for x in "${FAIL[@]}";  do echo "  $x"; done
  echo "================================="
  [[ ${#FAIL[@]} -eq 0 ]] || exit 1
}

main "$@"
