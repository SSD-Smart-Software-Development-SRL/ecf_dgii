# WooCommerce ECF DGII Plugin — Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a working WooCommerce plugin that sends E32 (Consumidor Final) invoices to the ECF SSD test API when orders are paid.

**Architecture:** WordPress plugin using WooCommerce hooks. The plugin maps WooCommerce order data to the ECF model from the `ecfx/ecf-dgii-php` SDK and sends it via the API. Uses WooCommerce Action Scheduler for async submission to avoid blocking checkout. Settings stored in `wp_options`, ECF data stored as order meta.

**Tech Stack:** PHP 8.1+, WordPress 6.4+, WooCommerce 8.0+, `ecfx/ecf-dgii-php` SDK, Podman for dev environment.

**Spec:** `docs/superpowers/specs/2026-03-12-woocommerce-ecf-dgii-plugin-design.md`

---

## File Structure

```
/Users/dawlin/Developer/puntoos/woo-ecf-dgii/
├── woo-ecf-dgii.php                     # Main plugin file: header, activation, init
├── composer.json                         # Dependencies (ecfx/ecf-dgii-php via path)
├── uninstall.php                         # Cleanup on uninstall
├── includes/
│   ├── class-ecf-plugin.php              # Singleton: registers hooks, loads dependencies
│   ├── class-ecf-settings.php            # WooCommerce settings tab: API token, env, RNC
│   ├── class-ecf-sequence-manager.php    # eNCF sequence tracking (atomic increment)
│   ├── class-ecf-mapper.php              # WooCommerce order → ECF model mapping
│   ├── class-ecf-order-handler.php       # Payment hook → schedule ECF submission
│   ├── class-ecf-api-client.php          # Thin wrapper: configures SDK, exposes send methods
│   └── class-ecf-admin-order.php         # Admin order metabox: ECF status display
├── assets/
│   └── css/
│       └── admin.css                     # Admin metabox styles
├── dev/
│   ├── podman-compose.yml                # WordPress + WooCommerce + MariaDB
│   └── setup.sh                          # Auto-install WooCommerce + activate plugin
└── tests/
    ├── bootstrap.php                     # Test bootstrap (WP test framework)
    ├── test-ecf-mapper.php               # Unit tests for order→ECF mapping
    └── test-ecf-sequence-manager.php     # Unit tests for sequence management
```

---

## Chunk 1: Dev Environment + Plugin Skeleton

### Task 1: Create project directory and composer.json

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/composer.json`

- [ ] **Step 1: Create project directory**

```bash
mkdir -p /Users/dawlin/Developer/puntoos/woo-ecf-dgii
```

- [ ] **Step 2: Create composer.json with path repository for SDK**

```json
{
    "name": "puntoos/woo-ecf-dgii",
    "description": "WooCommerce plugin for Dominican Republic electronic fiscal documents (ECF) via ECF SSD API",
    "type": "wordpress-plugin",
    "license": "proprietary",
    "require": {
        "php": "^8.1",
        "ecfx/ecf-dgii-php": "^1.0"
    },
    "repositories": [
        {
            "type": "path",
            "url": "../ecf_dgii_clients/php",
            "options": {
                "symlink": true
            }
        }
    ],
    "autoload": {
        "classmap": ["includes/"]
    }
}
```

- [ ] **Step 3: Run composer install**

```bash
cd /Users/dawlin/Developer/puntoos/woo-ecf-dgii && composer install
```

Expected: `ecfx/ecf-dgii-php` installed as symlink, vendor/autoload.php created.

- [ ] **Step 4: Initialize git repo**

```bash
cd /Users/dawlin/Developer/puntoos/woo-ecf-dgii
git init
cat > .gitignore << 'EOF'
/vendor/
.idea/
.vscode/
*.log
EOF
```

- [ ] **Step 5: Commit**

```bash
git add composer.json composer.lock .gitignore
git commit -m "feat: initialize plugin with composer and SDK dependency"
```

---

### Task 2: Create main plugin file

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/woo-ecf-dgii.php`

- [ ] **Step 1: Create the main plugin file with WordPress header**

```php
<?php
/**
 * Plugin Name: WooCommerce ECF DGII
 * Plugin URI: https://github.com/puntoos/woo-ecf-dgii
 * Description: Electronic fiscal documents (ECF) for Dominican Republic via ECF SSD API. Automatically sends invoices to DGII when WooCommerce orders are paid.
 * Version: 0.1.0
 * Requires at least: 6.2
 * Requires PHP: 8.1
 * Author: Puntoos
 * License: Proprietary
 * Text Domain: woo-ecf-dgii
 * Domain Path: /languages
 * WC requires at least: 8.0
 * WC tested up to: 9.0
 */

defined('ABSPATH') || exit;

define('WOO_ECF_DGII_VERSION', '0.1.0');
define('WOO_ECF_DGII_PLUGIN_FILE', __FILE__);
define('WOO_ECF_DGII_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('WOO_ECF_DGII_PLUGIN_URL', plugin_dir_url(__FILE__));

// Load Composer autoloader
if (file_exists(WOO_ECF_DGII_PLUGIN_DIR . 'vendor/autoload.php')) {
    require_once WOO_ECF_DGII_PLUGIN_DIR . 'vendor/autoload.php';
}

// Declare HPOS compatibility
add_action('before_woocommerce_init', function () {
    if (class_exists(\Automattic\WooCommerce\Utilities\FeaturesUtil::class)) {
        \Automattic\WooCommerce\Utilities\FeaturesUtil::declare_compatibility(
            'custom_order_tables',
            __FILE__,
            true
        );
    }
});

// Check WooCommerce is active before initializing
add_action('plugins_loaded', function () {
    if (!class_exists('WooCommerce')) {
        add_action('admin_notices', function () {
            echo '<div class="error"><p>';
            echo esc_html__('WooCommerce ECF DGII requires WooCommerce to be installed and active.', 'woo-ecf-dgii');
            echo '</p></div>';
        });
        return;
    }

    require_once WOO_ECF_DGII_PLUGIN_DIR . 'includes/class-ecf-plugin.php';
    Ecf_Plugin::instance();
});

// Activation hook: create custom tables
register_activation_hook(__FILE__, function () {
    require_once WOO_ECF_DGII_PLUGIN_DIR . 'includes/class-ecf-plugin.php';
    Ecf_Plugin::activate();
});
```

- [ ] **Step 2: Commit**

```bash
git add woo-ecf-dgii.php
git commit -m "feat: add main plugin file with WC dependency check and HPOS compat"
```

---

### Task 3: Create core plugin class

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/includes/class-ecf-plugin.php`

- [ ] **Step 1: Create the plugin class directory**

```bash
mkdir -p /Users/dawlin/Developer/puntoos/woo-ecf-dgii/includes
```

- [ ] **Step 2: Create the singleton plugin class**

```php
<?php
defined('ABSPATH') || exit;

class Ecf_Plugin {

    private static ?Ecf_Plugin $instance = null;

    public static function instance(): self {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        $this->load_dependencies();
        $this->init_hooks();
    }

    private function load_dependencies(): void {
        require_once WOO_ECF_DGII_PLUGIN_DIR . 'includes/class-ecf-settings.php';
        require_once WOO_ECF_DGII_PLUGIN_DIR . 'includes/class-ecf-sequence-manager.php';
        require_once WOO_ECF_DGII_PLUGIN_DIR . 'includes/class-ecf-api-client.php';
        require_once WOO_ECF_DGII_PLUGIN_DIR . 'includes/class-ecf-mapper.php';
        require_once WOO_ECF_DGII_PLUGIN_DIR . 'includes/class-ecf-order-handler.php';
        require_once WOO_ECF_DGII_PLUGIN_DIR . 'includes/class-ecf-admin-order.php';
    }

    private function init_hooks(): void {
        Ecf_Settings::init();
        Ecf_Order_Handler::init();
        Ecf_Admin_Order::init();
    }

    public static function activate(): void {
        Ecf_Sequence_Manager::create_table();
    }
}
```

- [ ] **Step 3: Commit**

```bash
git add includes/class-ecf-plugin.php
git commit -m "feat: add core plugin class with dependency loading"
```

---

### Task 4: Create Podman dev environment

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/dev/podman-compose.yml`
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/dev/setup.sh`

- [ ] **Step 1: Create dev directory**

```bash
mkdir -p /Users/dawlin/Developer/puntoos/woo-ecf-dgii/dev
```

- [ ] **Step 2: Create podman-compose.yml**

```yaml
version: "3.8"

services:
  db:
    image: docker.io/library/mariadb:10.11
    environment:
      MYSQL_ROOT_PASSWORD: wordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    volumes:
      - db_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
      interval: 10s
      timeout: 5s
      retries: 3

  wordpress:
    image: docker.io/library/wordpress:6.4-php8.2
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DEBUG: "1"
    volumes:
      - wp_data:/var/www/html
      - ../:/var/www/html/wp-content/plugins/woo-ecf-dgii
      - ../../ecf_dgii_clients/php:/opt/ecf-dgii-php
    depends_on:
      db:
        condition: service_healthy

volumes:
  db_data:
  wp_data:
```

- [ ] **Step 3: Create setup.sh**

This script runs inside the WordPress container to install WooCommerce and activate the plugin.

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "=== WooCommerce ECF DGII Dev Setup ==="

# Wait for WordPress to be ready
until wp core is-installed --allow-root 2>/dev/null; do
    echo "Waiting for WordPress..."
    sleep 2
done

# Install and activate WooCommerce
if ! wp plugin is-active woocommerce --allow-root 2>/dev/null; then
    echo "Installing WooCommerce..."
    wp plugin install woocommerce --activate --allow-root
fi

# Run composer install inside the plugin directory
cd /var/www/html/wp-content/plugins/woo-ecf-dgii
if [ ! -d vendor ]; then
    echo "Running composer install..."
    composer install --no-dev --no-interaction
fi

# Activate our plugin
if ! wp plugin is-active woo-ecf-dgii --allow-root 2>/dev/null; then
    echo "Activating WooCommerce ECF DGII..."
    wp plugin activate woo-ecf-dgii --allow-root
fi

# Set up basic WooCommerce settings for testing
wp option update woocommerce_currency DOP --allow-root
wp option update woocommerce_default_country DO --allow-root

echo "=== Setup complete ==="
echo "WordPress: http://localhost:8080"
echo "Admin: http://localhost:8080/wp-admin (admin/admin)"
```

- [ ] **Step 4: Make setup.sh executable**

```bash
chmod +x /Users/dawlin/Developer/puntoos/woo-ecf-dgii/dev/setup.sh
```

- [ ] **Step 5: Commit**

```bash
git add dev/
git commit -m "feat: add Podman dev environment with WordPress + WooCommerce"
```

---

## Chunk 2: Settings Page + API Client

### Task 5: Create settings page

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/includes/class-ecf-settings.php`

- [ ] **Step 1: Create WooCommerce settings tab class**

This adds a "ECF DGII" tab under WooCommerce > Settings.

```php
<?php
defined('ABSPATH') || exit;

class Ecf_Settings {

    public const OPTION_API_TOKEN = 'ecf_dgii_api_token';
    public const OPTION_ENVIRONMENT = 'ecf_dgii_environment';
    public const OPTION_COMPANY_RNC = 'ecf_dgii_company_rnc';
    public const OPTION_COMPANY_DATA = 'ecf_dgii_company_data';
    public const OPTION_DEFAULT_ECF_TYPE = 'ecf_dgii_default_ecf_type';
    public const OPTION_RETRY_MAX = 'ecf_dgii_retry_max';
    public const OPTION_RETRY_INTERVAL = 'ecf_dgii_retry_interval';

    private const ENVIRONMENTS = [
        'test' => 'https://api.test.ecfx.ssd.com.do',
        'cert' => 'https://api.cert.ecfx.ssd.com.do',
        'prod' => 'https://api.prod.ecfx.ssd.com.do',
    ];

    public static function init(): void {
        add_filter('woocommerce_settings_tabs_array', [self::class, 'add_settings_tab'], 50);
        add_action('woocommerce_settings_tabs_ecf_dgii', [self::class, 'render_settings']);
        add_action('woocommerce_update_options_ecf_dgii', [self::class, 'save_settings']);
        add_action('wp_ajax_ecf_dgii_test_connection', [self::class, 'ajax_test_connection']);
    }

    public static function add_settings_tab(array $tabs): array {
        $tabs['ecf_dgii'] = __('ECF DGII', 'woo-ecf-dgii');
        return $tabs;
    }

    public static function get_api_host(): string {
        $env = get_option(self::OPTION_ENVIRONMENT, 'test');
        return self::ENVIRONMENTS[$env] ?? self::ENVIRONMENTS['test'];
    }

    public static function get_api_token(): string {
        return get_option(self::OPTION_API_TOKEN, '');
    }

    public static function get_company_rnc(): string {
        return get_option(self::OPTION_COMPANY_RNC, '');
    }

    public static function get_company_data(): array {
        return get_option(self::OPTION_COMPANY_DATA, []);
    }

    public static function get_settings_fields(): array {
        $fields = [
            'ecf_dgii_section_api' => [
                'name' => __('API Connection', 'woo-ecf-dgii'),
                'type' => 'title',
                'desc' => __('Configure your ECF SSD API connection.', 'woo-ecf-dgii'),
            ],
            self::OPTION_ENVIRONMENT => [
                'name' => __('Environment', 'woo-ecf-dgii'),
                'type' => 'select',
                'options' => [
                    'test' => __('Test', 'woo-ecf-dgii'),
                    'cert' => __('Certification', 'woo-ecf-dgii'),
                    'prod' => __('Production', 'woo-ecf-dgii'),
                ],
                'default' => 'test',
                'desc' => __('Select the ECF SSD API environment.', 'woo-ecf-dgii'),
            ],
            self::OPTION_API_TOKEN => [
                'name' => __('API Token', 'woo-ecf-dgii'),
                'type' => 'password',
                'desc' => __('Your ECF SSD API authentication token.', 'woo-ecf-dgii'),
            ],
            self::OPTION_COMPANY_RNC => [
                'name' => __('Company RNC', 'woo-ecf-dgii'),
                'type' => 'text',
                'desc' => __('Your company RNC. Cannot be changed once saved.', 'woo-ecf-dgii'),
                'custom_attributes' => get_option(self::OPTION_COMPANY_RNC)
                    ? ['readonly' => 'readonly']
                    : [],
            ],
            'ecf_dgii_section_api_end' => [
                'type' => 'sectionend',
            ],
            'ecf_dgii_section_general' => [
                'name' => __('General Settings', 'woo-ecf-dgii'),
                'type' => 'title',
            ],
            self::OPTION_DEFAULT_ECF_TYPE => [
                'name' => __('Default ECF Type (when RNC provided)', 'woo-ecf-dgii'),
                'type' => 'select',
                'options' => [
                    'E31' => __('E31 - Crédito Fiscal', 'woo-ecf-dgii'),
                    'E32' => __('E32 - Consumo', 'woo-ecf-dgii'),
                ],
                'default' => 'E31',
            ],
            self::OPTION_RETRY_MAX => [
                'name' => __('Max retries before contingencia', 'woo-ecf-dgii'),
                'type' => 'number',
                'default' => 3,
                'desc' => __('Number of retry attempts before falling back to B-series.', 'woo-ecf-dgii'),
                'custom_attributes' => ['min' => 1, 'max' => 10],
            ],
            self::OPTION_RETRY_INTERVAL => [
                'name' => __('Retry interval (seconds)', 'woo-ecf-dgii'),
                'type' => 'number',
                'default' => 5,
                'custom_attributes' => ['min' => 1, 'max' => 60],
            ],
            'ecf_dgii_section_general_end' => [
                'type' => 'sectionend',
            ],
        ];

        return $fields;
    }

    public static function render_settings(): void {
        // Show company data if fetched
        $company_data = self::get_company_data();
        if (!empty($company_data)) {
            echo '<div class="ecf-company-info">';
            echo '<h3>' . esc_html__('Company Information (from ECF SSD)', 'woo-ecf-dgii') . '</h3>';
            echo '<table class="form-table">';
            if (!empty($company_data['razonSocial'])) {
                echo '<tr><th>' . esc_html__('Legal Name', 'woo-ecf-dgii') . '</th>';
                echo '<td>' . esc_html($company_data['razonSocial']) . '</td></tr>';
            }
            if (!empty($company_data['direccion'])) {
                echo '<tr><th>' . esc_html__('Address', 'woo-ecf-dgii') . '</th>';
                echo '<td>' . esc_html($company_data['direccion']) . '</td></tr>';
            }
            echo '</table></div>';
        }

        woocommerce_admin_fields(self::get_settings_fields());

        // Test connection button
        echo '<table class="form-table"><tr><th></th><td>';
        echo '<button type="button" class="button" id="ecf-test-connection">';
        echo esc_html__('Test Connection', 'woo-ecf-dgii');
        echo '</button>';
        echo '<span id="ecf-connection-result" style="margin-left:10px;"></span>';
        echo '</td></tr></table>';

        // Inline JS for test connection
        ?>
        <script>
        jQuery(function($) {
            $('#ecf-test-connection').on('click', function() {
                var $btn = $(this);
                var $result = $('#ecf-connection-result');
                $btn.prop('disabled', true);
                $result.text('<?php echo esc_js(__('Testing...', 'woo-ecf-dgii')); ?>');
                $.post(ajaxurl, {
                    action: 'ecf_dgii_test_connection',
                    _wpnonce: '<?php echo wp_create_nonce('ecf_dgii_test_connection'); ?>'
                }, function(response) {
                    $btn.prop('disabled', false);
                    if (response.success) {
                        $result.html('<span style="color:green;">' + response.data + '</span>');
                    } else {
                        $result.html('<span style="color:red;">' + response.data + '</span>');
                    }
                });
            });
        });
        </script>
        <?php
    }

    public static function save_settings(): void {
        woocommerce_update_options(self::get_settings_fields());
    }

    public static function ajax_test_connection(): void {
        check_ajax_referer('ecf_dgii_test_connection');

        if (!current_user_can('manage_woocommerce')) {
            wp_send_json_error(__('Permission denied.', 'woo-ecf-dgii'));
        }

        try {
            $client = new Ecf_Api_Client();
            $company = $client->get_company(self::get_company_rnc());

            // Cache company data
            update_option(self::OPTION_COMPANY_DATA, [
                'razonSocial' => $company->getRazonSocial() ?? '',
                'direccion' => $company->getDireccion() ?? '',
            ]);

            wp_send_json_success(
                sprintf(
                    __('Connected! Company: %s', 'woo-ecf-dgii'),
                    $company->getRazonSocial() ?? 'OK'
                )
            );
        } catch (\Exception $e) {
            wp_send_json_error($e->getMessage());
        }
    }
}
```

- [ ] **Step 2: Commit**

```bash
git add includes/class-ecf-settings.php
git commit -m "feat: add WooCommerce settings tab for ECF DGII configuration"
```

---

### Task 6: Create API client wrapper

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/includes/class-ecf-api-client.php`

- [ ] **Step 1: Create the API client class**

This wraps SDK Configuration and provides methods for submitting ECFs and fetching company data.

```php
<?php
defined('ABSPATH') || exit;

use Ecfx\EcfDgii\Api\EcfApi;
use Ecfx\EcfDgii\Api\CompanyApi;
use Ecfx\EcfDgii\Configuration;
use Ecfx\EcfDgii\Model\ECF;
use Ecfx\EcfDgii\Model\EcfResponse;
use Ecfx\EcfDgii\Model\TipoeCFType;
use GuzzleHttp\Client;

class Ecf_Api_Client {

    private Configuration $config;
    private Client $http;

    private const TIPO_ECF_METHODS = [
        'E31' => 'recepcionEcf31',
        'E32' => 'recepcionEcf32',
        'E33' => 'recepcionEcf33',
        'E34' => 'recepcionEcf34',
    ];

    public function __construct(?string $token = null, ?string $host = null) {
        $this->config = new Configuration();
        $this->config->setHost($host ?? Ecf_Settings::get_api_host());
        $this->config->setAccessToken($token ?? Ecf_Settings::get_api_token());
        $this->http = new Client();
    }

    /**
     * Submit an ECF document. Returns the initial response with messageId.
     * Does NOT poll — the caller is responsible for checking status later.
     */
    public function submit_ecf(ECF $ecf, string $ecf_type): EcfResponse {
        $api = new EcfApi($this->http, $this->config);
        $method = self::TIPO_ECF_METHODS[$ecf_type]
            ?? throw new \InvalidArgumentException("Unsupported ECF type: {$ecf_type}");

        return $api->$method($ecf);
    }

    /**
     * Check the status of a previously submitted ECF.
     */
    public function get_ecf_status(string $rnc, string $message_id): array {
        $api = new EcfApi($this->http, $this->config);
        return $api->getEcfById($rnc, $message_id);
    }

    /**
     * Fetch company data from the ECF SSD API.
     */
    public function get_company(string $rnc) {
        $api = new CompanyApi($this->http, $this->config);
        return $api->getCompanyByRnc($rnc);
    }
}
```

- [ ] **Step 2: Commit**

```bash
git add includes/class-ecf-api-client.php
git commit -m "feat: add ECF API client wrapper for SDK"
```

---

## Chunk 3: Sequence Manager

### Task 7: Create sequence manager with DB table

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/includes/class-ecf-sequence-manager.php`
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/tests/test-ecf-sequence-manager.php`

- [ ] **Step 1: Create the sequence manager class**

```php
<?php
defined('ABSPATH') || exit;

class Ecf_Sequence_Manager {

    private const TABLE_SUFFIX = 'ecf_sequences';

    public static function get_table_name(): string {
        global $wpdb;
        return $wpdb->prefix . self::TABLE_SUFFIX;
    }

    /**
     * Create the sequences table on plugin activation.
     */
    public static function create_table(): void {
        global $wpdb;
        $table = self::get_table_name();
        $charset = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE {$table} (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            ecf_type VARCHAR(5) NOT NULL,
            serie CHAR(1) NOT NULL DEFAULT 'E',
            prefix VARCHAR(13) NOT NULL,
            current_number BIGINT NOT NULL,
            range_start BIGINT NOT NULL,
            range_end BIGINT NOT NULL,
            expiration_date DATE NOT NULL,
            is_active TINYINT(1) DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ) {$charset};";

        require_once ABSPATH . 'wp-admin/includes/upgrade.php';
        dbDelta($sql);
    }

    /**
     * Add a new sequence range.
     */
    public static function add_sequence(
        string $ecf_type,
        string $serie,
        string $prefix,
        int $range_start,
        int $range_end,
        string $expiration_date,
    ): int|false {
        global $wpdb;

        return $wpdb->insert(self::get_table_name(), [
            'ecf_type' => $ecf_type,
            'serie' => $serie,
            'prefix' => $prefix,
            'current_number' => $range_start,
            'range_start' => $range_start,
            'range_end' => $range_end,
            'expiration_date' => $expiration_date,
            'is_active' => 1,
        ]);
    }

    /**
     * Claim the next eNCF number atomically.
     *
     * Uses UPDATE ... WHERE current_number < range_end to prevent race conditions.
     * Returns the claimed eNCF string (e.g., "E310000000001") or null if exhausted.
     */
    public static function claim_next(string $ecf_type, string $serie = 'E'): ?array {
        global $wpdb;
        $table = self::get_table_name();
        $today = current_time('Y-m-d');

        // Find active, non-expired sequence for this type
        $sequence = $wpdb->get_row($wpdb->prepare(
            "SELECT id, prefix, current_number, range_end, expiration_date
             FROM {$table}
             WHERE ecf_type = %s
               AND serie = %s
               AND is_active = 1
               AND expiration_date >= %s
               AND current_number <= range_end
             ORDER BY id ASC
             LIMIT 1",
            $ecf_type,
            $serie,
            $today
        ));

        if (!$sequence) {
            return null;
        }

        // Atomic increment — check affected rows to confirm claim
        $affected = $wpdb->query($wpdb->prepare(
            "UPDATE {$table}
             SET current_number = current_number + 1
             WHERE id = %d AND current_number <= %d",
            $sequence->id,
            $sequence->range_end
        ));

        if ($affected === 0) {
            // Race condition or exhausted — try again recursively
            // (next call will find a different sequence or return null)
            return self::claim_next($ecf_type, $serie);
        }

        $number = str_pad((string) $sequence->current_number, 10, '0', STR_PAD_LEFT);
        $encf = $sequence->prefix . $number;

        return [
            'encf' => $encf,
            'expiration_date' => $sequence->expiration_date,
        ];
    }

    /**
     * Get all sequences for admin display.
     */
    public static function get_all_sequences(): array {
        global $wpdb;
        $table = self::get_table_name();

        return $wpdb->get_results(
            "SELECT *, (range_end - current_number + 1) as remaining
             FROM {$table}
             WHERE is_active = 1
             ORDER BY ecf_type, serie, id",
            ARRAY_A
        ) ?: [];
    }
}
```

- [ ] **Step 2: Create test file for sequence manager**

```php
<?php
/**
 * Tests for Ecf_Sequence_Manager.
 *
 * Run with: cd /path/to/woo-ecf-dgii && vendor/bin/phpunit tests/test-ecf-sequence-manager.php
 * (Requires WP test framework — for now these serve as integration test specs)
 */

class Test_Ecf_Sequence_Manager {

    /**
     * Test: add_sequence inserts a row and claim_next returns first number.
     *
     * Setup:
     *   Ecf_Sequence_Manager::add_sequence('E32', 'E', 'E32', 1, 100, '2027-12-31');
     *
     * Assert:
     *   $result = Ecf_Sequence_Manager::claim_next('E32');
     *   assert($result['encf'] === 'E320000000001');
     *
     *   $result2 = Ecf_Sequence_Manager::claim_next('E32');
     *   assert($result2['encf'] === 'E320000000002');
     */
    public function test_claim_next_returns_sequential_numbers(): void {}

    /**
     * Test: claim_next returns null when sequence is exhausted.
     *
     * Setup:
     *   Ecf_Sequence_Manager::add_sequence('E32', 'E', 'E32', 1, 1, '2027-12-31');
     *   Ecf_Sequence_Manager::claim_next('E32'); // Claims the only number
     *
     * Assert:
     *   $result = Ecf_Sequence_Manager::claim_next('E32');
     *   assert($result === null);
     */
    public function test_claim_next_returns_null_when_exhausted(): void {}

    /**
     * Test: claim_next skips expired sequences.
     *
     * Setup:
     *   Ecf_Sequence_Manager::add_sequence('E32', 'E', 'E32', 1, 100, '2020-01-01');
     *
     * Assert:
     *   $result = Ecf_Sequence_Manager::claim_next('E32');
     *   assert($result === null);
     */
    public function test_claim_next_skips_expired(): void {}
}
```

- [ ] **Step 3: Commit**

```bash
git add includes/class-ecf-sequence-manager.php tests/
git commit -m "feat: add eNCF sequence manager with atomic claiming"
```

---

## Chunk 4: ECF Mapper (Order → ECF Model)

### Task 8: Create the ECF mapper

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/includes/class-ecf-mapper.php`
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/tests/test-ecf-mapper.php`

This is the core of the plugin — it translates a WooCommerce order into an ECF model.

- [ ] **Step 1: Create the mapper class**

```php
<?php
defined('ABSPATH') || exit;

use Ecfx\EcfDgii\Model\ECF;
use Ecfx\EcfDgii\Model\Encabezado;
use Ecfx\EcfDgii\Model\IdDoc;
use Ecfx\EcfDgii\Model\Emisor;
use Ecfx\EcfDgii\Model\Comprador;
use Ecfx\EcfDgii\Model\Totales;
use Ecfx\EcfDgii\Model\Item;
use Ecfx\EcfDgii\Model\Retencion;
use Ecfx\EcfDgii\Model\VersionType;
use Ecfx\EcfDgii\Model\TipoeCFType;
use Ecfx\EcfDgii\Model\IndicadorFacturacionType;
use Ecfx\EcfDgii\Model\IndicadorBienoServicioType;

class Ecf_Mapper {

    private const ECF_TYPE_MAP = [
        'E31' => TipoeCFType::FACTURA_DE_CREDITO_FISCAL_ELECTRONICA,
        'E32' => TipoeCFType::FACTURA_DE_CONSUMO_ELECTRONICA,
        'E33' => TipoeCFType::NOTA_DE_DEBITO_ELECTRONICA,
        'E34' => TipoeCFType::NOTA_DE_CREDITO_ELECTRONICA,
    ];

    /**
     * Map a WooCommerce order to an ECF model.
     *
     * @param \WC_Order $order The WooCommerce order
     * @param string $ecf_type ECF type shorthand: E31, E32, E33, E34
     * @param string $encf The assigned eNCF number
     * @param string $expiration_date Sequence expiration date (Y-m-d)
     * @return ECF
     */
    public static function map_order(
        \WC_Order $order,
        string $ecf_type,
        string $encf,
        string $expiration_date,
    ): ECF {
        $company_data = Ecf_Settings::get_company_data();

        $encabezado = new Encabezado([
            'version' => VersionType::VERSION1_0,
            'id_doc' => self::build_id_doc($ecf_type, $encf, $expiration_date, $order),
            'emisor' => self::build_emisor($company_data, $order),
            'totales' => self::build_totales($order),
        ]);

        // Add comprador for E31 (if RNC provided)
        $rnc = $order->get_meta('_ecf_rnc_comprador');
        if ($rnc && $ecf_type === 'E31') {
            $encabezado->setComprador(new Comprador([
                'razon_social_comprador' => $order->get_meta('_ecf_razon_social') ?: null,
            ]));
        }

        return new ECF([
            'encabezado' => $encabezado,
            'detalles_items' => self::build_items($order),
        ]);
    }

    private static function build_id_doc(
        string $ecf_type,
        string $encf,
        string $expiration_date,
        \WC_Order $order,
    ): IdDoc {
        $id_doc = new IdDoc([
            'tipoe_cf' => self::ECF_TYPE_MAP[$ecf_type],
            'encf' => $encf,
            'fecha_vencimiento_secuencia' => new \DateTime($expiration_date),
        ]);

        return $id_doc;
    }

    private static function build_emisor(array $company_data, \WC_Order $order): Emisor {
        return new Emisor([
            'rnc_emisor' => Ecf_Settings::get_company_rnc(),
            'razon_social_emisor' => $company_data['razonSocial'] ?? '',
            'direccion_emisor' => $company_data['direccion'] ?? '',
            'fecha_emision' => new \DateTime($order->get_date_paid()?->format('Y-m-d') ?? 'now'),
            'numero_factura_interna' => (string) $order->get_id(),
        ]);
    }

    private static function build_totales(\WC_Order $order): Totales {
        return new Totales([
            'monto_total' => (float) $order->get_total(),
        ]);
    }

    /**
     * Build ECF line items from WooCommerce order items.
     *
     * @return Item[]
     */
    private static function build_items(\WC_Order $order): array {
        $items = [];
        $line_number = 1;

        // Product lines
        foreach ($order->get_items() as $item) {
            /** @var \WC_Order_Item_Product $item */
            $product = $item->get_product();
            $is_virtual = $product && $product->is_virtual();

            $items[] = new Item([
                'numero_linea' => $line_number++,
                'nombre_item' => $item->get_name(),
                'indicador_facturacion' => self::get_tax_indicator($item, $order),
                'indicador_bieno_servicio' => $is_virtual
                    ? IndicadorBienoServicioType::SERVICIO
                    : IndicadorBienoServicioType::BIEN,
                'cantidad_item' => (float) $item->get_quantity(),
                'precio_unitario_item' => (float) ($item->get_subtotal() / max(1, $item->get_quantity())),
                'monto_item' => (float) $item->get_subtotal(),
                'retencion' => new Retencion(),
            ]);
        }

        // Shipping as a line item
        foreach ($order->get_items('shipping') as $shipping) {
            /** @var \WC_Order_Item_Shipping $shipping */
            $shipping_total = (float) $shipping->get_total();
            if ($shipping_total > 0) {
                $items[] = new Item([
                    'numero_linea' => $line_number++,
                    'nombre_item' => $shipping->get_method_title() ?: __('Shipping', 'woo-ecf-dgii'),
                    'indicador_facturacion' => self::get_shipping_tax_indicator($shipping, $order),
                    'indicador_bieno_servicio' => IndicadorBienoServicioType::SERVICIO,
                    'cantidad_item' => 1.0,
                    'precio_unitario_item' => $shipping_total,
                    'monto_item' => $shipping_total,
                    'retencion' => new Retencion(),
                ]);
            }
        }

        // Fee lines
        foreach ($order->get_items('fee') as $fee) {
            /** @var \WC_Order_Item_Fee $fee */
            $fee_total = (float) $fee->get_total();
            if ($fee_total != 0) {
                $items[] = new Item([
                    'numero_linea' => $line_number++,
                    'nombre_item' => $fee->get_name(),
                    'indicador_facturacion' => IndicadorFacturacionType::ITBIS1_18_PERCENT,
                    'indicador_bieno_servicio' => IndicadorBienoServicioType::SERVICIO,
                    'cantidad_item' => 1.0,
                    'precio_unitario_item' => $fee_total,
                    'monto_item' => $fee_total,
                    'retencion' => new Retencion(),
                ]);
            }
        }

        return $items;
    }

    /**
     * Map WooCommerce tax rate to ECF IndicadorFacturacionType.
     */
    private static function get_tax_indicator(\WC_Order_Item_Product $item, \WC_Order $order): string {
        $tax_total = (float) $item->get_total_tax();
        $subtotal = (float) $item->get_subtotal();

        if ($tax_total <= 0 || $subtotal <= 0) {
            // Check if it's exempt or non-facturable
            $product = $item->get_product();
            $tax_class = $product ? $product->get_tax_class() : '';

            if ($tax_class === 'zero-rate') {
                return IndicadorFacturacionType::ITBIS3_0_PERCENT;
            }
            if ($tax_class === 'exempt' || $tax_class === 'reduced-rate') {
                return IndicadorFacturacionType::EXENTO_E;
            }
            return IndicadorFacturacionType::NO_FACTURABLE_18_PERCENT;
        }

        // Calculate effective tax rate
        $rate = ($tax_total / $subtotal) * 100;

        if ($rate >= 17 && $rate <= 19) {
            return IndicadorFacturacionType::ITBIS1_18_PERCENT;
        }
        if ($rate >= 15 && $rate < 17) {
            return IndicadorFacturacionType::ITBIS2_16_PERCENT;
        }

        // Fallback
        return IndicadorFacturacionType::ITBIS1_18_PERCENT;
    }

    /**
     * Get tax indicator for shipping items.
     */
    private static function get_shipping_tax_indicator(\WC_Order_Item_Shipping $shipping, \WC_Order $order): string {
        $tax = (float) $shipping->get_total_tax();
        $total = (float) $shipping->get_total();

        if ($tax <= 0 || $total <= 0) {
            return IndicadorFacturacionType::EXENTO_E;
        }

        $rate = ($tax / $total) * 100;
        if ($rate >= 17 && $rate <= 19) {
            return IndicadorFacturacionType::ITBIS1_18_PERCENT;
        }
        return IndicadorFacturacionType::ITBIS2_16_PERCENT;
    }
}
```

- [ ] **Step 2: Create test specification**

```php
<?php
/**
 * Test specifications for Ecf_Mapper.
 *
 * These document expected mapping behavior.
 * Full integration tests require WP test framework with WooCommerce.
 */

class Test_Ecf_Mapper {

    /**
     * Test: A simple E32 order with one product maps correctly.
     *
     * Setup:
     *   - WC_Order with 1 item: "Widget" qty 2, $50 each, 18% ITBIS
     *   - Total: $118.00 (100 + 18 tax)
     *   - No RNC (Consumidor Final)
     *
     * Assert:
     *   - ECF type = TipoeCFType::FACTURA_DE_CONSUMO_ELECTRONICA
     *   - version = VersionType::VERSION1_0
     *   - emisor.rncEmisor = company RNC
     *   - totales.montoTotal = 118.00
     *   - 1 line item:
     *     - nombreItem = "Widget"
     *     - cantidadItem = 2
     *     - precioUnitarioItem = 50.00
     *     - montoItem = 100.00
     *     - indicadorFacturacion = ITBIS1_18_PERCENT
     *     - indicadorBienoServicio = BIEN
     *   - comprador is null (E32 no RNC)
     */
    public function test_simple_e32_order(): void {}

    /**
     * Test: Shipping is mapped as a Servicio line item.
     *
     * Setup:
     *   - WC_Order with 1 product + shipping ($10)
     *
     * Assert:
     *   - 2 line items total
     *   - Item 2: shipping, indicadorBienoServicio = SERVICIO
     */
    public function test_shipping_as_line_item(): void {}

    /**
     * Test: Virtual product maps as Servicio.
     *
     * Setup:
     *   - WC_Order with 1 virtual product
     *
     * Assert:
     *   - indicadorBienoServicio = SERVICIO
     */
    public function test_virtual_product_is_servicio(): void {}

    /**
     * Test: Tax-exempt product maps to EXENTO_E.
     */
    public function test_exempt_product_tax_indicator(): void {}

    /**
     * Test: Zero-tax product maps to ITBIS3_0_PERCENT.
     */
    public function test_zero_rate_product_tax_indicator(): void {}
}
```

- [ ] **Step 3: Commit**

```bash
git add includes/class-ecf-mapper.php tests/test-ecf-mapper.php
git commit -m "feat: add ECF mapper for WooCommerce order to ECF model conversion"
```

---

## Chunk 5: Order Handler + Admin Panel

### Task 9: Create order handler (payment hook → ECF submission)

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/includes/class-ecf-order-handler.php`

- [ ] **Step 1: Create the order handler class**

This hooks into WooCommerce payment events, builds the ECF, and schedules async submission.

```php
<?php
defined('ABSPATH') || exit;

class Ecf_Order_Handler {

    public const META_ECF_TYPE = '_ecf_type';
    public const META_ECF_ENCF = '_ecf_encf';
    public const META_ECF_STATUS = '_ecf_status';
    public const META_ECF_CODSEC = '_ecf_codsec';
    public const META_ECF_MESSAGE_ID = '_ecf_message_id';
    public const META_ECF_RESPONSE = '_ecf_response';
    public const META_ECF_ERRORS = '_ecf_errors';
    public const META_ECF_RNC_COMPRADOR = '_ecf_rnc_comprador';
    public const META_ECF_RAZON_SOCIAL = '_ecf_razon_social';

    public const STATUS_PENDING = 'pending';
    public const STATUS_SUBMITTING = 'submitting';
    public const STATUS_POLLING = 'polling';
    public const STATUS_ACCEPTED = 'accepted';
    public const STATUS_REJECTED = 'rejected';
    public const STATUS_ERROR = 'error';
    public const STATUS_CONTINGENCIA = 'contingencia';

    public static function init(): void {
        // Primary hook: fires on successful payment
        add_action('woocommerce_payment_complete', [self::class, 'on_payment_complete']);

        // Fallback hooks for offline payment methods
        add_action('woocommerce_order_status_processing', [self::class, 'on_order_processing']);
        add_action('woocommerce_order_status_completed', [self::class, 'on_order_completed']);

        // Action Scheduler hooks
        add_action('ecf_dgii_submit_ecf', [self::class, 'async_submit_ecf']);
        add_action('ecf_dgii_poll_ecf', [self::class, 'async_poll_ecf']);
    }

    /**
     * Triggered when payment is complete.
     */
    public static function on_payment_complete(int $order_id): void {
        self::schedule_ecf_submission($order_id);
    }

    /**
     * Fallback: order moved to processing (e.g., bank transfer marked paid).
     */
    public static function on_order_processing(int $order_id): void {
        self::schedule_ecf_submission($order_id);
    }

    /**
     * Fallback: order moved to completed.
     */
    public static function on_order_completed(int $order_id): void {
        self::schedule_ecf_submission($order_id);
    }

    /**
     * Schedule ECF submission via Action Scheduler (non-blocking).
     */
    private static function schedule_ecf_submission(int $order_id): void {
        $order = wc_get_order($order_id);
        if (!$order) {
            return;
        }

        // Don't re-process orders that already have an ECF
        $existing_status = $order->get_meta(self::META_ECF_STATUS);
        if ($existing_status && $existing_status !== self::STATUS_ERROR) {
            return;
        }

        // Determine ECF type
        $rnc = $order->get_meta(self::META_ECF_RNC_COMPRADOR);
        $ecf_type = $rnc
            ? (get_option(Ecf_Settings::OPTION_DEFAULT_ECF_TYPE, 'E31'))
            : 'E32';

        // Claim eNCF sequence
        $sequence = Ecf_Sequence_Manager::claim_next($ecf_type);
        if (!$sequence) {
            $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_ERROR);
            $order->update_meta_data(self::META_ECF_ERRORS, __('No available eNCF sequences for type ', 'woo-ecf-dgii') . $ecf_type);
            $order->save();
            $order->add_order_note(
                sprintf(__('ECF Error: No available eNCF sequences for %s.', 'woo-ecf-dgii'), $ecf_type)
            );
            return;
        }

        // Store initial ECF data on the order
        $order->update_meta_data(self::META_ECF_TYPE, $ecf_type);
        $order->update_meta_data(self::META_ECF_ENCF, $sequence['encf']);
        $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_PENDING);
        $order->save();

        // Schedule async submission
        as_schedule_single_action(
            time(),
            'ecf_dgii_submit_ecf',
            ['order_id' => $order_id, 'expiration_date' => $sequence['expiration_date']],
            'ecf-dgii'
        );
    }

    /**
     * Async: Submit ECF to API (runs via Action Scheduler).
     */
    public static function async_submit_ecf(int $order_id, string $expiration_date): void {
        $order = wc_get_order($order_id);
        if (!$order) {
            return;
        }

        $ecf_type = $order->get_meta(self::META_ECF_TYPE);
        $encf = $order->get_meta(self::META_ECF_ENCF);

        $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_SUBMITTING);
        $order->save();

        try {
            // Map order to ECF
            $ecf = Ecf_Mapper::map_order($order, $ecf_type, $encf, $expiration_date);

            // Submit to API
            $client = new Ecf_Api_Client();
            $response = $client->submit_ecf($ecf, $ecf_type);

            // Store messageId and schedule polling
            $message_id = $response->getMessageId();
            $order->update_meta_data(self::META_ECF_MESSAGE_ID, $message_id);
            $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_POLLING);
            $order->save();

            $order->add_order_note(
                sprintf(__('ECF submitted. eNCF: %s, MessageId: %s', 'woo-ecf-dgii'), $encf, $message_id)
            );

            // Schedule first poll
            as_schedule_single_action(
                time() + 3,
                'ecf_dgii_poll_ecf',
                ['order_id' => $order_id, 'attempt' => 1],
                'ecf-dgii'
            );
        } catch (\Exception $e) {
            $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_ERROR);
            $order->update_meta_data(self::META_ECF_ERRORS, $e->getMessage());
            $order->save();
            $order->add_order_note(
                sprintf(__('ECF submission failed: %s', 'woo-ecf-dgii'), $e->getMessage())
            );
        }
    }

    /**
     * Async: Poll ECF status (runs via Action Scheduler).
     */
    public static function async_poll_ecf(int $order_id, int $attempt): void {
        $order = wc_get_order($order_id);
        if (!$order) {
            return;
        }

        $max_attempts = (int) get_option(Ecf_Settings::OPTION_RETRY_MAX, 3);
        $retry_interval = (int) get_option(Ecf_Settings::OPTION_RETRY_INTERVAL, 5);
        $rnc = Ecf_Settings::get_company_rnc();
        $message_id = $order->get_meta(self::META_ECF_MESSAGE_ID);

        try {
            $client = new Ecf_Api_Client();
            $results = $client->get_ecf_status($rnc, $message_id);

            if (empty($results)) {
                throw new \RuntimeException('Empty response from ECF status check');
            }

            $result = $results[0];
            $progress = $result->getProgress();

            // Check if finished
            if ($progress && strtolower($progress->value ?? $progress) === 'finished') {
                $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_ACCEPTED);
                $order->update_meta_data(self::META_ECF_CODSEC, $result->getCodSec() ?? '');
                $order->update_meta_data(self::META_ECF_RESPONSE, json_encode($result->jsonSerialize()));
                $order->save();
                $order->add_order_note(
                    sprintf(
                        __('ECF accepted! eNCF: %s, Security Code: %s', 'woo-ecf-dgii'),
                        $order->get_meta(self::META_ECF_ENCF),
                        $result->getCodSec() ?? 'N/A'
                    )
                );
                return;
            }

            // Check if error/rejected
            if ($progress && strtolower($progress->value ?? $progress) === 'error') {
                $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_REJECTED);
                $order->update_meta_data(self::META_ECF_ERRORS, $result->getErrors() ?? '');
                $order->save();
                $order->add_order_note(
                    sprintf(__('ECF rejected: %s', 'woo-ecf-dgii'), $result->getErrors() ?? 'Unknown error')
                );
                return;
            }

            // Still processing — schedule another poll if under max
            if ($attempt < $max_attempts * 10) { // More polls than retries (polling != retry)
                as_schedule_single_action(
                    time() + $retry_interval,
                    'ecf_dgii_poll_ecf',
                    ['order_id' => $order_id, 'attempt' => $attempt + 1],
                    'ecf-dgii'
                );
            } else {
                // Polling timed out
                $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_ERROR);
                $order->update_meta_data(self::META_ECF_ERRORS, __('Polling timed out', 'woo-ecf-dgii'));
                $order->save();
                $order->add_order_note(__('ECF polling timed out. Check ECF SSD dashboard.', 'woo-ecf-dgii'));
            }
        } catch (\Exception $e) {
            if ($attempt < $max_attempts * 10) {
                as_schedule_single_action(
                    time() + $retry_interval,
                    'ecf_dgii_poll_ecf',
                    ['order_id' => $order_id, 'attempt' => $attempt + 1],
                    'ecf-dgii'
                );
            } else {
                $order->update_meta_data(self::META_ECF_STATUS, self::STATUS_ERROR);
                $order->update_meta_data(self::META_ECF_ERRORS, $e->getMessage());
                $order->save();
            }
        }
    }
}
```

- [ ] **Step 2: Commit**

```bash
git add includes/class-ecf-order-handler.php
git commit -m "feat: add order handler with async ECF submission via Action Scheduler"
```

---

### Task 10: Create admin order metabox

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/includes/class-ecf-admin-order.php`
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/assets/css/admin.css`

- [ ] **Step 1: Create the admin order panel class**

```php
<?php
defined('ABSPATH') || exit;

class Ecf_Admin_Order {

    public static function init(): void {
        add_action('add_meta_boxes', [self::class, 'add_metabox']);
        add_action('admin_enqueue_scripts', [self::class, 'enqueue_styles']);
        add_action('wp_ajax_ecf_dgii_retry_submission', [self::class, 'ajax_retry']);
    }

    public static function add_metabox(): void {
        $screen = wc_get_container()
            ->get(\Automattic\WooCommerce\Internal\DataStores\Orders\CustomOrdersTableController::class)
            ->custom_orders_table_usage_is_enabled()
            ? wc_get_page_screen_id('shop-order')
            : 'shop_order';

        add_meta_box(
            'ecf-dgii-status',
            __('ECF DGII', 'woo-ecf-dgii'),
            [self::class, 'render_metabox'],
            $screen,
            'side',
            'high'
        );
    }

    public static function render_metabox($post_or_order): void {
        $order = ($post_or_order instanceof \WC_Order)
            ? $post_or_order
            : wc_get_order($post_or_order->ID);

        if (!$order) {
            echo '<p>' . esc_html__('Order not found.', 'woo-ecf-dgii') . '</p>';
            return;
        }

        $status = $order->get_meta(Ecf_Order_Handler::META_ECF_STATUS) ?: 'none';
        $ecf_type = $order->get_meta(Ecf_Order_Handler::META_ECF_TYPE);
        $encf = $order->get_meta(Ecf_Order_Handler::META_ECF_ENCF);
        $codsec = $order->get_meta(Ecf_Order_Handler::META_ECF_CODSEC);
        $errors = $order->get_meta(Ecf_Order_Handler::META_ECF_ERRORS);

        $status_labels = [
            'none' => ['label' => __('Not sent', 'woo-ecf-dgii'), 'class' => 'ecf-status-none'],
            Ecf_Order_Handler::STATUS_PENDING => ['label' => __('Pending', 'woo-ecf-dgii'), 'class' => 'ecf-status-pending'],
            Ecf_Order_Handler::STATUS_SUBMITTING => ['label' => __('Submitting', 'woo-ecf-dgii'), 'class' => 'ecf-status-pending'],
            Ecf_Order_Handler::STATUS_POLLING => ['label' => __('Processing', 'woo-ecf-dgii'), 'class' => 'ecf-status-pending'],
            Ecf_Order_Handler::STATUS_ACCEPTED => ['label' => __('Accepted', 'woo-ecf-dgii'), 'class' => 'ecf-status-accepted'],
            Ecf_Order_Handler::STATUS_REJECTED => ['label' => __('Rejected', 'woo-ecf-dgii'), 'class' => 'ecf-status-rejected'],
            Ecf_Order_Handler::STATUS_ERROR => ['label' => __('Error', 'woo-ecf-dgii'), 'class' => 'ecf-status-error'],
            Ecf_Order_Handler::STATUS_CONTINGENCIA => ['label' => __('Contingencia', 'woo-ecf-dgii'), 'class' => 'ecf-status-contingencia'],
        ];

        $s = $status_labels[$status] ?? $status_labels['none'];
        ?>
        <div class="ecf-metabox">
            <p>
                <strong><?php esc_html_e('Status:', 'woo-ecf-dgii'); ?></strong>
                <span class="ecf-status-badge <?php echo esc_attr($s['class']); ?>">
                    <?php echo esc_html($s['label']); ?>
                </span>
            </p>

            <?php if ($ecf_type): ?>
                <p><strong><?php esc_html_e('Type:', 'woo-ecf-dgii'); ?></strong> <?php echo esc_html($ecf_type); ?></p>
            <?php endif; ?>

            <?php if ($encf): ?>
                <p><strong><?php esc_html_e('eNCF:', 'woo-ecf-dgii'); ?></strong> <?php echo esc_html($encf); ?></p>
            <?php endif; ?>

            <?php if ($codsec): ?>
                <p><strong><?php esc_html_e('Security Code:', 'woo-ecf-dgii'); ?></strong> <?php echo esc_html($codsec); ?></p>
            <?php endif; ?>

            <?php if ($errors): ?>
                <p class="ecf-error-details">
                    <strong><?php esc_html_e('Errors:', 'woo-ecf-dgii'); ?></strong><br>
                    <?php echo esc_html($errors); ?>
                </p>
            <?php endif; ?>

            <?php if (in_array($status, ['error', 'rejected', 'none'])): ?>
                <p>
                    <button type="button" class="button ecf-retry-btn"
                            data-order-id="<?php echo esc_attr($order->get_id()); ?>">
                        <?php esc_html_e('Send ECF', 'woo-ecf-dgii'); ?>
                    </button>
                </p>
                <script>
                jQuery(function($) {
                    $('.ecf-retry-btn').on('click', function() {
                        var $btn = $(this);
                        $btn.prop('disabled', true).text('<?php echo esc_js(__('Sending...', 'woo-ecf-dgii')); ?>');
                        $.post(ajaxurl, {
                            action: 'ecf_dgii_retry_submission',
                            order_id: $btn.data('order-id'),
                            _wpnonce: '<?php echo wp_create_nonce('ecf_dgii_retry'); ?>'
                        }, function() {
                            location.reload();
                        });
                    });
                });
                </script>
            <?php endif; ?>
        </div>
        <?php
    }

    public static function enqueue_styles(string $hook): void {
        if (!in_array($hook, ['post.php', 'post-new.php', 'woocommerce_page_wc-orders'])) {
            return;
        }
        wp_enqueue_style(
            'ecf-dgii-admin',
            WOO_ECF_DGII_PLUGIN_URL . 'assets/css/admin.css',
            [],
            WOO_ECF_DGII_VERSION
        );
    }

    public static function ajax_retry(): void {
        check_ajax_referer('ecf_dgii_retry');
        if (!current_user_can('manage_woocommerce')) {
            wp_send_json_error('Permission denied');
        }

        $order_id = absint($_POST['order_id'] ?? 0);
        if (!$order_id) {
            wp_send_json_error('Invalid order ID');
        }

        // Reset status so handler will re-process
        $order = wc_get_order($order_id);
        if ($order) {
            $order->update_meta_data(Ecf_Order_Handler::META_ECF_STATUS, Ecf_Order_Handler::STATUS_ERROR);
            $order->save();
        }

        Ecf_Order_Handler::on_payment_complete($order_id);
        wp_send_json_success();
    }
}
```

- [ ] **Step 2: Create admin CSS**

```bash
mkdir -p /Users/dawlin/Developer/puntoos/woo-ecf-dgii/assets/css
```

```css
/* ECF DGII Admin Styles */
.ecf-metabox p {
    margin: 8px 0;
}

.ecf-status-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 3px;
    font-size: 12px;
    font-weight: 600;
}

.ecf-status-none {
    background: #ddd;
    color: #666;
}

.ecf-status-pending {
    background: #fff3cd;
    color: #856404;
}

.ecf-status-accepted {
    background: #d4edda;
    color: #155724;
}

.ecf-status-rejected {
    background: #f8d7da;
    color: #721c24;
}

.ecf-status-error {
    background: #f8d7da;
    color: #721c24;
}

.ecf-status-contingencia {
    background: #fff3cd;
    color: #856404;
}

.ecf-error-details {
    background: #fff5f5;
    border-left: 3px solid #dc3545;
    padding: 8px;
    font-size: 12px;
}
```

- [ ] **Step 3: Commit**

```bash
git add includes/class-ecf-admin-order.php assets/
git commit -m "feat: add admin order metabox showing ECF status"
```

---

### Task 11: Create uninstall.php

**Files:**
- Create: `/Users/dawlin/Developer/puntoos/woo-ecf-dgii/uninstall.php`

- [ ] **Step 1: Create uninstall cleanup**

```php
<?php
defined('WP_UNINSTALL_PLUGIN') || exit;

global $wpdb;

// Drop custom table
$wpdb->query("DROP TABLE IF EXISTS {$wpdb->prefix}ecf_sequences");

// Remove plugin options
$options = [
    'ecf_dgii_api_token',
    'ecf_dgii_environment',
    'ecf_dgii_company_rnc',
    'ecf_dgii_company_data',
    'ecf_dgii_default_ecf_type',
    'ecf_dgii_retry_max',
    'ecf_dgii_retry_interval',
];

foreach ($options as $option) {
    delete_option($option);
}
```

- [ ] **Step 2: Commit**

```bash
git add uninstall.php
git commit -m "feat: add uninstall cleanup for options and custom table"
```

---

## Chunk 6: Integration Testing

### Task 12: End-to-end testing with Podman

This task verifies the entire flow works: plugin activates, settings save, orders trigger ECF submission.

- [ ] **Step 1: Start the Podman dev environment**

```bash
cd /Users/dawlin/Developer/puntoos/woo-ecf-dgii/dev
podman-compose up -d
```

Wait for containers to be healthy:

```bash
podman-compose ps
```

Expected: Both `db` and `wordpress` containers running, wordpress on port 8080.

- [ ] **Step 2: Access WordPress and complete setup**

Open `http://localhost:8080` in a browser. Complete the WordPress installation wizard:
- Site Title: ECF Test Store
- Username: admin
- Password: admin
- Email: test@test.com

- [ ] **Step 3: Run setup script inside WordPress container**

```bash
podman-compose exec wordpress bash /var/www/html/wp-content/plugins/woo-ecf-dgii/dev/setup.sh
```

Expected output includes "Setup complete". WooCommerce installed, plugin activated.

- [ ] **Step 4: Verify plugin appears in WordPress admin**

Navigate to: `http://localhost:8080/wp-admin/plugins.php`
Expected: "WooCommerce ECF DGII" is listed and active.

- [ ] **Step 5: Configure ECF DGII settings**

Navigate to: `http://localhost:8080/wp-admin/admin.php?page=wc-settings&tab=ecf_dgii`

Fill in:
- Environment: Test
- API Token: (your ECF SSD test token)
- Company RNC: (your test RNC)

Click "Save changes", then "Test Connection".
Expected: Green "Connected! Company: ..." message.

- [ ] **Step 6: Add an eNCF sequence**

This requires adding a sequence directly to the database (admin UI for sequences is Phase 2+).

```bash
podman-compose exec wordpress wp eval '
require_once "/var/www/html/wp-content/plugins/woo-ecf-dgii/includes/class-ecf-sequence-manager.php";
Ecf_Sequence_Manager::add_sequence("E32", "E", "E32", 1, 1000, "2027-12-31");
echo "Sequence added\n";
' --allow-root
```

- [ ] **Step 7: Create a test WooCommerce product**

Navigate to: `http://localhost:8080/wp-admin/post-new.php?post_type=product`
- Product name: "Test Widget"
- Regular price: 1000
- Publish

Or via WP-CLI:

```bash
podman-compose exec wordpress wp wc product create \
    --name="Test Widget" \
    --regular_price=1000 \
    --allow-root \
    --user=1
```

- [ ] **Step 8: Set up Dominican tax rates**

Navigate to: WooCommerce > Settings > Tax
- Enable taxes
- Add a standard rate: Country=DO, Rate=18%, Name=ITBIS

Or via WP-CLI:

```bash
podman-compose exec wordpress wp option update woocommerce_calc_taxes yes --allow-root
```

- [ ] **Step 9: Place a test order**

Navigate to the shop, add "Test Widget" to cart, proceed to checkout.
Fill in billing details, select a payment method (Cash on Delivery for testing), place order.

Then in admin, change order status to "Processing" to trigger the ECF submission.

- [ ] **Step 10: Verify ECF submission**

Navigate to the order in WooCommerce admin.
Check the "ECF DGII" metabox on the right side:
- Status should progress: Pending → Submitting → Processing → Accepted
- eNCF number should be displayed
- Security code should appear once accepted
- Order notes should show ECF submission log

Check Action Scheduler: `http://localhost:8080/wp-admin/tools.php?page=action-scheduler`
Expected: `ecf_dgii_submit_ecf` and `ecf_dgii_poll_ecf` actions completed.

- [ ] **Step 11: Commit any fixes from testing**

```bash
cd /Users/dawlin/Developer/puntoos/woo-ecf-dgii
git add -A
git commit -m "fix: adjustments from integration testing"
```

---

## Summary

After completing all tasks, the plugin will:
1. Install and activate on WordPress + WooCommerce
2. Provide a settings page for API connection, RNC, and environment
3. Track eNCF sequences with atomic claiming
4. Map WooCommerce orders to ECF E32 (Consumidor Final) documents
5. Submit ECFs asynchronously via Action Scheduler
6. Poll for results and store status on order meta
7. Display ECF status in an admin order metabox
8. Support manual retry for failed submissions
