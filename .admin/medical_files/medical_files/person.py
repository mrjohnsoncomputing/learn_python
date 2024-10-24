from random import choice, randint
from enum import Enum
from dataclasses import dataclass

from .dna import Dna


class Sex(Enum):
    male = "male"
    female = "female"


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    sex: Sex
    dna: Dna

    @classmethod
    def from_random(cls, firstnames: list[str], surnames: list[str]):
        return cls(first_name=choice(firstnames),
                   last_name=choice(surnames),
                   age=randint(1, 100),
                   sex=choice([x.value for x in Sex]),
                   dna=Dna.from_random())
    @classmethod
    def from_string(cls, person_string: str, dna: str):
        elements = person_string.replace("(", "-").replace(",", "-").replace(")", "").split("-")
        return cls(
            first_name=elements[0],
            last_name=elements[1],
            age=elements[2],
            sex=Sex[elements[3]],
            dna = Dna.from_string(dna))
    
    def __str__(self) -> str:
        return f"{self.first_name}-{self.last_name}({self.age},{self.sex})"
