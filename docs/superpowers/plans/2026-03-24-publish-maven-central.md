# Publish Java & Kotlin SDKs to Maven Central — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish `ecf-dgii-sdk-java` and `ecf-dgii-sdk-kotlin` to Maven Central via Sonatype Central Portal.

**Architecture:** Update build configs for both SDKs with Central Portal publishing plugins, rename Kotlin packages from `com.ecfx.sdk` to `dom.com.ssd.ecfx.sdk`, update CI/CD workflow, and guide user through manual account/key setup.

**Tech Stack:** Maven + `central-publishing-maven-plugin:0.10.0` (Java), Gradle + `com.vanniktech.maven.publish:0.36.0` (Kotlin), GitHub Actions, GPG

**Spec:** `docs/superpowers/specs/2026-03-24-publish-maven-central-design.md`

---

### Task 1: Java — Update `pom.xml` metadata and add release profile

**Files:**
- Modify: `java/pom.xml`

- [ ] **Step 1: Update metadata in `pom.xml`**

Change these fields:
- `artifactId`: `ecf-dgii-client` → `ecf-dgii-sdk-java`
- `name`: `ecf-dgii-sdk-java`
- `description`: `SDK de Java para la API de ECF DGII (comprobantes fiscales electrónicos de República Dominicana)`
- `url`: `https://github.com/puntoos/ecf_dgii_clients`
- License: Unlicense → MIT (`https://opensource.org/licenses/MIT`)
- Developer: Replace OpenAPI-Generator with Puntoos (`dev@puntoos.com`)
- SCM: Point all URLs to `github.com/puntoos/ecf_dgii_clients`

**Note:** `groupId` is already `dom.com.ssd.ecfx` — no change needed. Java source packages are under `dom.com.ssd.ecfx.client` which is fine (Maven groupId doesn't need to match Java package exactly).

**Note:** No `<distributionManagement>` section is needed. The `central-publishing-maven-plugin` with `<extensions>true</extensions>` intercepts the Maven deploy lifecycle automatically.

- [ ] **Step 2: Replace `sign-artifacts` profile with `release` profile**

**Important:** The current profile is named `sign-artifacts` but the CI workflow already references `-P release`. This rename fixes that mismatch. Replace the entire `<profiles>` section:

```xml
<profiles>
    <profile>
        <id>release</id>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-gpg-plugin</artifactId>
                    <version>3.2.1</version>
                    <executions>
                        <execution>
                            <id>sign-artifacts</id>
                            <phase>verify</phase>
                            <goals>
                                <goal>sign</goal>
                            </goals>
                            <configuration>
                                <gpgArguments>
                                    <arg>--pinentry-mode</arg>
                                    <arg>loopback</arg>
                                </gpgArguments>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
                <plugin>
                    <groupId>org.sonatype.central</groupId>
                    <artifactId>central-publishing-maven-plugin</artifactId>
                    <version>0.10.0</version>
                    <extensions>true</extensions>
                    <configuration>
                        <publishingServerId>central</publishingServerId>
                        <autoPublish>true</autoPublish>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

- [ ] **Step 3: Verify Java build compiles**

Run: `cd java && mvn -B package --no-transfer-progress`
Expected: BUILD SUCCESS

- [ ] **Step 4: Commit**

```bash
git add java/pom.xml
git commit -m "feat(java): update pom.xml metadata and add Central Portal release profile"
```

---

### Task 2: Java — Remove duplicate `build.gradle` and update `settings.gradle`

**Files:**
- Delete: `java/build.gradle`
- Modify: `java/settings.gradle`

- [ ] **Step 1: Delete `java/build.gradle`**

```bash
git rm java/build.gradle
```

- [ ] **Step 2: Update `java/settings.gradle`**

Change `rootProject.name` from `ecf-dgii-client` to `ecf-dgii-sdk-java`:

```groovy
rootProject.name = "ecf-dgii-sdk-java"
```

- [ ] **Step 3: Commit**

```bash
git add java/settings.gradle
git commit -m "chore(java): remove duplicate build.gradle, update settings.gradle artifact name"
```

---

### Task 3: Kotlin — Rewrite `build.gradle` with Vanniktech publishing plugin

**Files:**
- Modify: `kotlin/build.gradle`
- Modify: `kotlin/settings.gradle`

- [ ] **Step 1: Rewrite `kotlin/build.gradle`**

Replace the entire file with the following. This switches from the legacy `buildscript`/`apply plugin` pattern to the `plugins { }` DSL, which is required by the Vanniktech plugin:

```groovy
plugins {
    id 'org.jetbrains.kotlin.jvm' version '2.2.20'
    id 'org.jetbrains.kotlin.plugin.serialization' version '2.2.20'
    id 'com.diffplug.spotless' version '7.2.1'
    id 'com.vanniktech.maven.publish' version '0.36.0'
}

group 'dom.com.ssd.ecfx'
version '1.0.0'

repositories {
    mavenCentral()
}

// Spotless config
spotless {
    enforceCheck false
    format 'misc', {
        target '.gitignore'
        trimTrailingWhitespace()
        indentWithSpaces()
        endWithNewline()
    }
    kotlin {
        ktfmt()
    }
}

java {
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
}

test {
    useJUnitPlatform()
}

dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk8:2.2.20"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-core:1.10.2"
    implementation "org.jetbrains.kotlinx:kotlinx-serialization-json:1.9.0"
    implementation "com.squareup.okhttp3:okhttp:4.12.0"
    testImplementation "io.kotlintest:kotlintest-runner-junit5:3.4.2"
}

tasks.withType(org.jetbrains.kotlin.gradle.tasks.KotlinCompile).configureEach {
    kotlinOptions {
        jvmTarget = "11"
        freeCompilerArgs += "-Xopt-in=kotlinx.serialization.ExperimentalSerializationApi"
    }
}

// Maven Central publishing via Vanniktech plugin
mavenPublishing {
    publishToMavenCentral(com.vanniktech.maven.publish.SonatypeHost.CENTRAL_PORTAL)
    signAllPublications()
    coordinates('dom.com.ssd.ecfx', 'ecf-dgii-sdk-kotlin', version)

    pom {
        name = 'ECF DGII SDK Kotlin'
        description = 'SDK de Kotlin para la API de ECF DGII (comprobantes fiscales electrónicos de República Dominicana)'
        url = 'https://github.com/puntoos/ecf_dgii_clients'

        licenses {
            license {
                name = 'MIT License'
                url = 'https://opensource.org/licenses/MIT'
            }
        }

        developers {
            developer {
                id = 'puntoos'
                name = 'Puntoos'
                email = 'dev@puntoos.com'
            }
        }

        scm {
            connection = 'scm:git:git://github.com/puntoos/ecf_dgii_clients.git'
            developerConnection = 'scm:git:ssh://github.com/puntoos/ecf_dgii_clients.git'
            url = 'https://github.com/puntoos/ecf_dgii_clients'
        }
    }
}
```

**Note:** The Vanniktech plugin automatically creates sources and javadoc JARs, so the manual `java { withSourcesJar(); withJavadocJar() }` block is no longer needed.

- [ ] **Step 2: Update `kotlin/settings.gradle`**

Change `rootProject.name` from `ecf-dgii-sdk` to `ecf-dgii-sdk-kotlin`:

```groovy
rootProject.name = 'ecf-dgii-sdk-kotlin'
```

- [ ] **Step 3: Verify Kotlin build compiles**

Run: `cd kotlin && ./gradlew build`
Expected: BUILD SUCCESSFUL

- [ ] **Step 4: Commit**

```bash
git add kotlin/build.gradle kotlin/settings.gradle
git commit -m "feat(kotlin): replace OSSRH publishing with Vanniktech Central Portal plugin"
```

---

### Task 4: Kotlin — Rename package from `com.ecfx.sdk` to `dom.com.ssd.ecfx.sdk`

**Files:**
- Move: All files under `kotlin/src/main/kotlin/com/ecfx/sdk/` → `kotlin/src/main/kotlin/dom/com/ssd/ecfx/sdk/`
- Move: All files under `kotlin/src/test/kotlin/com/ecfx/sdk/` → `kotlin/src/test/kotlin/dom/com/ssd/ecfx/sdk/`
- Modify: ~500+ `package` declarations and ~1,200 `import` statements

This is a mechanical rename. Use a script:

- [ ] **Step 1: Move source directories**

```bash
cd kotlin
mkdir -p src/main/kotlin/dom/com/ssd/ecfx/sdk
cp -r src/main/kotlin/com/ecfx/sdk/* src/main/kotlin/dom/com/ssd/ecfx/sdk/
rm -rf src/main/kotlin/com/ecfx

mkdir -p src/test/kotlin/dom/com/ssd/ecfx/sdk
cp -r src/test/kotlin/com/ecfx/sdk/* src/test/kotlin/dom/com/ssd/ecfx/sdk/
rm -rf src/test/kotlin/com/ecfx
```

- [ ] **Step 2: Replace all package and import declarations**

```bash
cd kotlin
find src -name "*.kt" -exec sed -i '' 's/package com\.ecfx\.sdk/package dom.com.ssd.ecfx.sdk/g' {} +
find src -name "*.kt" -exec sed -i '' 's/import com\.ecfx\.sdk/import dom.com.ssd.ecfx.sdk/g' {} +
```

- [ ] **Step 3: Verify build still compiles**

Run: `cd kotlin && ./gradlew build`
Expected: BUILD SUCCESSFUL

- [ ] **Step 4: Commit**

```bash
cd kotlin
git add -A src/
git commit -m "refactor(kotlin): rename package from com.ecfx.sdk to dom.com.ssd.ecfx.sdk"
```

---

### Task 5: Update CI/CD workflow

**Files:**
- Modify: `.github/workflows/publish-maven.yml`

- [ ] **Step 1: Update deploy-java job**

Add tag filter to the `if` condition to prevent spurious deploys on non-maven releases:

```yaml
  deploy-java:
    if: github.event_name == 'release' && startsWith(github.event.release.tag_name, 'maven-v')
```

The rest of the Java deploy job is correct — `mvn -B deploy -P release` works because the `central-publishing-maven-plugin` with `<extensions>true</extensions>` intercepts the deploy lifecycle. The `server-id: central` in `setup-java` matches the `publishingServerId` in the plugin config.

- [ ] **Step 2: Update deploy-kotlin job**

Add tag filter and change the publish command and env var names:

```yaml
deploy-kotlin:
    if: github.event_name == 'release' && startsWith(github.event.release.tag_name, 'maven-v')
    runs-on: ubuntu-latest
    needs: [ build-kotlin ]
    defaults:
      run:
        working-directory: kotlin
    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK for publishing
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
          cache: gradle

      - name: Setup Gradle
        uses: gradle/actions/setup-gradle@v4

      - name: Publish to Maven Central
        run: ./gradlew publishAndReleaseToMavenCentral
        env:
          ORG_GRADLE_PROJECT_mavenCentralUsername: ${{ secrets.MAVEN_USERNAME }}
          ORG_GRADLE_PROJECT_mavenCentralPassword: ${{ secrets.MAVEN_PASSWORD }}
          ORG_GRADLE_PROJECT_signingInMemoryKey: ${{ secrets.GPG_PRIVATE_KEY }}
          ORG_GRADLE_PROJECT_signingInMemoryKeyPassword: ${{ secrets.GPG_PASSPHRASE }}
```

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/publish-maven.yml
git commit -m "ci: update Kotlin deploy to use Vanniktech plugin with Central Portal env vars"
```

---

### Task 6: Update READMEs (Spanish)

**Files:**
- Modify: `java/README.md`
- Modify: `kotlin/README.md`
- Modify: `README.md` (main)

- [ ] **Step 1: Update Java README**

- Change artifact ID in Maven snippet: `ecf-dgii-client` → `ecf-dgii-sdk-java`
- Change artifact ID in Gradle snippet: `ecf-dgii-client` → `ecf-dgii-sdk-java`
- Add Maven Central badge at top

- [ ] **Step 2: Update Kotlin README**

- Update package references from `com.ecfx.sdk` to `dom.com.ssd.ecfx.sdk` in all examples and model links
- Add installation snippets (Maven and Gradle) with `ecf-dgii-sdk-kotlin`
- Add Maven Central badge at top

- [ ] **Step 3: Update main README if needed**

- Update any artifact ID references

- [ ] **Step 4: Commit**

```bash
git add java/README.md kotlin/README.md README.md
git commit -m "docs: update READMEs with new artifact IDs and Maven Central badges"
```

---

### Task 7: USER ACTION — Sonatype Account, GPG Key, and GitHub Secrets

This task requires manual steps by the user. Claude should guide step-by-step.

- [ ] **Step 1: Create Sonatype Central Portal account**

Go to `https://central.sonatype.com` and sign up (can use GitHub login).

- [ ] **Step 2: Register namespace `dom.com.ssd.ecfx`**

In the portal, go to Namespaces → Add Namespace → enter `dom.com.ssd.ecfx`.
The portal will give you a DNS TXT record value.

- [ ] **Step 3: Add DNS TXT record**

Add the TXT record to `ecfx.ssd.com.do` (or parent domain as directed by portal).
Wait for verification.

- [ ] **Step 4: Generate GPG key**

```bash
gpg --full-generate-key
# Choose: RSA and RSA, 4096 bits, no expiration, your name and email
```

- [ ] **Step 5: Publish GPG public key to keyserver**

```bash
gpg --list-keys --keyid-format short
# Note the 8-char key ID
gpg --keyserver keyserver.ubuntu.com --send-keys <KEY_ID>
```

- [ ] **Step 6: Export GPG private key for CI**

```bash
gpg --armor --export-secret-keys <KEY_ID>
# Copy the full output (including BEGIN/END lines)
```

- [ ] **Step 7: Generate Central Portal token**

In the portal: Account → Generate User Token. Save the username and password values.

- [ ] **Step 8: Configure GitHub Secrets**

```bash
gh secret set MAVEN_USERNAME
gh secret set MAVEN_PASSWORD
gh secret set GPG_PRIVATE_KEY
gh secret set GPG_PASSPHRASE
```

---

### Task 8: First publish — Create release

> **BLOCKER:** Task 7 (Sonatype account, GPG key, GitHub secrets) MUST be fully completed before this task. The release will fail without valid credentials.

- [ ] **Step 1: Verify both builds pass**

```bash
cd java && mvn -B package --no-transfer-progress
cd ../kotlin && ./gradlew build
```

- [ ] **Step 2: Create GitHub release to trigger deploy**

```bash
gh release create maven-v1.0.0 --title "Maven v1.0.0" --notes "Primera publicación de ecf-dgii-sdk-java y ecf-dgii-sdk-kotlin en Maven Central."
```

- [ ] **Step 3: Monitor CI/CD workflow**

```bash
gh run list --workflow=publish-maven.yml --limit=1
gh run watch
```

- [ ] **Step 4: Verify on Maven Central**

After CI completes, check `https://central.sonatype.com` for the published artifacts.
They should also appear on `https://search.maven.org` within a few hours.
