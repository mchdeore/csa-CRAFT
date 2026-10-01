# connectors

Data-source connectors. `LocalFileSource` reads from a filesystem root (configurable via `CONNECTORS_ROOT`, defaults to `~/Documents`). Future SharePoint/S3/Samba sources will land as siblings implementing the same `DataSource` protocol.
