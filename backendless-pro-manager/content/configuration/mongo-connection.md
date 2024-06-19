# MongoDB Connection Configuration

This section provides configuration details for connecting to MongoDB, including timeout settings, endpoint configurations, and authentication details for different service areas within the application.

### Connection Timeout Settings

Sets the timeout in milliseconds for attempting a connection.

| Configuration Property Path                      | Type    | Default Value        | Example                                  |
|--------------------------------------------------|---------|----------------------|------------------------------------------|
| `config/mongo/connection/connectTimeout`         | Integer | `5000` milliseconds  | `config/mongo/connection/connectTimeout = 10000` |

Specifies the maximum wait time in milliseconds for a connection to become available.

| Configuration Property Path                      | Type    | Default Value        | Example                                  |
|--------------------------------------------------|---------|----------------------|------------------------------------------|
| `config/mongo/connection/maxWaitTime`            | Integer | `5000` milliseconds  | `config/mongo/connection/maxWaitTime = 10000` |

Determines the timeout in milliseconds for selecting a server for operations.

| Configuration Property Path                      | Type    | Default Value        | Example                                  |
|--------------------------------------------------|---------|----------------------|------------------------------------------|
| `config/mongo/connection/serverSelectionTimeout` | Integer | `5000` milliseconds  | `config/mongo/connection/serverSelectionTimeout = 10000` |

### Service-Specific Endpoint Configurations

#### Analytics Service

Specifies the MongoDB endpoints for the Analytics service.

| Configuration Property Path                            | Type    | Default Value   | Example                                         |
|--------------------------------------------------------|---------|-----------------|-------------------------------------------------|
| `config/mongo/connection/analytics/endpoints`          | String  | `bl-mongo:27017`| `config/mongo/connection/analytics/endpoints = bl-mongo-analytics:27017` |

#### Settings Service

Specifies the MongoDB endpoints for the Settings service.

| Configuration Property Path                            | Type    | Default Value   | Example                                         |
|--------------------------------------------------------|---------|-----------------|-------------------------------------------------|
| `config/mongo/connection/settings/endpoints`           | String  | `bl-mongo:27017`| `config/mongo/connection/settings/endpoints = bl-mongo-settings:27017` |

#### Push Templates Service

Specifies the MongoDB endpoints for the Push Templates service.

| Configuration Property Path                            | Type    | Default Value   | Example                                         |
|--------------------------------------------------------|---------|-----------------|-------------------------------------------------|
| `config/mongo/connection/pushtemplates/endpoints`      | String  | `bl-mongo:27017`| `config/mongo/connection/pushtemplates/endpoints = bl-mongo-pushtemplates:27017` |

### Log Management

Sets the time in seconds after which timer logs in MongoDB will expire.

| Configuration Property Path                         | Type    | Default Value        | Example                                  |
|-----------------------------------------------------|---------|----------------------|------------------------------------------|
| `config/mongo/timerLogs/expireAfterSeconds`         | Integer | `2592000` seconds (30 days) | `config/mongo/timerLogs/expireAfterSeconds = 31536000` (1 year) |

Specifies the maximum number of timer log entries to retain.

| Configuration Property Path                         | Type    | Default Value        | Example                                  |
|-----------------------------------------------------|---------|----------------------|------------------------------------------|
| `config/mongo/timerLogs/historyLimit`               | Integer | `1000`               | `config/mongo/timerLogs/historyLimit = 5000` |