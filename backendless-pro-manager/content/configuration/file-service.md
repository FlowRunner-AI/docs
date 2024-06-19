# Files Service Configuration

This section outlines the configuration settings for the Files Service operations within your application. These settings control file compression operations and define important system paths that are typically set during initial setup and not modified thereafter.

#### File Operation Execution Times

- **`config/files/operation/unzip/executionTime`**
    - **Description:** Specifies the maximum allowed execution time for the unzip operation, in seconds.
    - **Type:** Integer
    - **Default:** `1000` seconds
    - **Example:** `config/files/operation/unzip/executionTime = 1200`

- **`config/files/operation/zip/executionTime`**
    - **Description:** Specifies the maximum allowed execution time for the zip operation, in seconds.
    - **Type:** Integer
    - **Default:** `1000` seconds
    - **Example:** `config/files/operation/zip/executionTime = 1200`

#### Repository Configuration

- **`config/repository/location`**
    - **Description:** Defines the location of the repository. This is a system option that should not be changed.
    - **Type:** Path
    - **Default:** `/opt/backendless/repo`
    - **Example:** `config/repository/location = /opt/backendless/repo`

- **`config/repository/migration/dir`**
    - **Description:** Specifies the directory for migration within the repository. This is a system option that should not be changed.
    - **Type:** Path
    - **Default:** `/opt/backendless/repo`
    - **Example:** `config/repository/migration/dir = /opt/backendless/repo`


Here is the added documentation for the configuration settings related to body size limitations for parsers in your system:

---

### Max file(body) size that can be uploaded to Backendless PRO 

Adjust settings related to body size limits for parsers that buffer content on disk. These configurations are important for managing how data is processed and stored temporarily during operations in the application.

#### Maximum Disk Buffer Size

- **`config/playServer/play/http/parser/maxDiskBuffer`**
    - **Description:** Configures the maximum size of a body for parsers that buffer content on disk, such as the raw parser or "multipart/form-data."
    - **Type:** Data Size
    - **Default:** `1G` (Gigabyte)
    - **Example:** `config/playServer/play/http/parser/maxDiskBuffer = 2G`

#### Maximum Content Length for Akka

- **`config/playServer/akka/http/server/parsing/maxContentLength`**
    - **Description:** Configures the maximum body size for Akka, aligning with the maximum value from `config.playServer.play.http.parser.maxDiskBuffer` or `config.playServer.play.http.parser.maxMemoryBuffer`. Ensures consistency in maximum allowable content size across different buffering strategies.
    - **Type:** Data Size
    - **Default:** `1G` (Gigabyte)
    - **Example:** `config/playServer/akka/http/server/parsing/maxContentLength = 2G`

