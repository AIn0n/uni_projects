from population import Population
import genome_interface, random, math, copy

CITIES = [
    (119, 38), (37, 38), (197, 55), (85, 165), (12, 50), (100, 53), (81, 142),
    (121, 137), (85, 145), (80, 197), (91, 176), (106, 55), (123, 57), (40, 81),
    (78, 125), (190, 46), (187, 40), (37, 107), (17, 11), (67, 56), (78, 133),
    (87, 23), (184, 197), (111, 12), (66, 178)]

CITIES_IDX = [x for x in range(0, len(CITIES))]

def cross_over_order(parent1, parent2):
    output = copy.deepcopy(parent1)
    crosspoints = sorted(random.sample([x for x in range(len(parent1.genes))], k = 2)) + [len(parent1.genes)]
    output.genes.clear()
    idxs = [0, 0]
    genes = [parent1.genes, parent2.genes]
    curr = 0
    for c in crosspoints:
        while len(output.genes) < c:
            if not genes[curr][idxs[curr]] in output.genes:
                output.genes.append(genes[curr][idxs[curr]])
            idxs[curr] += 1
            if idxs[curr] >= len(genes[curr]):
                idxs[curr] = 0
        curr = 0 if curr else 1
    return output

class PointGenome(genome_interface.GenomeInterface):
    def __init__(self, value) -> None:
        self.value = value
    
    def randomize(self):
        self.value = random.choice(CITIES_IDX)

    def getValue(self):
        return self.value

    def reverse(self):
        pass

    def __repr__(self) -> str:
        return f"{self.value}"

    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value

distance = lambda a, b : math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def built_point_genome(num_of_genes):
    list_idx = copy.deepcopy(CITIES_IDX)
    random.shuffle(list_idx)
    return [PointGenome(n) for n in list_idx]

def distanceFitness(genes):
    genes_val = [x.getValue() for x in genes]
    output = 0
    last_point = CITIES[genes_val[0]]
    for gene in genes_val[1:]:
        output += distance(last_point, CITIES[gene])
        last_point = CITIES[gene]

    return (1.0 / output) if len(set(genes_val)) == len(genes) else 0


if __name__ == "__main__":
    population = Population(len(CITIES), built_point_genome, 100, distanceFitness)
    while population.population[0].fitness < 1.0 / 800:
        population.getNewPopulation(0.2, 0.01, cross_over_order)

    print(1.0 / population.population[0].fitness)
