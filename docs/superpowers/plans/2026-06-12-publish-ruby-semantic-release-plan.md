# Integración de Semantic Release para Ruby SDK - Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Configurar e integrar Semantic Release en el SDK de Ruby de manera que en cada push a `main` se analicen de forma aislada los commits de la carpeta `ruby/`, se determine la nueva versión semántica, se realice el commit con la actualización de versión, se cree el tag de git y se publique la gema en RubyGems.org.

**Architecture:**
*   **Filtro**: `semantic-release-monorepo` limita el análisis al historial de `ruby/**`.
*   **Pipeline**: Un único job `release` ejecuta los tests y luego corre `semantic-release`.
*   **Automatización de Versión**: Se edita el archivo `lib/ecf_dgii/version.rb` en la fase `prepareCmd` usando una sustitución por expresión regular en Ruby.
*   **Publicación**: Se realiza `gem build` y `gem push` en la fase `publishCmd`.
*   **Tag & Changelog**: Se suben a GitHub a través de los plugins estándar de semantic-release.

**Tech Stack:** GitHub Actions, Semantic Release (JS), RubyGems, Ruby.

---

### Task 1: Crear la configuración de Semantic Release

**Files:**
- Create: `ruby/.releaserc.json`

- [ ] **Step 1: Escribir el archivo `.releaserc.json`**

Crear el archivo `ruby/.releaserc.json` con el siguiente contenido:

```json
{
  "extends": "semantic-release-monorepo",
  "tagFormat": "ruby-v${version}",
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/exec",
      {
        "prepareCmd": "ruby -pi -e 'gsub(/VERSION = \".*?\"/, \"VERSION = \\\"${nextRelease.version}\\\"\")' lib/ecf_dgii/version.rb",
        "publishCmd": "gem build ecf-dgii.gemspec && gem push ecf-dgii-${nextRelease.version}.gem"
      }
    ],
    [
      "@semantic-release/git",
      {
        "assets": ["lib/ecf_dgii/version.rb"],
        "message": "chore(ruby): release ${nextRelease.version} [skip ci]"
      }
    ],
    "@semantic-release/github"
  ]
}
```

---

### Task 2: Actualizar el workflow de GitHub Actions

**Files:**
- Modify: `.github/workflows/publish-ruby.yml`

- [ ] **Step 1: Sobreescribir el archivo del workflow**

Reemplazar todo el contenido de `.github/workflows/publish-ruby.yml` con el siguiente workflow simplificado:

```yaml
# yaml-language-server: $schema=https://json.schemastore.org/github-workflow.json

name: publish-ruby
on:
  workflow_dispatch:
  push:
    branches:
      - 'main'
    paths:
      - 'ruby/**'
      - '.github/workflows/publish-ruby.yml'

defaults:
  run:
    working-directory: ruby

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Setup Java
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Generate SDK code
        run: ./generate.sh

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.4'
          bundler-cache: true
          working-directory: ruby

      - name: Install dependencies
        run: bundle install

      - name: Run tests
        run: bundle exec rspec

      - name: Run Semantic Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GEM_HOST_API_KEY: ${{ secrets.RUBYGEMS_API_KEY }}
        run: |
          npx -p semantic-release \
              -p semantic-release-monorepo \
              -p @semantic-release/exec \
              -p @semantic-release/git \
              semantic-release
```

---

### Task 3: Commit y push de los cambios

- [ ] **Step 1: Commitear los cambios y empujar**

```bash
git add ruby/.releaserc.json .github/workflows/publish-ruby.yml
git commit -m "ci: integrate semantic-release for automatic versioning and release"
git push
```
