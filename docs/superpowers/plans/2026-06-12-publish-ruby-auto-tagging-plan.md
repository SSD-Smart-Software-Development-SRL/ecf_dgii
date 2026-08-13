# Auto-Tagging en Workflow de Ruby - Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Modificar `.github/workflows/publish-ruby.yml` para soportar triggers de tags, añadir un job intermedio `tag-creation` en pushes a `main`, y actualizar `deploy` para que se ejecute en el tag push.

**Architecture:** 
1. `push` a `main` -> ejecuta `build` (tests + build) -> ejecuta `tag-creation` (si la versión de `lib/ecf_dgii/version.rb` no tiene tag, lo crea y empuja).
2. `push` de tag `ruby-v*` -> ejecuta `build` (tests + build) -> ejecuta `deploy` (publica en RubyGems).

**Tech Stack:** GitHub Actions, Git, Ruby.

---

### Task 1: Modificar el archivo de workflow de GitHub Actions

**Files:**
- Modify: `.github/workflows/publish-ruby.yml`

- [ ] **Step 1: Reemplazar el contenido de `.github/workflows/publish-ruby.yml`**

Reemplazar el archivo entero con el nuevo diseño que incluye triggers de tags, job de tag-creation y las condiciones actualizadas:

```yaml
# yaml-language-server: $schema=https://json.schemastore.org/github-workflow.json

name: publish-ruby
on:
  workflow_dispatch:
  push:
    branches:
      - 'main'
    tags:
      - 'ruby-v*'
    paths:
      - 'ruby/**'
      - '.github/workflows/publish-ruby.yml'
  release:
    types:
      - published

defaults:
  run:
    working-directory: ruby

jobs:
  build:
    if: github.event_name != 'release' || startsWith(github.event.release.tag_name, 'ruby-v')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

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

      - name: Build gem
        run: gem build ecf-dgii.gemspec

      - name: Upload gem artifact
        uses: actions/upload-artifact@v4
        with:
          name: ruby-gem
          if-no-files-found: error
          retention-days: 7
          path: ruby/*.gem

  tag-creation:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    needs: [ build ]
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.4'

      - name: Extract Version & Push Tag
        run: |
          VERSION=$(ruby -Ilib -r ecf_dgii/version -e 'puts EcfDgii::VERSION')
          TAG_NAME="ruby-v$VERSION"
          
          if git rev-parse "$TAG_NAME" >/dev/null 2>&1; then
            echo "El tag $TAG_NAME ya existe. Omitiendo creación."
          else
            echo "Creando y empujando el tag $TAG_NAME..."
            git config --global user.name "github-actions[bot]"
            git config --global user.email "github-actions[bot]@users.noreply.github.com"
            git tag "$TAG_NAME"
            git push origin "$TAG_NAME"
          fi

  deploy:
    if: (github.event_name == 'release' && startsWith(github.event.release.tag_name, 'ruby-v')) || (github.event_name == 'push' && startsWith(github.ref, 'refs/tags/ruby-v'))
    runs-on: ubuntu-latest
    needs: [ build ]
    steps:
      - uses: actions/checkout@v4

      - name: Download gem artifact
        uses: actions/download-artifact@v4
        with:
          name: ruby-gem
          path: ruby/

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.4'

      - name: Configure RubyGems Credentials & Publish
        env:
          GEM_HOST_API_KEY: ${{ secrets.RUBYGEMS_API_KEY }}
        run: |
          mkdir -p ~/.gem
          chmod 0700 ~/.gem
          echo "---" > ~/.gem/credentials
          echo ":rubygems_api_key: $GEM_HOST_API_KEY" >> ~/.gem/credentials
          chmod 0600 ~/.gem/credentials
          cd ruby
          gem push *.gem
```

- [ ] **Step 2: Commit local de los cambios**

```bash
git add .github/workflows/publish-ruby.yml
git commit -m "ci: add automatic git tagging to ruby workflow"
```
