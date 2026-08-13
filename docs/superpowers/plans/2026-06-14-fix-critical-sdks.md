# Fix Critical SDKs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the 3 SDKs that are completely broken (Python, Ruby, C++) so they compile/import and their READMEs reflect the actual API.

**Architecture:** Each SDK is independent — they share the same OpenAPI spec source but different generators. Python uses `openapi-python-client`, Ruby and C++ use `openapi-generator`. The root cause for all 3 is that generated code changed but handwritten wrappers and docs were not updated.

**Tech Stack:** openapi-python-client, openapi-generator 7.14.0, kiota, npx, python3, ruby, CMake

---

## File Structure

### Python SDK
- `python/generate.sh` — regeneration script (needs openapi-python-client)
- `python/ecf_dgii/client.py` — handwritten client (imports from missing generated module)
- `python/ecf_dgii/__init__.py` — re-exports (needs EstadoType)
- `python/ecf_dgii/frontend_client.py` — may need import fixes
- `python/ecf_dgii/generated/api/ecf/` — MISSING module
- `python/README.md` — needs full rewrite for per-type models

### Ruby SDK
- `ruby/generate.sh` — regeneration script
- `ruby/lib/ecf_dgii/client.rb` — handwritten client (references generated APIs)
- `ruby/lib/ecf_dgii/generated/models/` — MISSING directory
- `ruby/lib/ecf_dgii/frontend_client.rb` — may need fixes

### C++ SDK
- `C++/include/ecf-dgii-client/EcfClient.h` — handwritten client (sendEcf removed, docs correct)
- `C++/test_package/src/test.cpp` — BROKEN (uses old model names)
- `C++/README.md` — outdated (references sendEcf, old model names)
- `C++/include/ecf-dgii-client/model/` — generated models EXIST (Ecf31ECF.h etc.) ✅

---

### Task 1: Python — Install openapi-python-client and regenerate SDK

**Files:**
- Install: `pipx install openapi-python-client`
- Modify: `python/generate.sh` (if needed for Windows compat)
- Run: `python/generate.sh`

- [ ] **Step 1: Install openapi-python-client**

Run: `pipx install openapi-python-client`
Expected: Installed successfully

- [ ] **Step 2: Regenerate Python SDK**

```bash
cd python
$env:SPEC_PATH = "$HOME/Developer/puntoos/ecf_dgii/src/Apis/ECF_DGII.EcfApi/wwwroot/openapi/v1.json"
./generate.sh
```

Expected: Script completes, `ecf_dgii/generated/` has `api/ecf/` module

- [ ] **Step 3: Verify import works**

```bash
cd python
python -c "import ecf_dgii; print('IMPORT OK')"
```

Expected: `IMPORT OK`

- [ ] **Step 4: Run tests to verify nothing is broken**

```bash
cd python
pip install -e ".[dev]"
pytest
```

Expected: Tests pass

- [ ] **Step 5: Commit**

```bash
git add python/ecf_dgii/generated/
git commit -m "fix(python): regenerate SDK from OpenAPI spec"
```

---

### Task 2: Python — Add missing EstadoType re-export and fix README

**Files:**
- Modify: `python/ecf_dgii/__init__.py` — add EstadoType
- Modify: `python/README.md` — update examples

- [ ] **Step 1: Add EstadoType to __init__.py exports**

Add `EstadoType` to the imports and `__all__` list in `ecf_dgii/__init__.py`.

- [ ] **Step 2: Fix README — update imports to use per-type models**

Change:
```python
from ecf_dgii import EcfClient, ECF, Encabezado, IdDoc, Emisor, Totales, Item
```
To:
```python
from ecf_dgii import EcfClient, Ecf31ECF, Ecf31Encabezado, Ecf31IdDoc, Ecf31Emisor, Ecf31Totales, Ecf31Item
```

- [ ] **Step 3: Fix README — update send_ecf() to use per-type methods**

Change `client.send_ecf(ecf)` to `client.send_ecf31(ecf)`.

- [ ] **Step 4: Fix README — correct method names**

Fix:
- `get_certificate` → `get_current_certificate`
- `update_certificate` → `update_certificate_company` (update signature)
- `aprobacion_comercial` → `send_aprobacion_comercial`
- `estatus_servicios` → `estatus_servicio`
- `consulta_directorio_listado` → `consulta_directorio`

- [ ] **Step 5: Fix README — add await to frontend examples**

All frontend methods are async — add `await` to examples.

- [ ] **Step 6: Commit**

```bash
git add python/ecf_dgii/__init__.py python/README.md
git commit -m "fix(python): align README with regenerated SDK and fix EstadoType export"
```

---

### Task 3: Ruby — Regenerate SDK

**Files:**
- Run: `ruby/generate.sh`
- Verify: `ruby/lib/ecf_dgii/generated/models/` exists

- [ ] **Step 1: Regenerate Ruby SDK**

```bash
cd ruby
$env:SPEC_PATH = "$HOME/Developer/puntoos/ecf_dgii/src/Apis/ECF_DGII.EcfApi/wwwroot/openapi/v1.json"
./generate.sh
```

Expected: Script completes, `lib/ecf_dgii/generated/models/` has model files

- [ ] **Step 2: Verify tests pass**

```bash
cd ruby
bundle exec rake spec
```

Expected: Tests pass

- [ ] **Step 3: Commit**

```bash
git add ruby/lib/ecf_dgii/generated/
git commit -m "fix(ruby): regenerate SDK from OpenAPI spec"
```

---

### Task 4: C++ — Fix test_package and README

**Files:**
- Modify: `C++/test_package/src/test.cpp` — use per-type models
- Modify: `C++/README.md` — remove sendEcf references, update examples

- [ ] **Step 1: Fix test_package/src/test.cpp**

Replace old generic model includes with per-type:
```cpp
// Before:
#include <ecf-dgii-client/model/ECF.h>
// After:
#include <ecf-dgii-client/model/Ecf31ECF.h>
#include <ecf-dgii-client/model/Ecf31Encabezado.h>
#include <ecf-dgii-client/model/Ecf31IdDoc.h>
```

- [ ] **Step 2: Update README — remove sendEcf references**

Replace all `sendEcf(ecf)` with `ecfApi()->recepcionEcf31(rnc, ecf31)` pattern.

- [ ] **Step 3: Update README — fix model names**

Replace generic `ECF`, `Encabezado`, `IdDoc`, `Emisor` with per-type `Ecf31ECF`, `Ecf31Encabezado`, etc.

- [ ] **Step 4: Update README — fix consultaEstado signature**

`consultaEstado(rnc, encf)` → `consultaEstado(rnc, rncEmisor, ncfElectronico, rncComprador, codigoSeguridad)`

- [ ] **Step 5: Commit**

```bash
git add C++/test_package/src/test.cpp C++/README.md
git commit -m "fix(cpp): align test_package and README with per-type models"
```

---

### Task 5: Update root README with correct imports

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Fix TypeScript import**

Change `import { EcfClient } from 'ecf-dgii-client'` to `import { EcfClient } from '@ssddo/ecf-sdk'`

- [ ] **Step 2: Fix Python import**

Change `from ecf_dgii_client import EcfClient` to `from ecf_dgii import EcfClient`

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "fix(root): correct SDK import paths in examples"
```
