from utils.genetic_algorithm import genetic_algorithm, genetic_algorithm_for_charts
from utils.setup import generete_population, fitting_function
from utils.plot import Plot


def run_simulation():
    population_size = int(input("Size of population: "))
    crossover_prob = float(input("Crossover probability: "))
    mutation_prob = float(input("Mutation probability: "))
    population = generete_population(20, population_size)
    print(population)
    best_individual, best_rating, keys, values = \
    genetic_algorithm_for_charts(fitting_function, population, mutation_prob, crossover_prob)
    print(best_individual, best_rating)
    plot = Plot(keys, values, "Algortihm Visualization")
    plot.manipulate_plot(labels={"x": "iteration", "y": "averege rating"})
    plot.show()



if __name__ == "__main__":
    run_simulation()
