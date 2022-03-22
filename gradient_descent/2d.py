"""
2d.py - shows charts of g(x) function
"""
from utils.gradient_descent import gradient_descent_for_charts
from utils.plot import Plot
from math import cos, pi, sin
from utils.settings import params_g
import numpy as np


def main():
    for x_start, step in params_g:
        minimum, keys = gradient_descent_for_charts(gradient_g,
                                                    x_start, step)
        abs_max = max(keys, key=lambda x: abs(x))
        borders = {"left": int(-3/2*abs_max),
                   "right": int(3/2*abs_max)}       # calculate plot borders
        values = [g(x) for x in keys]
        plot = Plot(keys, values, f"Value: {np.around(g(minimum), 5)}")
        plot.draw_function(g, borders, int(1 / step))
        print(f"({x_start}, {step}): {minimum}")    # print in terminal current experiment
        plot.show()


def g(x):
    return x**2-10*cos(2*pi*x)+10


def gradient_g(x):
    return 2*x+20*pi*sin(2*pi*x)


if __name__ == "__main__":
    main()
