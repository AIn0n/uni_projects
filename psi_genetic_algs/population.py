from black import out
from speciman import Speciman
import random

class Population:
    def __init__(self, num_of_genes, genomeConstructor, populationSize, fitFun) -> None:
        self.population = [
            Speciman(num_of_genes, genomeConstructor) for _ in range(populationSize)
        ]
        self.fitnessFunction = fitFun
        self.evalFitness()

    def evalFitness(self):
        for elem in self.population:
            elem.fitness = self.fitnessFunction(elem.genes)

    def getNewPopulation(self, elitarism_precentage :float, mut_prob :float, crossover_method=Speciman.getNewSpeciman):
        assert elitarism_precentage <= 1.0 and mut_prob <= 1.0 # arguments checking
        # with elitarism we take upper, better part of population so we need to first sort it
        self.population.sort(key= lambda x : x.fitness, reverse=True)
        # from precentage we want to get number of specimen who stay as elite
        num_of_elit = int(elitarism_precentage * len(self.population))
        output = self.population[: num_of_elit]
        fitness = [x.fitness for x in self.population]
        if all(x == 0 for x in fitness):
            fitness = None
        while len(output) < len(self.population):
            parents = random.choices(self.population, weights=fitness, k=2)
            new = crossover_method(*parents)
            new.mutate(mut_prob)
            output.append(new)
        self.population = output
        self.evalFitness()