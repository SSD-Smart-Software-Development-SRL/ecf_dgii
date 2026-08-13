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
#   OPENAPI_GEN_VERSION  openapi-generator JAR version (default: 7.14.0)
#
# Exit code: 0 if all attempted SDKs passed; 1 if any failed (skipped does not count).
#
set -o pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Ensure user's gem bin directory is in PATH
USER_GEM_BIN="$(ruby -e "require 'rubygems'; puts Gem.user_dir + '/bin'" 2>/dev/null || true)"
if [[ -n "$USER_GEM_BIN" && -d "$USER_GEM_BIN" ]]; then
  export PATH="$USER_GEM_BIN:$PATH"
fi

SPEC_PATH="${SPEC_PATH:-$HOME/Developer/puntoos/ecf_dgii/src/Apis/ECF_DGII.EcfApi/wwwroot/openapi/v1.json}"
RECEPTOR_SPEC_PATH="${RECEPTOR_SPEC_PATH:-$HOME/Developer/puntoos/ecf_dgii/src/Apis/ECF_DGII.ReceptorApi/wwwroot/openapi/v1.json}"
# Convert SPEC_PATH and RECEPTOR_SPEC_PATH to absolute paths if they are relative
if [[ ! "$SPEC_PATH" =~ ^/ ]]; then
  SPEC_PATH="$(pwd)/$SPEC_PATH"
fi
if [[ ! "$RECEPTOR_SPEC_PATH" =~ ^/ ]]; then
  RECEPTOR_SPEC_PATH="$(pwd)/$RECEPTOR_SPEC_PATH"
fi
OPENAPI_GEN_VERSION="${OPENAPI_GEN_VERSION:-7.14.0}"
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
  ( cd "$REPO_ROOT/java" \
      && JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$OPENAPI_GEN_VERSION \
         npx -y $NPX_PKG generate -c openapi-generator-config.yaml -i "$SPEC_PATH" ) \
    && ( cd "$REPO_ROOT/java" && ./mvnw -B -q -DskipTests=false test ) \
    && ok "java" || bad "java"
}

regen_kotlin() {
  step "kotlin (openapi-generator kotlin/jvm-okhttp4)"
  command -v npx >/dev/null && command -v java >/dev/null || { skip "kotlin" "npx or java missing"; return; }
  ( cd "$REPO_ROOT" \
      && JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$OPENAPI_GEN_VERSION \
         npx -y $NPX_PKG generate \
           -i "$SPEC_PATH" \
           -g kotlin \
           -o kotlin/ \
           --library jvm-okhttp4 \
           --additional-properties=groupId=do.com.ssd.ecfx,artifactId=ecf-dgii-sdk-kotlin,packageName=dom.com.ssd.ecfx.sdk,serializationLibrary=kotlinx_serialization,dateLibrary=java8 ) \
    && ( cd "$REPO_ROOT/kotlin" && ./gradlew -q build -x test ) \
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
  ( cd "$REPO_ROOT/ios" \
      && JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$OPENAPI_GEN_VERSION \
         npx -y $NPX_PKG generate \
           -i ./openapi-v1-processed.json \
           -g swift6 \
           -o . \
           --additional-properties=projectName=EcfDgiiClient,responseAs=AsyncAwait,useSPMFileStructure=true,swiftPackagePath=Sources/EcfDgiiClient ) \
    && ( cd "$REPO_ROOT/ios" && swift build ) \
    && ok "ios" || bad "ios"
}

regen_ruby() {
  step "ruby (openapi-generator)"
  command -v npx >/dev/null && command -v java >/dev/null || { skip "ruby" "npx or java missing"; return; }
  ( cd "$REPO_ROOT/ruby" \
      && SPEC_PATH="$SPEC_PATH" ./generate.sh \
      && bundle exec rake spec ) \
    && ok "ruby" || bad "ruby"
}

regen_cpp() {
  step "cpp (openapi-generator cpp-restsdk) — regen only, no build"
  command -v npx >/dev/null && command -v java >/dev/null || { skip "cpp" "npx or java missing"; return; }
  rm -rf "$REPO_ROOT/C++/include/ecf-dgii-client/api" \
         "$REPO_ROOT/C++/include/ecf-dgii-client/model" \
         "$REPO_ROOT/C++/src/api" \
         "$REPO_ROOT/C++/src/model"
  ( cd "$REPO_ROOT" \
      && JAVA_OPTS="-Xmx4g" OPENAPI_GENERATOR_VERSION=$OPENAPI_GEN_VERSION \
         npx -y $NPX_PKG generate \
           -i "$SPEC_PATH" \
           -g cpp-restsdk \
           -o C++ \
           --additional-properties=packageName=ecf-dgii-client ) \
    && ok "cpp" || bad "cpp"
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
    ruby)       regen_ruby ;;
    cpp|c++)    regen_cpp ;;
    bruno)      refresh_bruno ;;
    *)          echo "Unknown target: $1" >&2; exit 2 ;;
  esac
}

main() {
  require_spec
  echo "Repo root:      $REPO_ROOT"
  echo "Spec:           $SPEC_PATH"
  echo "Receptor spec:  $RECEPTOR_SPEC_PATH"
  echo "Generator:      $NPX_PKG  (JAR $OPENAPI_GEN_VERSION)"

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
    regen_ruby
    regen_cpp
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
