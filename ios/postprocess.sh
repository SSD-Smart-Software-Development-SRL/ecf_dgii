#!/usr/bin/env bash
# Post-process the generated Swift SDK (run by scripts/regenerate-all.sh):
# - Int/Double instead of the empty `type: [integer|number, string]` wrappers;
# - explicit dictionary types so Swift 6 type-checks the long query lists;
# - unknown DgiiSubmissionState / ReceptorDirectoryStatus values decode as
#   `.unknownDefaultOpenApi` instead of failing the whole response.
set -euo pipefail
cd "$(dirname "$0")"
for name in GetCompaniesPageParameter GetCompaniesLimitParameter SearchEcfsAmountFromParameter; do
  rm -f "Sources/EcfDgiiClient/Models/$name.swift" "docs/$name.md"
done
for f in Sources/EcfDgiiClient/APIs/*.swift Sources/EcfDgiiClient/Models/*.swift; do
  perl -pi -e 's/\bGetCompanies(Page|Limit)Parameter\b/Int/g; s/\bSearchEcfsAmountFromParameter\b/Double/g' "$f"
  case "$f" in *DgiiAPI.swift|*ApiKeyAPI.swift|*/Models/*) continue ;; esac
  perl -0pi -e 's/APIHelper\.mapValuesToQueryItems\(\[\n(.*?)\n        \]\)/APIHelper.mapValuesToQueryItems(([\n$1\n        ] as [String: (wrappedValue: (any Sendable)?, isExplode: Bool)]))/gs' "$f"
done
for name in DgiiSubmissionState ReceptorDirectoryStatus; do
  f="Sources/EcfDgiiClient/Models/$name.swift"
  grep -q unknownDefaultOpenApi "$f" && continue
  perl -0pi -e 's/(public enum \w+: String, Sendable, Codable, CaseIterable) \{\n(.*?)\n\}/$1, CaseIterableDefaultsLast {\n$2\n    case unknownDefaultOpenApi = "unknown_default_open_api"\n}/s' "$f"
done
