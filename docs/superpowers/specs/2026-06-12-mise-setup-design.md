# Diseño de Configuración de Mise para ECF DGII SDK

## 1. Contexto y Objetivos

El proyecto `ecf_dgii` es un monorepo poliglot que contiene SDKs de facturación electrónica para múltiples lenguajes de programación (.NET, TypeScript, React, Python, Java, Kotlin, iOS, C++). 

Para regenerar y validar estos SDKs, los desarrolladores y los pipelines de CI necesitan un conjunto diverso de herramientas instaladas en sus entornos de desarrollo locales. Para simplificar esta configuración y asegurar la consistencia, se implementará una configuración de `mise` centralizada en la raíz del proyecto.

## 2. Herramientas y Versiones

Se configurará el archivo `mise.toml` en la raíz con las siguientes herramientas:

* **dotnet**: `10.0.105` (Alineado con el archivo [global.json](file:///home/deuriib/Projects/ecf_dgii/global.json) del monorepo).
* **node**: `22` (Versión estable LTS que satisface el requisito `>=18` del SDK de TypeScript y React).
* **pnpm**: `latest` (Gestor de paquetes recomendado para los proyectos de TypeScript y React).
* **python**: `3.12` (Versión compatible para el SDK de Python y sus herramientas de generación).
* **java**: `temurin-17` (JDK LTS que permite la compilación tanto del SDK de Java con target Java 8 como del SDK de Kotlin con target Java 11).
* **kiota**: `1.32.2` (Versión de la CLI de Kiota compatible con la biblioteca de abstracción de .NET).

## 3. Tareas Automatizadas (Mise Tasks)

Se definirán las siguientes tareas dentro de `mise.toml` para agilizar el flujo de trabajo:

```toml
[tasks."regen"]
description = "Regenera todos los SDKs del monorepo"
run = "./scripts/regenerate-all.sh"

[tasks."regen:dotnet"]
description = "Regenera el SDK de .NET"
run = "./scripts/regenerate-all.sh dotnet"

[tasks."regen:typescript"]
description = "Regenera el SDK de TypeScript"
run = "./scripts/regenerate-all.sh typescript"

[tasks."regen:react"]
description = "Regenera el SDK de React"
run = "./scripts/regenerate-all.sh react"

[tasks."regen:python"]
description = "Regenera el SDK de Python"
run = "./scripts/regenerate-all.sh python"

[tasks."regen:java"]
description = "Regenera el SDK de Java"
run = "./scripts/regenerate-all.sh java"

[tasks."regen:kotlin"]
description = "Regenera el SDK de Kotlin"
run = "./scripts/regenerate-all.sh kotlin"

[tasks."regen:ios"]
description = "Regenera el SDK de iOS (Solo macOS)"
run = "./scripts/regenerate-all.sh ios"

[tasks."regen:cpp"]
description = "Regenera el SDK de C++"
run = "./scripts/regenerate-all.sh cpp"

[tasks."regen:bruno"]
description = "Actualiza las colecciones de Bruno"
run = "./scripts/regenerate-all.sh bruno"
```

## 4. Plan de Verificación

Una vez creado el archivo `mise.toml`:
1. Se ejecutará `mise install` para verificar la descarga e instalación correcta de todas las herramientas.
2. Se verificará que las versiones activas en la shell coincidan con las especificadas.
3. Se correrá una prueba de regeneración parcial (ej. `mise run regen:typescript`) para validar que las tareas funcionen correctamente con el entorno cargado de mise.
