
# MongoDB Connection Configuration

This section provides configuration details for connecting to MongoDB, including timeout settings, endpoint configurations, and authentication details for different service areas within the application.

#### Connection Timeout Settings

- **`config/mongo/connection/connectTimeout`**
    - **Description:** Sets the timeout in milliseconds for attempting a connection.
    - **Type:** Integer
    - **Default:** `5000` milliseconds (5 seconds)
    - **Example:** `config/mongo/connection/connectTimeout = 10000`

- **`config/mongo/connection/maxWaitTime`**
    - **Description:** Specifies the maximum wait time in milliseconds for a connection to become available.
    - **Type:** Integer
    - **Default:** `5000` milliseconds (5 seconds)
    - **Example:** `config/mongo/connection/maxWaitTime = 10000`

- **`config/mongo/connection/serverSelectionTimeout`**
    - **Description:** Determines the timeout in milliseconds for selecting a server for operations.
    - **Type:** Integer
    - **Default:** `5000` milliseconds (5 seconds)
    - **Example:** `config/mongo/connection/serverSelectionTimeout = 10000`

#### Service-Specific Endpoint Configurations

##### Analytics Service

- **`config/mongo/connection/analytics/endpoints`**
    - **Description:** Specifies the MongoDB endpoints for the Analytics service.
    - **Type:** String
    - **Default:** `bl-mongo:27017`
    - **Example:** `config/mongo/connection/analytics/endpoints = bl-mongo-analytics:27017`

##### Settings Service

- **`config/mongo/connection/settings/endpoints`**
    - **Description:** Specifies the MongoDB endpoints for the Settings service.
    - **Type:** String
    - **Default:** `bl-mongo:27017`
    - **Example:** `config/mongo/connection/settings/endpoints = bl-mongo-settings:27017`

##### Push Templates Service

- **`config/mongo/connection/pushtemplates/endpoints`**
    - **Description:** Specifies the MongoDB endpoints for the Push Templates service.
    - **Type:** String
    - **Default:** `bl-mongo:27017`
    - **Example:** `config/mongo/connection/pushtemplates/endpoints = bl-mongo-pushtemplates:27017`

#### Log Management

- **`config/mongo/timerLogs/expireAfterSeconds`**
    - **Description:** Sets the time in seconds after which timer logs in MongoDB will expire.
    - **Type:** Integer
    - **Default:** `2592000` seconds (30 days)
    - **Example:** `config/mongo/timerLogs/expireAfterSeconds = 31536000` (1 year)

- **`config/mongo/timerLogs/historyLimit`**
    - **Description:** Specifies the maximum number of timer log entries to retain.
    - **Type:** Integer
    - **Default:** `1000`
    - **Example:** `config/mongo/timerLogs/historyLimit = 5000`