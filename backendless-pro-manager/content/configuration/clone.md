# Clone application
#### Cloning Timeout

- **`config/taskman/cloning/timeoutSeconds`**
    - **Description:** Specifies the timeout in seconds for the cloning operations, ensuring operations do not run indefinitely.
    - **Type:** Integer
    - **Default:** `7200` (2 hours)
    - **Example:** `config/taskman/cloning/timeoutSeconds = 1200` (20 minutes)


#### Export Configuration

- **`config/cloning/export/executable`**
    - **Description:** Specifies the executable used for the export operation.
    - **Type:** String
    - **Default:** `mysqldump`
    - **Example:** `config/cloning/export/executable = mysqldump`

- **`config/cloning/export/options`**
    - **Description:** Provides a variety of options for the export operation including protocol, transaction type, database options, and more. Refer to the official MySQL documentation for a complete list of mysqldump options.
    - **Type:** String
    - **Example:**
      ```
      config/cloning/export/options = --protocol=TCP;\
                                      --single-transaction;\
                                      --add-drop-database;\
                                      --add-drop-table;\
                                      --skip-add-locks;\
                                      --create-options;\
                                      --disable-keys;\
                                      --extended-insert;\
                                      --skip-lock-tables;\
                                      --quick;\
                                      --skip-set-charset;\
                                      --column-statistics=0;\
                                      --events;\
                                      --routines;\
                                      --triggers
      ```

#### Import Configuration

- **`config/cloning/import/executable`**
    - **Description:** Specifies the executable used for the import operation.
    - **Type:** String
    - **Default:** `mysql`
    - **Example:** `config/cloning/import/executable = mysql`

- **`config/cloning/import/options`**
    - **Description:** Provides the protocol setting for the import operation.
    - **Type:** String
    - **Default:** `--protocol=TCP`
    - **Example:** `config/cloning/import/options = --protocol=TCP`


