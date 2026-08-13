# Auto-Tagging y Despliegue en la misma ejecución - Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Resolver la restricción de GitHub Actions por la cual los eventos disparados por `GITHUB_TOKEN` no desencadenan otros workflows. Configurar el job `tag-creation` para producir un output (`created: true`) y encadenar el job `deploy` para ejecutarse en el mismo pipeline si el tag fue recién creado.

**Architecture:**
1. `push` a `main` -> ejecuta `build`.
2. `tag-creation` se ejecuta después de `build`. Si crea y empuja el tag, retorna `created=true`.
3. `deploy` se ejecuta después de `build` y `tag-creation`. Se ejecuta si el evento es un release manual OR si el push a main produjo un tag nuevo (`created == 'true'`).

**Tech Stack:** GitHub Actions, Git, Ruby.

---

### Task 1: Modificar el archivo de workflow de GitHub Actions

**Files:**
- Modify: `.github/workflows/publish-ruby.yml`

- [ ] **Step 1: Reemplazar el contenido de `.github/workflows/publish-ruby.yml`**

Reemplazar el archivo con el nuevo diseño que implementa outputs y encadenamiento:

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
    outputs:
      created: ${{ steps.push-tag.outputs.created }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.4'

      - name: Extract Version & Push Tag
        id: push-tag
        run: |
          VERSION=$(ruby -Ilib -r ecf_dgii/version -e 'puts EcfDgii::VERSION')
          TAG_NAME="ruby-v$VERSION"
          
          if git rev-parse "$TAG_NAME" >/dev/null 2>&1; then
            echo "El tag $TAG_NAME ya existe. Omitiendo creación."
            echo "created=false" >> $GITHUB_OUTPUT
          else
            echo "Creando y empujando el tag $TAG_NAME..."
            git config --global user.name "github-actions[bot]"
            git config --global user.email "github-actions[bot]@users.noreply.github.com"
            git tag "$TAG_NAME"
            git push origin "$TAG_NAME"
            echo "created=true" >> $GITHUB_OUTPUT
          fi

  deploy:
    if: (github.event_name == 'release' && startsWith(github.event.release.tag_name, 'ruby-v')) || (github.event_name == 'push' && github.ref == 'refs/heads/main' && needs.tag-creation.outputs.created == 'true')
    runs-on: ubuntu-latest
    needs: [ build, tag-creation ]
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
git commit -m "ci: deploy in the same run if new tag is created"
```
