# Mise Setup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Configurar el entorno de herramientas del monorepo mediante un archivo `mise.toml` en la raíz con soporte para Node.js, pnpm, Python, Java y .NET SDK, además de definir las tareas de automatización para la regeneración y compilación de los SDKs.

**Architecture:** Se creará un único archivo `mise.toml` en la raíz del proyecto para centralizar el entorno de desarrollo y las tareas comunes.

**Tech Stack:** mise, Node.js, pnpm, Python, Java, .NET SDK, Kiota.

---

### Task 1: Crear archivo `mise.toml` en la raíz

**Files:**
- Create: `mise.toml`

- [x] **Step 1: Crear el archivo `mise.toml`**

Escribir el siguiente contenido en el archivo:

```toml
[tools]
dotnet = "10.0.105"
node = "22"
pnpm = "latest"
python = "3.12"
java = "temurin-17"
kiota = "1.32.2"

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

- [x] **Step 2: Commit**

```bash
git add mise.toml
git commit -m "feat: add mise.toml configuration with tools and tasks"
```

---

### Task 2: Verificar la instalación de herramientas mediante Mise

**Files:**
- Modify: None (verification step)

- [x] **Step 1: Instalar herramientas especificadas**

Ejecutar el comando de instalación de mise para asegurar que todas las herramientas y plugins se descarguen e instalen.

Run: `mise install`
Expected output: Mensajes indicando que se instalaron o usaron las versiones correctas de dotnet, node, pnpm, python, java, kiota.

- [x] **Step 2: Verificar versión activa de las herramientas principales**

Correr comandos de versión para verificar que `mise` los esté sirviendo correctamente.

Run: `mise exec -- node -v && mise exec -- dotnet --version && mise exec -- java -version && mise exec -- python --version && mise exec -- kiota --version`
Expected output:
- node: `v22.x.x`
- dotnet: `10.0.105`
- java: `openjdk version "17.0.x"` (o temurin)
- python: `3.12.x`
- kiota: `1.32.2`

---

### Task 3: Probar las tareas de Mise

**Files:**
- Modify: None (verification step)

- [x] **Step 1: Listar las tareas disponibles en mise**

Run: `mise tasks`
Expected output: Una lista de tareas que incluye `regen`, `regen:dotnet`, `regen:typescript`, etc., con sus respectivas descripciones.

- [x] **Step 2: Ejecutar una tarea de prueba (ej. bruno)**

Haremos una prueba con la tarea `regen:bruno` que usa `bru` si estuviera disponible, o de lo contrario validaremos si el script `./scripts/regenerate-all.sh` es invocado. Nota: Si falla porque falta el archivo `v1.json` del spec de OpenAPI, el script debería fallar indicando "Spec not found at..." en vez de fallar porque las herramientas o el script no son encontrados.

Run: `mise run regen:bruno`
Expected output: El script de regeneración debe ejecutarse e intentar buscar el spec en la ruta establecida, imprimiendo el mensaje correspondiente en consola.

- [x] **Step 3: Fijar versiones exactas de Node y pnpm en `mise.toml`**

Modificar `mise.toml` para usar `node = "22.22.3"` y `pnpm = "11.6.0"`.

- [x] **Step 4: Hacer commit de las versiones fijadas**

Run:
```bash
git add mise.toml
git commit -m "refactor: pin node and pnpm versions in mise.toml for reproducibility"
```
