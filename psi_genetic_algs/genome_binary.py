import random
from genome_interface import GenomeInterface

class BinaryGenome(GenomeInterface):
    def __init__(self) -> None:
        self.value = 0
        self.randomize()

    def randomize(self):
        self.value = random.choice([0, 1])

    def getValue(self):
        return self.value

    def reverse(self):
        self.value = 0 if self.value else 1

def binary_genome_constructor(num_of_genes :int) -> list:
    return [BinaryGenome() for _ in range(num_of_genes)]