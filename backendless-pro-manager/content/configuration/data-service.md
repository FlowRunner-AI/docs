### Data Service Configuration

Configure various aspects of the Data Service to optimize performance, functionality, and data access patterns in your application. These settings control features such as Access Control Lists, column visibility, pagination, bulk operations, and special handling for large texts.

#### Access Control and Security

- **`config/db/application/aclEnabled`**
    - **Description:** Determines if Access Control List (ACL) features are enabled for applications. Disabling this can speed up retrieve operations at the cost of finer-grained permissions.
    - **Type:** Boolean
    - **Default:** `true`
    - **Example:** `config/db/application/aclEnabled = false`
    - **Further Reading:** [Data Security](https://backendless.com/docs/rest/data_security.html)

- **`config/db/application/columnVisibilityEnabled`**
    - **Description:** Determines if the visibility of columns feature is enabled for applications.
    - **Type:** Boolean
    - **Default:** `true`
    - **Example:** `config/db/application/columnVisibilityEnabled = false`

#### Pagination and Batch Processing

- **`pagesize/max`**
    - **Description:** Sets the maximum page size for "find" operations in Data Service.
    - **Type:** Integer
    - **Default:** `100`
    - **Example:** `pagesize/max = 200`

- **`pagesize/default`**
    - **Description:** Sets the default page size for "find" operations in Data Service.
    - **Type:** Integer
    - **Default:** `10`
    - **Example:** `pagesize/default = 20`

- **`bulkcreate/max`**
    - **Description:** Sets the maximum size of batch for "bulk create" operations in Data Service.
    - **Type:** Integer
    - **Default:** `100`
    - **Example:** `bulkcreate/max = 150`

- **`config/data/bulkUpsert/max`**
    - **Description:** Sets the maximum size of batch for "bulk upsert" operations in Data Service.
    - **Type:** Integer
    - **Default:** `100`
    - **Example:** `config/data/bulkUpsert/max = 150`

- **`config/data/relationsPageSize/max`**
    - **Description:** Sets the maximum page size for relations for "find" operations in Data Service.
    - **Type:** Integer
    - **Default:** `100`
    - **Example:** `config/data/relationsPageSize/max = 200`

- **`config/data/relationsPageSize/default`**
    - **Description:** Sets the default page size for relations for "find" operations in Data Service.
    - **Type:** Integer
    - **Default:** `10`
    - **Example:** `config/data/relationsPageSize/default = 20`

#### Additional Data Handling Settings

- **`config/counters/retrieve/max`**
    - **Description:** Sets the maximum size of batch for listing operation for Atomic counters.
    - **Type:** Integer
    - **Default:** `1000`
    - **Example:** `config/counters/retrieve/max = 1500`

- **`config/data/shrinkLargeTextForConsole`**
    - **Description:** Sets the size to which values of "large text" columns will be reduced for Console requests, enhancing performance and readability.
    - **Type:** Integer
    - **Default:** `1000`
    - **Example:** `config/data/shrinkLargeTextForConsole = 500`
