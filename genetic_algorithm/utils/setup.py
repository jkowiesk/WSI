from math import sin
from random import randint


def fitting_function(x):
    sum = (x[0] + 2*x[1] - 7)**2
    sum += (2*x[0] + x[1] - 5)**2
    sum += sin(1.5*x[2])**3
    sum += (x[2] - 1)**2 * (1 + sin(1.5*x[3])**2)
    sum += (x[3] - 1)**2 * (1 + sin(x[3])**2)
    return sum


def generete_population(individual_size, population_num):
    population = []
    for _ in range(population_num):
        individual = []
        for __ in range(individual_size):
            individual.append(randint(0, 1))
        population.append(individual)
    return population
