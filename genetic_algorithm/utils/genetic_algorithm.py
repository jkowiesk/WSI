from utils.operations import rate_population, find_best, reproduce, \
                             crossover, mutate

RANGE = 10000


def genetic_algorithm(fitting_function, population,
                      mutation_prob=0.5, crossing_prob=1):
    ratings = rate_population(fitting_function, population)
    best_individual, best_rating = find_best(ratings, population)
    for _ in range(RANGE):
        offspring = reproduce(population, ratings)
        offspring = crossover(offspring, crossing_prob)
        offspring = mutate(offspring, mutation_prob)

        ratings = rate_population(fitting_function, offspring)
        new_best_individual, new_best_rating = find_best(ratings, offspring)
        if new_best_rating >= best_rating:
            best_individual = new_best_individual
            best_rating = new_best_rating

        population = offspring
    return best_individual, best_rating


def genetic_algorithm_for_charts(fitting_function, population,
                                 mutation_prob=0.5, crossing_prob=1):
    ratings = rate_population(fitting_function, population)
    best_individual, best_rating = find_best(ratings, population)
    keys, values = [], []
    for i in range(RANGE):
        offspring = reproduce(population, ratings)
        offspring = crossover(offspring, crossing_prob)
        offspring = mutate(offspring, mutation_prob)

        ratings = rate_population(fitting_function, offspring)
        new_best_individual, new_best_rating = find_best(ratings, offspring)
        if new_best_rating >= best_rating:
            best_individual = new_best_individual
            best_rating = new_best_rating

        population = offspring
        avarage = 0
        for rating in ratings:
            avarage += rating
        avarage /= len(population)
        if (i % 100 == 0):
            keys.append(i)
            values.append(avarage)

    return best_individual, best_rating, keys, values
