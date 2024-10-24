from dataclasses import dataclass
from random import randint, random
from .codon import Codon, CANCER_SEQUENCE

@dataclass
class Dna:
    sequence: list[Codon]
    count: int
    has_cancer: bool = False

    @classmethod
    def from_string(cls, dna_string: str):
        sequence = []
        has_cancer = False
        for i in range(0, len(dna_string), 3):
            codon_string = dna_string[i:i+3]
            if codon_string == CANCER_SEQUENCE:
                has_cancer = True
            sequence.append(Codon.from_string(codon_string))
        return cls(
            sequence=sequence,
            count=len(sequence),
            has_cancer=has_cancer)
    
    @classmethod
    def from_random(cls):
        r = random()
        return cls(
            has_cancer = r > 0.999,
            count = randint(50, 64),
            sequence = self._get_codons())
        
    def _get_codons(self):
        sequence = []
        for i in range(self.count):
            sequence.append(Codon.from_healthy())

        if self.has_cancer:
            position = randint(0, len(sequence) - 1)
            sequence[position] = Codon.from_cancer()
        return sequence

    def __str__(self) -> str:
        return "".join([str(x) for x in self.sequence])
