from population import Population
from genome_binary import BinaryGenome, binary_genome_constructor

def countOnes(genes):
    return sum(x.getValue() for x in genes)

if __name__ == "__main__":
    population = Population(10, binary_genome_constructor, 10, countOnes)
    for _ in range(100):
        population.getNewPopulation(0.2, 0.05)
    print(list(map(lambda x: x.getValue(), population.population[0].genes)))
    print(population.population[0].fitness)