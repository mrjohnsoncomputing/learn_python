from dataclasses import dataclass, field
from random import choice

START_SEQUENCE = "ATG"
END_SEQUENCE = "TAA"


@dataclass
class Codon:
    sequence: list[str] = field(default_factory=list)

    def __str__(self):
        return ''.join(self.sequence)

    @classmethod
    def from_string(cls, codon_string):
        return cls(sequence=list(codon_string))

    @classmethod
    def from_random(cls):
        options: list[str] = ["A", "C", "G", "T"]
        count: int = 3
        sequence = START_SEQUENCE
        while sequence in [START_SEQUENCE, END_SEQUENCE]:
            sequence = [choice(options) for x in range(count)]
        return cls(sequence=sequence)
