from random import randint, random
from .codon import HealthyCodon, CancerCodon, Codon


class Dna:
    sequence: list[Codon]
    count: int

    def __init__(self):
        r = random()
        self.has_cancer = r > 0.999
        self.count = randint(50, 64)
        self.sequence = self._get_codons()

    def _get_codons(self):
        sequence = []
        for i in range(self.count):
            sequence.append(HealthyCodon())

        if self.has_cancer:
            position = randint(0, len(sequence) - 1)
            sequence[position] = CancerCodon()
            print("Applying Cancer")
        return sequence

    def __str__(self) -> str:
        return "".join([str(x) for x in self.sequence])
