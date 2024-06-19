# MySQL Connection Configuration

This section details the settings required to configure MySQL connection parameters for applications using sharding. It is applicable to JAVA or JavaScript applications.

### Sharding Configuration

Declares the active shard or shards, separated by semicolons if multiple.

| Configuration Property Path         | Type   | Default Value | Example                                      |
|-------------------------------------|--------|---------------|----------------------------------------------|
| `config/sharding/shards`            | String | N/A           | `config/sharding/shards = main_backendless;shard1` |

### Shard Connection Settings

For each declared shard, you must define the following connection settings:

#### Pattern

Regular expression or pipe-separated database names to match databases to the shard.

| Configuration Property Path                    | Type    | Default Value | Example                                                  |
|------------------------------------------------|---------|---------------|----------------------------------------------------------|
| `config/connection/<shard>/pattern`            | String  | `.*`          | `config/connection/main/pattern = main_backendless|main_application|<app-id1>` |

#### Endpoints

Specifies the host and port of the database server.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/<shard>/endpoints`          | String  | N/A           | `config/connection/main/endpoints = bl-mysql:3306` |

#### User

Database username for authentication.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/<shard>/user`               | String  | N/A           | `config/connection/main/user = root` |

#### Password

Database password for authentication.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/<shard>/password`           | String  | N/A           | `config/connection/main/password = your-password` |

#### Idle Test Period

Time in milliseconds between idle connection checks.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/<shard>/idleTestPeriod`     | Integer | N/A           | `config/connection/main/idleTestPeriod = 60000` |

#### Idle Timeout

Time in milliseconds before an idle connection is closed.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/<shard>/idleTimeout`        | Integer | N/A           | `config/connection/main/idleTimeout = 600000` |

#### Maximum Active Connections

Maximum number of active connections.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/<shard>/maxActive`          | Integer | N/A           | `config/connection/main/maxActive = 100` |

#### Maximum Idle Connections

Maximum number of idle connections in the pool.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/<shard>/maxIdle`            | Integer | N/A           | `config/connection/main/maxIdle = 100` |

#### Minimum Idle Connections

Minimum number of idle connections in the pool.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/<shard>/minIdle`            | Integer | N/A           | `config/connection/main/minIdle = 5` |

### JDBC URL Template

Template for constructing JDBC connection URLs. Includes placeholders for dialect, endpoints, and other settings.

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/connection/main/urlTemplate`           | String  | N/A           | `config/connection/main/urlTemplate = jdbc:${dialect}://${endpoints}?zeroDateTimeBehavior=${zeroDateTimeBehavior}&useSSL=${useSSL}&requireSSL=${requireSSL}&dumpQueriesOnException=${dumpQueriesOnException}&exceptionInterceptors=${exceptionInterceptors}&allowPublicKeyRetrieval=${allowPublicKeyRetrieval}&serverTimezone=UTC&failOverReadOnly=false&secondsBeforeRetrySource=60` |