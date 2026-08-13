# Especificación de Diseño: Workflow de Publicación para Ruby SDK

## Contexto
El repositorio `ecf_dgii` contiene múltiples SDKs en un monorepo poliglot. El SDK de Ruby (`ecf-dgii`) se encuentra en el directorio `ruby/`. Este documento define el diseño del workflow de CI/CD para compilar, probar y publicar de forma automatizada la gema de Ruby en RubyGems.org.

## Requerimientos
1. **CI Automatizado**: Validar (ejecutar pruebas unitarias) en cada push a la rama principal `main` que modifique el código Ruby o el workflow.
2. **CD Automatizado**: Publicar automáticamente la gema en RubyGems.org cuando se crea una nueva release de GitHub con el tag `ruby-v*`.
3. **Seguridad**: Autenticación segura con RubyGems usando secretos del repositorio de GitHub (`RUBYGEMS_API_KEY`).
4. **Consistencia**: Mantener el mismo estilo y estructura que el resto de los workflows de publicación del repositorio (e.g., `publish-pypi.yml`, `publish-npm.yml`).

## Detalles del Diseño

### Archivo del Workflow
*   **Ruta**: `.github/workflows/publish-ruby.yml`
*   **Nombre del workflow**: `publish-ruby`

### Disparadores (Triggers)
```yaml
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
```

### Trabajos (Jobs)

#### 1. Job `build`
*   **Entorno**: `ubuntu-latest`
*   **Condición**: No ser un evento `release` o, si lo es, que el tag empiece con `ruby-v`.
*   **Pasos**:
    1.  `actions/checkout@v4`: Clonar el repositorio.
    2.  `actions/setup-ruby@v1`: Configurar la versión de Ruby a `3.4` y habilitar caché de `bundler`.
    3.  Instalación de dependencias: `bundle install` en la ruta `ruby`.
    4.  Pruebas: `bundle exec rspec` en la ruta `ruby`.
    5.  Compilación: `gem build ecf-dgii.gemspec` en la ruta `ruby`.
    6.  `actions/upload-artifact@v4`: Subir el archivo `.gem` generado.

#### 2. Job `deploy`
*   **Entorno**: `ubuntu-latest`
*   **Condición**: Solo en eventos `release` y que el tag empiece con `ruby-v`.
*   **Dependencia**: Requiere que `build` se complete con éxito.
*   **Pasos**:
    1.  `actions/download-artifact@v4`: Descargar el artefacto de la gema compilada.
    2.  Configuración de credenciales de RubyGems:
        *   Crear el archivo `~/.gem/credentials`.
        *   Escribir el token `secrets.RUBYGEMS_API_KEY`.
        *   Asignar los permisos seguros `0600`.
    3.  Publicación: `gem push *.gem`.

## Plan de Pruebas y Validación
1. **Validación del Workflow**: Verificar sintaxis localmente antes de commitear.
2. **Ejecución de CI**: Comprobar que al hacer push de esta rama, el job de `build` (compilación + tests) se ejecute de forma exitosa en GitHub.
