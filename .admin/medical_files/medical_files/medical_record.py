from pathlib import Path

from .person import Person


class MedicalRecord:

    def __init__(self, person: Person) -> None:
        self._person = person

    def write(self, output_directory: Path):
        file_path = output_directory.joinpath(str(self._person))
        with open(file_path, "w") as f:
            f.write(str(self._person.dna))
