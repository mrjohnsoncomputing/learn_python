from pathlib import Path
from dataclasses import dataclass
from .person import Person

@dataclass
class MedicalRecord:
    _person: Person

    @property
    def signs_of_cancer(self):
        return self._person.dna.has_cancer
    
    @classmethod
    def from_person(cls, person: Person):
        return cls(_person = person)

    def write(self, output_directory: Path):
        file_path = output_directory.joinpath(str(self._person) + ".txt")
        with open(file_path, "w") as f:
            f.write(str(self._person.dna))

    @classmethod
    def from_file(cls, file_path: Path):
        with open(file_path) as f:
            dna = f.read()
        self._person = Person.from_string(file_path.stem, dna)
        print(person)
        return cls(_person=person)
