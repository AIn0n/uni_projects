from population import Population
from genome_binary import BinaryGenome, binary_genome_constructor

# global lambdas
convert_to_int = lambda l : int("".join(str(n.getValue()) for n in l), 2)
equation = lambda a, b : 2 * (a ** 2) + b

def get_a_b_from_genes(genes):
    return convert_to_int(genes[:4]), convert_to_int(genes[4:])

def countFunction(genes):
    return 1 if equation(*get_a_b_from_genes(genes)) == 33 else -1

if __name__ == "__main__":
    population = Population(8, binary_genome_constructor, 10, countFunction)
    while population.population[0].fitness != 1:
        population.getNewPopulation(0.5, 0.1)

    a, b = get_a_b_from_genes(population.population[0].genes)
    print(f"a = {a}, b = {b}, 2 * {a}^2 + {b} = {equation(a, b)}")