from random import choice
from abc import ABC

CANCER_SEQUENCE = "AAA"


class Codon(ABC):
    _options: list[str] = ["A", "C", "G", "T"]
    _count: int = 3
    _sequence: list[str] = []

    def __str__(self):
        return "".join(self._sequence)


class HealthyCodon(Codon):

    def __init__(self):
        self._sequence = self.create_sequence()

    def create_sequence(self):
        sequence = CANCER_SEQUENCE
        while sequence in [CANCER_SEQUENCE]:
            sequence = [choice(self._options) for x in range(self._count)]
        return sequence


class CancerCodon(Codon):
    _sequence: list[str] = ["A", "A", "A"]
