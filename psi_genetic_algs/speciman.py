import copy
import random

class Speciman:
    def __init__(self, num_of_genes, genomeConstructor) -> None:
        self.fitness = 0
        self.genes = genomeConstructor(num_of_genes)
        self.idx_cache = [i for i in range(len(self.genes))]

    def mutate(self, mutation_prob :float):
        if random.random() < mutation_prob:
            mutate_function = random.choice([self.mutate_inverse, self.mutate_reverse, self.mutate_swap])
            mutate_function()

    def get_n_random_idxs(self, n):
        output = random.sample(self.idx_cache, k=n)
        return output[0] if n == 1 else output

    def mutate_reverse(self):
        self.genes[self.get_n_random_idxs(1)].reverse()

    def mutate_swap(self):
        i1, i2 = self.get_n_random_idxs(2)
        self.genes[i1], self.genes[i2] = self.genes[i2], self.genes[i1]

    def mutate_inverse(self):
        start, end = sorted(self.get_n_random_idxs(2))
        self.genes = self.genes[:start] + list(reversed(self.genes[start:end])) + self.genes[end:]

    @staticmethod
    def getNewSpeciman(parent1, parent2):
        output = copy.deepcopy(parent1)
        crosspoint = random.randint(0, len(output.genes))
        output.genes[:crosspoint] = parent2.genes[:crosspoint]
        return output