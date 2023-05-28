from population import Population
from genome_binary import BinaryGenome, binary_genome_constructor

ITEMS_VALUES = [266, 442, 671, 526, 388, 245, 210, 145, 126, 322]
ITEMS_WEIGHTS = [3, 13, 10, 9, 7, 1, 8, 8, 2, 9]
MAX_WEIGHT = 35

def get_stolen_values(genes):
    idxs = [x.getValue() for x in genes]
    weight = sum(ITEMS_WEIGHTS[i] for i in range(len(idxs)) if idxs[i])
    value = sum(ITEMS_VALUES[i] for i in range(len(idxs)) if idxs[i])
    return value if weight <= MAX_WEIGHT else 0

if __name__ == "__main__":
    population = Population(len(ITEMS_VALUES), binary_genome_constructor, 8, get_stolen_values)
    
    for _ in range(200):
        population.getNewPopulation(0.2, 0.05)
    
    print(get_stolen_values(population.population[0].genes))