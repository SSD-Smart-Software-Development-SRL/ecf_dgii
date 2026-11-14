# Publicar el SDK Delphi con GitHub Actions

El workflow [publish-delphi.yml](../.github/workflows/publish-delphi.yml) sigue el
patrón de los otros SDKs: valida en `main` y publica automáticamente los archivos
cuando se crea una **GitHub Release** cuyo tag sea `delphi-vX.Y.Z`.

La distribución para el gestor **Boss** usa Git y el `boss.json` de la raíz del
monorepo. No requiere una cuenta de registro ni una API key de Boss. Los consumidores
fijan el tag Delphi en sus dependencias. El workflow adjunta el ZIP de fuentes probado
y su checksum SHA-256 a la release usando el `GITHUB_TOKEN` del repositorio.

## Configuración única del CI

1. Registra un runner Windows x64 con una instalación licenciada de Delphi y las
   etiquetas `self-hosted`, `Windows`, `X64`, `delphi`. Debe ser accesible desde este
   repositorio; un runner de organización restringido a repositorios privados no sirve.
2. En **Settings → Secrets and variables → Actions → Variables**, crea
   `DELPHI_RSVARS` con la ruta completa de `rsvars.bat`, por ejemplo
   `C:\Program Files (x86)\Embarcadero\Studio\23.0\bin\rsvars.bat` para una
   instalación de RAD Studio 12. Usa la ruta real de tu instalación.
3. El usuario del servicio del runner debe poder ejecutar `dcc32` y `dcc64` tras
   cargar ese archivo y tener la licencia de Delphi disponible.
4. Ejecuta **Actions → publish-delphi → Run workflow** en `main` para comprobar
   el proceso sin publicar una release.

El repositorio no tenía runners ni variables configuradas al preparar este workflow.
La configuración anterior sigue pendiente. GitHub-hosted runners no incluyen Delphi;
los checks de Node no sustituyen la compilación nativa.
Si falta `DELPHI_RSVARS`, una release o una ejecución manual fallan con un mensaje de
configuración antes de programar la compilación, y nunca se publica un ZIP sin haber ejecutado
las pruebas nativas. Un push a `main` solo muestra una advertencia y omite la compilación nativa.

## Publicar una versión

1. Actualiza `ECF_SDK_VERSION` en `delphi/src/EcfDgii.Types.pas`, `version` en el
   `boss.json` de la raíz y las versiones mostradas en documentación.
2. Confirma los cambios y súbelos a `main`.
3. En GitHub, crea y publica una release con tag **`delphi-v1.0.0`** para la primera
   versión (después, `delphi-vX.Y.Z`). No adjuntes el ZIP manualmente.

También puedes crear la release desde CLI, después de subir el commit y el tag:

```sh
git tag -a delphi-v1.0.0 -m "Delphi SDK 1.0.0"
git push origin delphi-v1.0.0
gh release create delphi-v1.0.0 --verify-tag --title "Delphi SDK 1.0.0" --generate-notes
```

**Crear solo el tag no publica los archivos**: al igual que los otros workflows,
la publicación se dispara con el evento `release.published`. Los tags de otros SDKs
se omiten. Un tag Delphi que no coincida con la versión del código y de Boss falla
antes del empaquetado.

## Qué hace el workflow

| Evento | Checks de contrato/paquete | Compilación Delphi | Adjuntar archivos a la release |
| --- | --- | --- | --- |
| Pull request con cambios Delphi | Sí, Ubuntu hospedado | No | No |
| Push a `main` con cambios Delphi | Sí | Win32 y Win64 (si el runner está configurado) | No |
| `workflow_dispatch` | Sí | Win32 y Win64 | No |
| Release `delphi-vX.Y.Z` | Sí | Win32 y Win64 | Sí, después de pasar ambos jobs |
| Release de otro SDK | Omitido | Omitido | Omitido |

El job hospedado verifica los 41 métodos contra `delphi/openapi-v1.json`, comprueba
los metadatos/versiones, construye el archivo, compara su contenido con las fuentes
y verifica SHA-256. Usa una copia versionada del OpenAPI: no depende de un checkout
privado adyacente ni descarga una especificación que pueda cambiar durante el build.

El job Windows ejecuta `delphi/scripts/ci-test.cmd`: compila el runtime package,
ejecuta las cinco suites offline y compila el ejemplo en ambas arquitecturas.
Si falla una compilación o prueba, **no se suben archivos a la release**.
Los pull requests no ejecutan código en el runner propio.

El job de publicación descarga el mismo artefacto validado y sube:

- `ecf-dgii-delphi-1.0.0.zip`
- `ecf-dgii-delphi-1.0.0.zip.sha256`

El ZIP contiene fuentes, metadatos Boss con rutas relativas al ZIP, licencia, logo,
OpenAPI, ejemplo y pruebas. La instalación desde Git usa el `boss.json` de la raíz
con `mainsrc: delphi/src/`; dentro del ZIP se ajusta a `src/` automáticamente.
Solo el job de publicación recibe `contents: write`. No necesita secretos externos.
Puedes reejecutar el workflow: reemplaza únicamente los archivos Delphi de esa release.

## Instalar desde Boss

Una vez disponible el tag, agrega esta dependencia al `boss.json` de la aplicación:

```json
{
  "dependencies": {
    "github.com/SSD-Smart-Software-Development-SRL/ecf_dgii": "delphi-v1.0.0"
  }
}
```

Luego ejecuta `boss install` desde la carpeta del proyecto. Conserva las demás
dependencias de tu manifiesto. Usa el tag exacto: el repositorio también contiene
tags de otros lenguajes. El código de Boss admite referencias Git exactas desde el
manifiesto; no se debe usar un rango semver genérico para este monorepo.

Boss consume directamente el tag Git, que ya existe al crear la release. La subida
del ZIP por Actions ocurre después de los checks; el workflow no oculta un tag cuyo
build haya fallado. Anuncia una versión después de que termine el workflow.

## Comprobar localmente

Desde la raíz del monorepo (Node.js 18+, Bash, zip y unzip):

```sh
node --test delphi/tests/*.test.mjs
RELEASE_TAG=delphi-v1.0.0 node delphi/scripts/check-release.mjs
bash delphi/scripts/package.sh
node delphi/scripts/check-package.mjs
```

Para actualizar el contrato, copia la especificación actual de la API a
`delphi/openapi-v1.json`, ejecuta `node delphi/scripts/generate.mjs` y confirma ambos
archivos. En Windows, `scripts\test.cmd dcc32` y `scripts\test.cmd dcc64` siguen
disponibles para pruebas manuales del compilador.

## Otros canales de Delphi

- **Boss**: distribución Git automatizada en esta entrega. [Boss](https://github.com/HashLoad/boss) y [Horse](https://github.com/HashLoad/horse/blob/master/boss.json) muestran este modelo de manifiesto.
- **DPM**: admite `dpm pack` y `dpm push` desde CI, con API key para su servidor. Es otro canal automatizable; este workflow no publica paquetes DPM. [CI de DPM](https://docs.delphi.dev/getting-started/continuous-integration.html).
- **GetIt**: catálogo integrado del IDE. La incorporación requiere la revisión de Embarcadero. Puede añadirse como canal adicional usando el ZIP generado por Actions; no es un requisito de la distribución por Boss. [Submit to GetIt](https://getitnow.embarcadero.com/submit/).
