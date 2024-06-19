# Data Service Configuration

Configure various aspects of the Data Service to optimize performance, functionality, and data access patterns in your application. These settings control features such as Access Control Lists, column visibility, pagination, bulk operations, and special handling for large texts.

### Access Control and Security

Determines if Access Control List (ACL) features are enabled for applications. Disabling this can speed up retrieve operations at the cost of finer-grained permissions.

| Configuration Property Path                  | Type    | Default Value | Example                               |
|----------------------------------------------|---------|---------------|---------------------------------------|
| `config/db/application/aclEnabled`           | Boolean | `true`        | `config/db/application/aclEnabled = false` |
| **Further Reading:** [Data Security](https://backendless.com/docs/rest/data_security.html)

Determines if the visibility of columns feature is enabled for applications.

| Configuration Property Path                              | Type    | Default Value | Example                                     |
|----------------------------------------------------------|---------|---------------|---------------------------------------------|
| `config/db/application/columnVisibilityEnabled`          | Boolean | `true`        | `config/db/application/columnVisibilityEnabled = false` |

### Pagination and Batch Processing

Sets the maximum page size for "find" API operations in Data Service.

| Configuration Property Path      | Type    | Default Value | Example                       |
|----------------------------------|---------|---------------|-------------------------------|
| `pagesize/max`                   | Integer | `100`         | `pagesize/max = 200`          |

Sets the default page size for "find" API operations in Data Service.

| Configuration Property Path      | Type    | Default Value | Example                       |
|----------------------------------|---------|---------------|-------------------------------|
| `pagesize/default`               | Integer | `10`          | `pagesize/default = 20`       |

Sets the maximum size of batch for "bulk create" API operations in Data Service.

| Configuration Property Path      | Type    | Default Value | Example                       |
|----------------------------------|---------|---------------|-------------------------------|
| `bulkcreate/max`                 | Integer | `100`         | `bulkcreate/max = 150`        |

Sets the maximum size of batch for "bulk upsert" API operations in Data Service.

| Configuration Property Path      | Type    | Default Value | Example                       |
|----------------------------------|---------|---------------|-------------------------------|
| `config/data/bulkUpsert/max`     | Integer | `100`         | `config/data/bulkUpsert/max = 150` |

Sets the maximum page size for relations for "find" API operations in Data Service.

| Configuration Property Path                      | Type    | Default Value | Example                       |
|--------------------------------------------------|---------|---------------|-------------------------------|
| `config/data/relationsPageSize/max`              | Integer | `100`         | `config/data/relationsPageSize/max = 200` |

Sets the default page size for relations for "find" API operations in Data Service.

| Configuration Property Path                      | Type    | Default Value | Example                       |
|--------------------------------------------------|---------|---------------|-------------------------------|
| `config/data/relationsPageSize/default`          | Integer | `10`          | `config/data/relationsPageSize/default = 20` |

### Additional Data Handling Settings

Sets the maximum size of batch for listing operation for Atomic counters.

| Configuration Property Path             | Type    | Default Value | Example                          |
|-----------------------------------------|---------|---------------|----------------------------------|
| `config/counters/retrieve/max`          | Integer | `1000`        | `config/counters/retrieve/max = 1500` |

Sets the size to which values of "large text" columns will be reduced for Console requests, enhancing performance and readability.

| Configuration Property Path                             | Type    | Default Value | Example                             |
|---------------------------------------------------------|---------|---------------|-------------------------------------|
| `config/data/shrinkLargeTextForConsole`                 | Integer | `1000`        | `config/data/shrinkLargeTextForConsole = 500` |