# DGII ECF SDK - Agent Instructions

This repository contains client SDKs for integrating with the ECF SSD API (Dominican Republic Electronic Invoicing) across multiple languages.

## Architecture & Code Boundaries

- **Polyglot Monorepo**: Each directory (`.net`, `typescript`, `react`, `python`, `java`, `kotlin`, `ios`, `C++`) is an independent package. PHP is maintained in a separate repository.
- **Generated vs. Handwritten Code**:
  - The SDKs are built on top of auto-generated API clients (usually under a `generated/` directory or similar) powered by OpenAPI.
  - **DO NOT** edit the generated code. If the API model/schema needs changing, the OpenAPI spec must be updated in its canonical location (a sibling repository) and the SDKs regenerated.
  - **DO** edit the custom handwritten wrappers (e.g., `client.ts`, `polling.py`, `frontend_client.py`). These provide DX, manage JWT authentication, and implement the mandatory polling logic for checking ECF submission status.

## Regeneration Workflow

If the upstream OpenAPI spec (`v1.json`) changes, you must regenerate the affected SDKs using the provided bash script.

- **Main Script**: `./scripts/regenerate-all.sh`
- **Regenerate specific language**: `./scripts/regenerate-all.sh typescript` (replace `typescript` with `python`, `dotnet`, etc.)
- **Environment Variables**: The script relies on the `SPEC_PATH` environment variable pointing to the canonical OpenAPI spec file.
  - Default: `$HOME/Developer/puntoos/ecf_dgii/src/Apis/ECF_DGII.EcfApi/wwwroot/openapi/v1.json`
- **TypeScript/React Quirks**: The `generate` npm script inside `typescript/package.json` and `react/package.json` hardcodes a relative path to the sibling repository (`../../ecf_dgii/src/Apis/.../v1.json`). If you run `pnpm generate` manually in those directories, ensure the sibling repo exists there.

## Versioning & Publishing

- **Version Bumping**: Version numbers are **not** updated automatically by the generator script. You must bump them manually in the respective manifests (`package.json`, `pyproject.toml`, `.csproj`, etc.) when making changes.
- **Publishing**: Packages are published via GitHub Actions (`.github/workflows/publish-*.yml`). Deployment to package registries (npm, PyPI, NuGet, etc.) typically triggers when a **GitHub Release** is created (e.g., `npm-v1.0.0`), not just on branch push.

## Testing & Quality

- Refer to each package's `README.md` for specific test commands.
- For Node.js packages (TypeScript, React), `pnpm` is the package manager (`pnpm install --frozen-lockfile`, `pnpm build`, `pnpm test`).
- Ensure any modifications to the handwritten wrappers correctly implement the polling logic with exponential backoff and accurately handle the `EcfResponse` interface.
