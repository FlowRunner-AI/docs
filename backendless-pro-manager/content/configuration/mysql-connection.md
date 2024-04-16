# MySQL Connection Configuration

This section details the settings required to configure MySQL connection parameters for applications using sharding. It is applicable to JAVA or JavaScript applications.

#### Sharding Configuration

- **`config/sharding/shards`**
    - **Description:** Declares the active shard or shards, separated by semicolons if multiple.
    - **Type:** String
    - **Example:** `config/sharding/shards = main_backendless;shard1`

#### Shard Connection Settings

For each declared shard, you must define the following connection settings:

- **Pattern**
    - **Key:** `config/connection/<shard>/pattern`
    - **Description:** Regular expression or pipe-separated database names to match databases to the shard.
    - **Default:** `.*`
    - **Example:** `config/connection/main/pattern = main_backendless|main_application|<app-id1>`

- **Endpoints**
    - **Key:** `config/connection/<shard>/endpoints`
    - **Description:** Specifies the host and port of the database server.
    - **Type:** String
    - **Example:** `config/connection/main/endpoints = bl-mysql:3306`

- **User**
    - **Key:** `config/connection/<shard>/user`
    - **Description:** Database username for authentication.
    - **Type:** String
    - **Example:** `config/connection/main/user = root`

- **Password**
    - **Key:** `config/connection/<shard>/password`
    - **Description:** Database password for authentication.
    - **Type:** String
    - **Example:** `config/connection/main/password = your-password`

- **Idle Test Period**
    - **Key:** `config/connection/<shard>/idleTestPeriod`
    - **Description:** Time in milliseconds between idle connection checks.
    - **Type:** Integer
    - **Example:** `config/connection/main/idleTestPeriod = 60000`

- **Idle Timeout**
    - **Key:** `config/connection/<shard>/idleTimeout`
    - **Description:** Time in milliseconds before an idle connection is closed.
    - **Type:** Integer
    - **Example:** `config/connection/main/idleTimeout = 600000`

- **Maximum Active Connections**
    - **Key:** `config/connection/<shard>/maxActive`
    - **Description:** Maximum number of active connections.
    - **Type:** Integer
    - **Example:** `config/connection/main/maxActive = 100`

- **Maximum Idle Connections**
    - **Key:** `config/connection/<shard>/maxIdle`
    - **Description:** Maximum number of idle connections in the pool.
    - **Type:** Integer
    - **Example:** `config/connection/main/maxIdle = 100`

- **Minimum Idle Connections**
    - **Key:** `config/connection/<shard>/minIdle`
    - **Description:** Minimum number of idle connections in the pool.
    - **Type:** Integer
    - **Example:** `config/connection/main/minIdle = 5`

#### JDBC URL Template

- **`config/connection/main/urlTemplate`**
    - **Description:** Template for constructing JDBC connection URLs. Includes placeholders for dialect, endpoints, and other settings.
    - **Type:** String
    - **Example:**
      ```
      config/connection/main/urlTemplate = jdbc:${dialect}://${endpoints}?zeroDateTimeBehavior=${zeroDateTimeBehavior}&useSSL=${useSSL}&requireSSL=${requireSSL}&dumpQueriesOnException=${dumpQueriesOnException}&exceptionInterceptors=${exceptionInterceptors}&allowPublicKeyRetrieval=${allowPublicKeyRetrieval}&serverTimezone=UTC&failOverReadOnly=false&secondsBeforeRetrySource=60
      ```