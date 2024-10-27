from pathlib import Path

import yaml
from pydantic import BaseModel, Field

class Config(BaseModel):
    command: str | None = None

    @staticmethod
    def read_yaml(file_path: Path, section: str | None = None):
        with open(file_path) as f:
            config_data = yaml.safe_load(f)
            if section is None:
                return config_data
            return config_data[section]

    

class CreationConfig(Config):
    command: str = "create"
    first_names: Path = Field()
    surnames: Path = Field()
    people: int = Field(default=10000)
    output_dir: Path = Field()

    @classmethod
    def from_yaml(cls, file_path: Path):
        config_data = cls.read_yaml(file_path, "create")
        return cls.model_validate(config_data)
    

class ParseConfig(Config):
    command: str = "parse"
    input_dir: Path = Field()

    @classmethod
    def from_yaml(cls, file_path: Path):
       config_data = cls.read_yaml(file_path, "parse")
       return cls.model_validate(config_data)