from utils.genetic_algorithm import genetic_algorithm
from utils.setup import fitting_function
import numpy as np
from utils.params import params
import csv

RANGE = 25


def main():
    j = 1
    fields = ["Population Size", "Crossing Prob", "Mutation Prob",
              "Arithmetic Average", "Standard deviation"]
    with open("./csv/holland_algorithm.csv", "w") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        for population, crossing_prob, mutation_prob in params:
            ratings = []
            avarage = 0
            for i in range(RANGE):
                best_individual, best_rating = genetic_algorithm(fitting_function, population,
                                                                 mutation_prob, crossing_prob)
                avarage += best_rating
                ratings.append(best_rating)
                print(i)
            avarage /= RANGE
            deviation = 0
            for rating in ratings:
                deviation += (rating - avarage)**2
            deviation = np.around((deviation/RANGE)**(1/2), 2)
            avarage = np.around(avarage, 2)
            csvwriter.writerow([len(population), crossing_prob,
                                mutation_prob, avarage, deviation])
            print(f"Parametr {j} finished.")
            j += 1


if __name__ == "__main__":
    main()
