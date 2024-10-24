from pathlib import Path

from .person import Person
from .medical_record import MedicalRecord
from .config import CreationConfig, ParseConfig
import click

def get_names(file_path: Path) -> list[str]:
    with open(file_path) as f:
        return f.read().splitlines()

@click.group()
def main():
    pass

@main.command()
@click.option("--config-file")
def create(config_file: str):
    file_path = Path(config_file)
    if not file_path.is_file():
        raise FileNotFoundError(f"Unable to find file: {file_path.resolve()}")
    config = CreationConfig.from_yaml(file_path)

    config.output_dir.mkdir(parents=True, exist_ok=True)
    firstnames = get_names(config.first_names)
    surnames = get_names(config.surnames)

    cancer_count = 0
    for i in range(config.people):
        person = Person.from_random(firstnames, surnames)
        medical_file = MedicalRecord(person)
        medical_file.write(config.output_dir)
        if medical_file.signs_of_cancer:
            cancer_count += 1
    print("Cancer Victims Created:", cancer_count)

@main.command()
@click.option("--config-file")
def parse(config_file: str):
    file_path = Path(config_file)
    if not file_path.is_file():
        raise FileNotFoundError(f"Unable to find file: {file_path.resolve()}")
    config = ParseConfig.from_yaml(file_path)
    count = 0
    for file_path in config.input_dir.glob("*.txt"):
        r = MedicalRecord.from_file(file_path)
        if r.signs_of_cancer:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
