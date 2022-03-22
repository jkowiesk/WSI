import numpy as np
from random import randint, random
from utils.gray import genetic_to_dec

GENOTYPE_SIZE = 20
MUTATION_NUM = 4


def rate_population(fitting_function, population):
    ratings = []
    for individual in population:
        value = genetic_to_dec(individual)
        ratings.append(-1*fitting_function(value))
    return ratings


def find_best(ratings, population):
    best_index = np.argmax(ratings)
    return population[best_index], ratings[best_index]


def translate_ratings(ratings):
    translate_ratings = []
    min_individual = min(ratings) - 1
    for rating in ratings:
        translate_ratings.append(rating - min_individual)
    return translate_ratings


def reproduce(population, ratings):
    population_num = len(population)
    translated_ratings = translate_ratings(ratings)
    sum_of_ratings = sum(translated_ratings)
    new_population = []
    while len(new_population) < population_num:
        pretender_index = randint(0, population_num - 1)
        adaptation = translated_ratings[pretender_index] / sum_of_ratings
        if random() < adaptation:
            new_population.append(population[pretender_index])
    return new_population


def crossover(population, crossing_prob):
    population_num = len(population)
    new_population = []
    parents_indexs = [x * 2 for x in range(population_num // 2)]
    for i in parents_indexs:
        parents = population[i:i+2]
        if random() < crossing_prob:
            cut = randint(0, GENOTYPE_SIZE)
            kids = []
            kids.append(parents[0][:cut] + parents[1][cut:])
            kids.append(parents[1][:cut] + parents[0][cut:])

            for kid in kids:
                new_population.append(kid)
        else:
            for parent in parents:
                new_population.append(parent)
    if (population_num % 2) != 0:
        new_population.append(population[-1])
    return new_population


def mutate(population, mutation_prob):
    new_population = []
    for individual in population:
        if random() < mutation_prob:
            for _ in range(MUTATION_NUM):
                rand_index = randint(0, GENOTYPE_SIZE - 1)
                individual[rand_index] = abs(individual[rand_index] - 1)
        new_population.append(individual)
    return new_population
