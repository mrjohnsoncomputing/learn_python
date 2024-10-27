from dataclasses import dataclass, field
from random import choice, random
from .gene import Gene, GENES
from .codon import START_SEQUENCE, END_SEQUENCE


@dataclass
class Dna:
    sequence: list[Gene] = field(default_factory=list)

    @classmethod
    def from_string(cls, dna_string: str):
        sequence = []
        index = 0
        while index < len(dna_string):
            codon_string = dna_string[index:index + 3]
            if codon_string == START_SEQUENCE:
                end_index = codon_string.find(END_SEQUENCE)
                gene = dna_string[index:end_index]
                sequence.append(Gene.from_string(gene))
            else:
                index += 1
        return cls(sequence=sequence)

    @classmethod
    def from_random(cls):
        missing_gene = random() > 0.99
        genes = len(GENES)

        sequence = []
        for i in range(genes):
            sequence.append(Gene.from_random())

        if missing_gene:
            sequence.remove(choice(sequence))
        return cls(sequence=sequence)

    def __str__(self) -> str:
        return "".join([str(x) for x in self.sequence])
