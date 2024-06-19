### Cloning Timeout

Specifies the timeout in seconds for cloning operations, ensuring they do not run indefinitely.

| Configuration Property Path             | Type    | Default Value | Example                                |
|-----------------------------------------|---------|---------------|----------------------------------------|
| `config/taskman/cloning/timeoutSeconds` | Integer | `7200` (2 hours) | `config/taskman/cloning/timeoutSeconds = 1200` (20 minutes) |

### Export Configuration

#### Executable

Specifies the executable used for the export operation.

| Configuration Property Path             | Type    | Default Value | Example                                |
|-----------------------------------------|---------|---------------|----------------------------------------|
| `config/cloning/export/executable`      | String  | `mysqldump`   | `config/cloning/export/executable = mysqldump` |

#### Export Options

Provides a variety of options for the export operation including protocol, transaction type, database options, and more. Refer to the official MySQL documentation for a complete list of `mysqldump` options.

| Configuration Property Path             | Type    | Default Value | Example                                |
|-----------------------------------------|---------|---------------|----------------------------------------|
| `config/cloning/export/options`         | String  | N/A           | `config/cloning/export/options = --protocol=TCP; --single-transaction; --add-drop-database; --add-drop-table; --skip-add-locks; --create-options; --disable-keys; --extended-insert; --skip-lock-tables; --quick; --skip-set-charset; --column-statistics=0; --events; --routines; --triggers` |

### Import Configuration

#### Executable

Specifies the executable used for the import operation.

| Configuration Property Path             | Type    | Default Value | Example                                |
|-----------------------------------------|---------|---------------|----------------------------------------|
| `config/cloning/import/executable`      | String  | `mysql`       | `config/cloning/import/executable = mysql` |

#### Import Options

Provides the protocol setting for the import operation.

| Configuration Property Path             | Type    | Default Value | Example                                |
|-----------------------------------------|---------|---------------|----------------------------------------|
| `config/cloning/import/options`         | String  | `--protocol=TCP` | `config/cloning/import/options = --protocol=TCP` |