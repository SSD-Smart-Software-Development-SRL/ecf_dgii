# Publicación Automática del SDK de Ruby en GitHub Actions - Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear el workflow `.github/workflows/publish-ruby.yml` para compilar, testear y publicar la gema de Ruby en RubyGems.org cuando se publique un release de GitHub.

**Architecture:** Se utilizará un pipeline de dos etapas (build y deploy) en GitHub Actions. La etapa de build corre en todos los pushes a main/PRs de ruby y compila la gema; la etapa de deploy corre solo en releases de GitHub con tags del formato `ruby-v*`.

**Tech Stack:** GitHub Actions, Ruby 3.4, Bundler, RubyGems.

---

### Task 1: Crear el archivo de workflow de GitHub Actions

**Files:**
- Create: `.github/workflows/publish-ruby.yml`

- [ ] **Step 1: Escribir el contenido del archivo de workflow**

Crear el archivo `.github/workflows/publish-ruby.yml` con el siguiente contenido:

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

  deploy:
    if: github.event_name == 'release' && startsWith(github.event.release.tag_name, 'ruby-v')
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

Ejecutar en la terminal para guardar los cambios de la tarea:
```bash
git add .github/workflows/publish-ruby.yml
git commit -m "ci: add GitHub Actions workflow to publish Ruby gem"
```
