#!/usr/bin/python3
# -*-coding: utf-8 -*

import random
from pyeasyga.pyeasyga import pyeasyga
from operator import attrgetter


# generated at random
# each weight or threshold is a single gene within the genome and is a real number in range [0,1]
def create_individual(data: [str]) -> [float]:
    return [random.uniform(0, 1) for _ in range(len(data))]


def one_point_crossover(parent_1: [float], parent_2: [float]) -> ([float], [float]):
    crossover_index = random.randrange(1, len(parent_1))
    child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
    child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
    return child_1, child_2


def simple_mutation(individual: [float]) -> [float]:
    mutate_index = random.randrange(len(individual))
    individual[mutate_index] = random.uniform(0, 1)


# the selection probability is proportional to the fitness of the individual
def roulette_wheel_selector(population: [pyeasyga.Chromosome]) -> pyeasyga.Chromosome:
    sum_of_fitness = 0
    fitnesses = []
    # sort from worst to fittest individual
    population.sort(key=attrgetter('fitness'))

    for individual in population:
        fitnesses.append(individual.fitness)
        sum_of_fitness += individual.fitness

    alea = random.random() * sum_of_fitness

    for i in range(len(population)):
        if fitnesses[i] < alea:
            return population[i]

    # when rounding errors occur, we return the fittest individual
    return population[-1]


def fitness(individual: [float], data: [str]) -> float:
    # TODO

    # example
    # fitness = 0
    # if individual.count(1) == 2:
    #     for (selected, (fruit, profit)) in zip(individual, data):
    #         if selected:
    #             fitness += profit
    # return fitness

    return 0


def run_ga(data: [str], population_size: int, generations: int, crossover_proba: float,
           mutation_proba: float, elitism: bool):
    ga = pyeasyga.GeneticAlgorithm(data, population_size, generations, crossover_proba, mutation_proba, elitism)

    ga.create_individual = create_individual
    ga.crossover_function = one_point_crossover
    ga.mutate_function = simple_mutation
    ga.selection_function = roulette_wheel_selector
    ga.fitness_function = fitness

    random.seed()
    ga.run()
    print(ga.best_individual())


