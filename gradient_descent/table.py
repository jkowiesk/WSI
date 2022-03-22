"""
table.py - makes two csv files with results of experiments in ./csv folder
"""
import csv
from utils.gradient_descent import gradient_descent
from math import cos, pi, sin
import numpy as np
from utils.settings import params_f, params_g


def main():
    fields = ["Start X", "Step Size", "Minimum", "Value"]
    with open("./csv/gradient_descent_g(x).csv", "w") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        for start_x, step_size in params_g:
            minimum = gradient_descent(g, gradient_g, start_x, step_size)
            minimum = np.around(minimum, 5)
            value = np.around(g(minimum), 2)
            csvwriter.writerow([start_x, step_size, minimum, value])

    with open("./csv/gradient_descent_f(x).csv", "w") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        for start_x, step_size in params_f:
            minimum = gradient_descent(f, gradient_f, start_x, step_size)
            minimum = np.around(minimum, 5)
            value = np.around(f(minimum), 2)
            csvwriter.writerow([start_x, step_size, minimum, value])


def g(x):
    return x**2-10*cos(2*pi*x)+10


def gradient_g(x):
    return 2*x+20*pi*sin(2*pi*x)


def f(x):
    return x[0]**2+x[1]**2


def gradient_f(x):
    return 2*x[0], 2*x[1]


if __name__ == "__main__":
    main()
