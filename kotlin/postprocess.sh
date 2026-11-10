#!/usr/bin/env bash
# Post-process the generated Kotlin SDK (run by scripts/regenerate-all.sh).
# The generator turns `type: [integer|number, string]` schemas (page, limit,
# line numbers, amounts...) into empty wrapper classes that cannot hold a value
# (montoTotal could not even be parsed); use Int / Double instead.
set -euo pipefail
cd "$(dirname "$0")"
INTS='GetCompaniesPageParameter|GetCompaniesLimitParameter|SearchEcfReceptionRequestsTiposEcfsParameterInner'
DOUBLES='SearchEcfsAmountFromParameter'
ALL="$INTS|$DOUBLES"
for name in ${ALL//|/ }; do
  rm -f "src/main/kotlin/dom/com/ssd/ecfx/sdk/models/$name.kt" \
        "src/test/kotlin/dom/com/ssd/ecfx/sdk/models/${name}Test.kt" "docs/$name.md"
done
grep -rlE "$ALL" src docs .openapi-generator/FILES 2>/dev/null | while read -r f; do
  perl -ni -e "next if /^import dom\.com\.ssd\.ecfx\.sdk\.models\.($ALL)\$/; next if m{^(docs|src/(main|test)/kotlin/dom/com/ssd/ecfx/sdk/models)/($ALL)(Test)?\.(md|kt)\$}; print" "$f"
  perl -pi -e "s/\[\*\*($INTS)\*\*\]\([^)]*\)/**kotlin.Int**/g; s/\[\*\*($DOUBLES)\*\*\]\([^)]*\)/**kotlin.Double**/g; s/\b($INTS)\b/Int/g; s/\b($DOUBLES)\b/kotlin.Double/g" "$f"
done || true
# Response status enums: drop @Contextual so the plain enum serializer is used and
# Json { coerceInputValues = true } (set by EcfClient) turns unknown values into null.
perl -0pi -e 's/\@Contextual (\@SerialName\(value = "\w+"\)\s+val \w+: (?:DgiiSubmissionState|ReceptorDirectoryStatus|EcfEstado)\?)/$1/g' \
  src/main/kotlin/dom/com/ssd/ecfx/sdk/models/*.kt
