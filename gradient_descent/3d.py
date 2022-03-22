"""
3d.py - shows charts of f(x) function
"""
from utils.gradient_descent import gradient_descent_for_charts
from utils.plot3D import Plot3D
from utils.settings import params_f
from math import ceil, floor
import numpy as np


def main():
    for point_start, step in params_f:
        minimum, points = gradient_descent_for_charts(gradient_f,
                                                      point_start, step)
        X, Y = list(), list()
        for x, y in points:
            X.append(x)
            Y.append(y)
        Z = [f(np.array([x, y])) for x, y in zip(X, Y)]
        x_left, y_left, z_left = floor(3/2*min(X)), floor(3/2*min(Y)), floor(3/2*min(Z))
        x_right, y_right, z_right = ceil(3/2*max(X)), ceil(3/2*max(Y)), ceil(3/2*max(Z))
        borders = {"x": [x_left, x_right],
                   "y": [y_left, y_right],
                   "z": [z_left, z_right]}              # create plot borders

        plot = Plot3D(X, Y, Z, borders)
        plot.draw_function(f)
        print(f"({point_start},{step}): {minimum}")     # print in terminal current experiment
        plot.show()


def f(x):
    return x[0]**2+x[1]**2


def gradient_f(x):
    return 2*x[0], 2*x[1]


if __name__ == "__main__":
    main()
