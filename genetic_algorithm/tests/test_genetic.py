from random import randint
from utils.gray import gray_to_dec
from utils.setup import fitting_function, generete_population
from utils.genetic_algorithm import genetic_algorithm
from utils.operations import reproduce, crossover, mutate
import numpy as np


def test_reproduce_even(monkeypatch):
    individual_num = 5
    cut = 3
    population = generete_population(individual_num, 4)
    parents_indexes = [x * 2 for x in range(len(population) // 2)]
    expected_population = []
    for i in parents_indexes:
        expected_population.append(population[i][:cut] + population[i+1][cut:])
        expected_population.append(population[i+1][:cut] + population[i][cut:])

    monkeypatch.setattr("utils.operations.GENOTYPE_SIZE", 5)
    monkeypatch.setattr("utils.operations.randint", lambda x, y: cut)
    offspring = crossover(population, 1)
    assert offspring == expected_population


def test_reproduce_odd(monkeypatch):
    individual_num = 5
    cut = 3
    population = generete_population(individual_num, 5)
    parents_indexes = [x * 2 for x in range(len(population) // 2)]
    expected_population = []
    for i in parents_indexes:
        expected_population.append(population[i][:cut] + population[i+1][cut:])
        expected_population.append(population[i+1][:cut] + population[i][cut:])
    expected_population.append(population[-1])

    monkeypatch.setattr("utils.operations.GENOTYPE_SIZE", 5)
    monkeypatch.setattr("utils.operations.randint", lambda x, y: cut)
    offspring = crossover(population, 1)
    assert offspring == expected_population


def test_fitting_function_borders():
    x = []
    for y1 in range(-16, 16):
        for y2 in range(-16, 16):
            for y3 in range(-16, 16):
                for y4 in range(-16, 16):
                    x.append([y1, y2, y3, y4])

    values = [int(fitting_function(num)) for num in x]
    minimum = min(values)
    maximum = max(values)
    assert minimum == 0 and maximum == 6771


def test_simple_fitting_function(monkeypatch):
    individual_num = 5
    population = generete_population(individual_num, 4)
    monkeypatch.setattr("utils.operations.genetic_to_dec", gray_to_dec)
    monkeypatch.setattr("utils.operations.GENOTYPE_SIZE", 5)
    best_individual, best_rating = genetic_algorithm(lambda x: x**2, population)
    assert best_individual == [1, 1, 0, 0, 0]
