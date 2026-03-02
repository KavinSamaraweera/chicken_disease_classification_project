# Entity is the return type of a function. If you don't have in-built return type, it needs to create custom return type.

#So, create data ingestion related config or entity
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:

    #these are getting from config.yaml
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path