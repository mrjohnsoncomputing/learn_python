from pathlib import Path

from .person import Person
from .medical_record import MedicalRecord


def get_names(file_path: Path) -> list[str]:
    with open(file_path) as f:
        return f.read().splitlines()


def main():
    output_dir = Path("./.data/medical_files")
    output_dir.mkdir(parents=True, exist_ok=True)

    firstnames = get_names(Path("./.data/firstnames.txt"))
    surnames = get_names(Path("./.data/surnames.txt"))

    people = 10000
    for i in range(people):
        person = Person.from_random(firstnames, surnames)
        medical_file = MedicalRecord(person)
        medical_file.write(output_dir)


if __name__ == "__main__":
    main()
