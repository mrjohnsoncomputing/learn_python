from dataclasses import dataclass, field
from random import choice
from abc import ABC

CANCER_SEQUENCE = "AAA"

@dataclass
class Codon:
    sequence: list[str] = field(default_factory=list)

    def __str__(self):
        return "".join(self.sequence)

    @classmethod
    def from_string(cls, codon_string):
        return cls(sequence=list(codon_string))
        
    @classmethod
    def from_healthy(cls):
        options: list[str] = ["A", "C", "G", "T"]
        count: int = 3
        sequence = CANCER_SEQUENCE
        while sequence in [CANCER_SEQUENCE]:
            sequence = [choice(options) for x in range(count)]
        return cls(sequence=sequence)
    
    @classmethod       
    def from_cancer(cls):
        return cls(
            sequence = list(CANCER_SEQUENCE)
        )
                
