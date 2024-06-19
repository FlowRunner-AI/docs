# Files Service Configuration

This section outlines the configuration settings for the Files Service operations within your application. These settings control file compression operations and define important system paths that are typically set during initial setup and not modified thereafter.

### File Operation Execution Times

Specifies the maximum allowed execution time for file operations, such as unzipping and zipping, in seconds.

#### Unzip Execution Time

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/files/operation/unzip/executionTime`   | Integer | `1000` seconds  | `config/files/operation/unzip/executionTime = 1200` |

#### Zip Execution Time

| Configuration Property Path                    | Type    | Default Value | Example                                   |
|------------------------------------------------|---------|---------------|-------------------------------------------|
| `config/files/operation/zip/executionTime`     | Integer | `1000` seconds  | `config/files/operation/zip/executionTime = 1200`  |

### Repository Configuration

Defines the location and migration directory for the repository. These are system options that should not be changed.

#### Repository Location

| Configuration Property Path                 | Type | Default Value               | Example                                |
|---------------------------------------------|------|-----------------------------|----------------------------------------|
| `config/repository/location`                | Path | `/opt/backendless/repo`     | `config/repository/location = /opt/backendless/repo`  |

#### Migration Directory

| Configuration Property Path                    | Type | Default Value               | Example                                |
|------------------------------------------------|------|-----------------------------|----------------------------------------|
| `config/repository/migration/dir`              | Path | `/opt/backendless/repo`     | `config/repository/migration/dir = /opt/backendless/repo`  |

---

### Max File (Body) Size Configuration

Adjust settings related to body size limits for parsers that buffer content on disk. These configurations are important for managing how data is processed and stored temporarily during operations in the application.

#### Maximum Disk Buffer Size

Configures the maximum size of a body for parsers that buffer content on disk, such as the raw parser or "multipart/form-data."

| Configuration Property Path                            | Type      | Default Value | Example                                            |
|--------------------------------------------------------|-----------|---------------|----------------------------------------------------|
| `config/playServer/play/http/parser/maxDiskBuffer`     | Data Size | `1G` (Gigabyte) | `config/playServer/play/http/parser/maxDiskBuffer = 2G` |

#### Maximum Content Length for Akka

Configures the maximum body size for Akka, aligning with the maximum value from `config.playServer.play.http.parser.maxDiskBuffer` or `config.playServer.play.http.parser.maxMemoryBuffer`. Ensures consistency in maximum allowable content size across different buffering strategies.

| Configuration Property Path                                  | Type      | Default Value | Example                                              |
|--------------------------------------------------------------|-----------|---------------|------------------------------------------------------|
| `config/playServer/akka/http/server/parsing/maxContentLength` | Data Size | `1G` (Gigabyte) | `config/playServer/akka/http/server/parsing/maxContentLength = 2G` |