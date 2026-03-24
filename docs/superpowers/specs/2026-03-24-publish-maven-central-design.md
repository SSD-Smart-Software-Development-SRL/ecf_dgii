# Publicación de SDK Java y Kotlin en Maven Central

## Resumen

Publicar los SDKs de Java y Kotlin del proyecto ECF DGII en Maven Central a través del nuevo Sonatype Central Portal (`central.sonatype.com`). Esto incluye configuración de cuenta, firma GPG, estandarización de metadatos, actualización de build files, y CI/CD automatizado.

## Decisiones de Diseño

| Decisión | Valor |
|----------|-------|
| Repositorio | Maven Central (via Sonatype Central Portal) |
| Group ID | `dom.com.ssd.ecfx` (ambos paquetes) |
| Artifact ID Java | `ecf-dgii-sdk-java` |
| Artifact ID Kotlin | `ecf-dgii-sdk-kotlin` |
| Versión inicial | `1.0.0` |
| Licencia | MIT |
| Build Java | Maven (`pom.xml`) — eliminar `build.gradle` duplicado |
| Build Kotlin | Gradle con plugin `com.vanniktech.maven.publish` |
| CI/CD | GitHub Actions, deploy en release tag `maven-v*` |
| Idioma READMEs | Español |

## 1. Configuración de Cuenta y Namespace

### 1.1 Sonatype Central Portal

1. Crear cuenta en `central.sonatype.com`
2. Registrar namespace `dom.com.ssd.ecfx`
3. Verificar dominio `ecfx.ssd.com.do` con registro DNS TXT (el portal provee el valor exacto)
4. Esperar verificación (minutos a un día)

### 1.2 GPG Key

1. Generar clave GPG: `gpg --full-generate-key` (RSA 4096)
2. Publicar clave pública a keyserver: `gpg --keyserver keyserver.ubuntu.com --send-keys <KEY_ID>`
3. Exportar clave privada armored para CI: `gpg --armor --export-secret-keys <KEY_ID>`

### 1.3 GitHub Secrets

| Secret | Descripción |
|--------|-------------|
| `MAVEN_USERNAME` | Token username del Central Portal |
| `MAVEN_PASSWORD` | Token password del Central Portal |
| `GPG_PRIVATE_KEY` | Clave privada GPG (armored) |
| `GPG_PASSPHRASE` | Passphrase de la clave GPG |

## 2. Cambios en Java SDK

### 2.1 `pom.xml` — Actualizar metadatos

**Cambios:**
- `artifactId`: `ecf-dgii-client` → `ecf-dgii-sdk-java`
- `name`: `ecf-dgii-sdk-java`
- `description`: `SDK de Java para la API de ECF DGII (comprobantes fiscales electrónicos de República Dominicana)`
- `url`: `https://github.com/puntoos/ecf_dgii_clients`
- Licencia: Unlicense → MIT
- Developer: OpenAPI-Generator Contributors → Puntoos (`dev@puntoos.com`)
- SCM: Apuntar a `github.com/puntoos/ecf_dgii_clients`

### 2.2 `pom.xml` — Agregar perfil `release`

Reemplazar el perfil `sign-artifacts` con un perfil `release` que incluya:

1. **`maven-gpg-plugin`** (`org.apache.maven.plugins:maven-gpg-plugin:3.2.1`) — firma de artefactos con GPG
   - Configurar `--pinentry-mode loopback` para CI no-interactivo:
   ```xml
   <configuration>
       <gpgArguments>
           <arg>--pinentry-mode</arg>
           <arg>loopback</arg>
       </gpgArguments>
   </configuration>
   ```
   - El passphrase se pasa via env var `GPG_PASSPHRASE` (configurado por `actions/setup-java`)

2. **`central-publishing-maven-plugin`** (`org.sonatype.central:central-publishing-maven-plugin:0.10.0`) — publicación al Central Portal
   - `<extensions>true</extensions>` — **requerido** para que reemplace el mecanismo de deploy default de Maven
   - `publishingServerId`: `central` — **debe coincidir** con el `server-id` en el step `actions/setup-java` del workflow
   - `autoPublish`: `true` (publica automáticamente después de validación)

**Nota:** Los plugins `maven-source-plugin` y `maven-javadoc-plugin` se mantienen en el build section principal (no mover al perfil) para que `mvn install` local también genere los JARs de fuentes y javadoc.

**Nota sobre paquetes Java:** El group ID es `dom.com.ssd.ecfx` y los paquetes Java están bajo `dom.com.ssd.ecfx.client`. No es necesario renombrar los paquetes Java — el group ID de Maven no requiere coincidir exactamente con la estructura de paquetes.

### 2.3 Eliminar `java/build.gradle`

El `build.gradle` del módulo Java es redundante con `pom.xml` y no tiene configuración de publicación. Eliminarlo para evitar confusión.

## 3. Cambios en Kotlin SDK

### 3.1 `build.gradle` — Plugin de publicación

Reemplazar la configuración manual de `maven-publish` + `signing` + OSSRH con el plugin `com.vanniktech.maven.publish`:

```groovy
plugins {
    id 'com.vanniktech.maven.publish' version '0.36.0'
}

mavenPublishing {
    publishToMavenCentral(SonatypeHost.CENTRAL_PORTAL, automaticRelease = true)
    signAllPublications()

    coordinates('dom.com.ssd.ecfx', 'ecf-dgii-sdk-kotlin', '1.0.0')

    pom {
        name = 'ECF DGII SDK Kotlin'
        description = 'SDK de Kotlin para la API de ECF DGII (comprobantes fiscales electrónicos de República Dominicana)'
        url = 'https://github.com/puntoos/ecf_dgii_clients'
        // ... licencia MIT, developer, SCM
    }
}
```

**Variables de entorno esperadas por el plugin:**
- `ORG_GRADLE_PROJECT_mavenCentralUsername` — Token username
- `ORG_GRADLE_PROJECT_mavenCentralPassword` — Token password
- `ORG_GRADLE_PROJECT_signingInMemoryKey` — Clave GPG privada
- `ORG_GRADLE_PROJECT_signingInMemoryKeyPassword` — Passphrase GPG

### 3.2 Cambio de Group ID y Package

- Group ID en `build.gradle`: `com.ecfx` → `dom.com.ssd.ecfx`
- Source package: `com.ecfx.sdk` → `dom.com.ssd.ecfx.sdk`
- Mover archivos fuente de `src/main/kotlin/com/ecfx/sdk/` a `src/main/kotlin/dom/com/ssd/ecfx/sdk/`
- Mover archivos de test de `src/test/kotlin/com/ecfx/sdk/` a `src/test/kotlin/dom/com/ssd/ecfx/sdk/`
- Actualizar todos los `import` y `package` declarations en fuentes y tests
- Verificar y actualizar `settings.gradle` si `rootProject.name` necesita cambio

### 3.3 Eliminar configuración vieja

Eliminar del `build.gradle`:
- Bloque `publishing { ... }` manual
- Bloque `signing { ... }` manual
- Plugins `maven-publish` y `signing` manuales

## 4. CI/CD — GitHub Actions

### 4.1 Actualizar `.github/workflows/publish-maven.yml`

**deploy-java:**
```yaml
- name: Set up JDK for publishing
  uses: actions/setup-java@v4
  with:
    java-version: '17'
    distribution: 'temurin'
    cache: maven
    server-id: central
    server-username: MAVEN_USERNAME
    server-password: MAVEN_PASSWORD
    gpg-private-key: ${{ secrets.GPG_PRIVATE_KEY }}
    gpg-passphrase: GPG_PASSPHRASE

- name: Publish to Maven Central
  run: mvn -B deploy --no-transfer-progress -P release
  env:
    MAVEN_USERNAME: ${{ secrets.MAVEN_USERNAME }}
    MAVEN_PASSWORD: ${{ secrets.MAVEN_PASSWORD }}
    GPG_PASSPHRASE: ${{ secrets.GPG_PASSPHRASE }}
```

**Nota:** El `server-id: central` en `setup-java` debe coincidir con el `publishingServerId` del `central-publishing-maven-plugin` en el `pom.xml`. El comando `mvn deploy` funciona porque el plugin usa `<extensions>true</extensions>`.

**deploy-kotlin** (actualizar env vars y comando — los actuales usan nombres incorrectos):
```yaml
- name: Publish to Maven Central
  run: ./gradlew publishAndReleaseToMavenCentral
  env:
    ORG_GRADLE_PROJECT_mavenCentralUsername: ${{ secrets.MAVEN_USERNAME }}
    ORG_GRADLE_PROJECT_mavenCentralPassword: ${{ secrets.MAVEN_PASSWORD }}
    ORG_GRADLE_PROJECT_signingInMemoryKey: ${{ secrets.GPG_PRIVATE_KEY }}
    ORG_GRADLE_PROJECT_signingInMemoryKeyPassword: ${{ secrets.GPG_PASSPHRASE }}
```

## 5. Documentación

### 5.1 READMEs (en español)

Actualizar ambos READMEs:
- Nuevos artifact IDs en snippets de instalación Maven/Gradle
- Group ID correcto en Kotlin README
- Agregar badge de Maven Central
- Mantener todo el contenido en español

### 5.2 Main README

- Actualizar nombres de paquetes y links si referencian artifact IDs viejos

## 6. Checklist de Publicación (primera vez)

Pasos manuales que el usuario debe completar:

1. [ ] Crear cuenta en `central.sonatype.com`
2. [ ] Registrar namespace `dom.com.ssd.ecfx`
3. [ ] Agregar registro DNS TXT a `ecfx.ssd.com.do`
4. [ ] Esperar verificación del namespace
5. [ ] Generar clave GPG y publicar a keyserver
6. [ ] Generar token de autenticación en Central Portal
7. [ ] Configurar GitHub Secrets (`MAVEN_USERNAME`, `MAVEN_PASSWORD`, `GPG_PRIVATE_KEY`, `GPG_PASSPHRASE`)
8. [ ] Crear GitHub Release con tag `maven-v1.0.0`
9. [ ] Verificar que los paquetes aparezcan en `search.maven.org`

## Artefactos Resultantes

Después de la publicación, los usuarios podrán agregar las dependencias:

**Java (Maven):**
```xml
<dependency>
    <groupId>dom.com.ssd.ecfx</groupId>
    <artifactId>ecf-dgii-sdk-java</artifactId>
    <version>1.0.0</version>
</dependency>
```

**Kotlin (Gradle):**
```kotlin
implementation("dom.com.ssd.ecfx:ecf-dgii-sdk-kotlin:1.0.0")
```

## 7. Troubleshooting

Problemas comunes en la primera publicación:

| Problema | Solución |
|----------|----------|
| Validación falla por javadoc faltante | Verificar que `maven-javadoc-plugin` (Java) y `withJavadocJar()` (Kotlin) estén configurados |
| Validación falla por artefactos sin firma | Verificar que la clave GPG esté publicada en keyserver y que los secrets estén correctos |
| Namespace rechazado | Verificar que el registro DNS TXT sea exactamente el valor provisto por el portal |
| Clave GPG no encontrada en keyserver | Esperar ~10 min después de publicar, o intentar otro keyserver (`keys.openpgp.org`) |
| `mvn deploy` falla con 401 | Verificar que `server-id: central` coincida en workflow y `pom.xml`, y que el token del portal sea válido |
