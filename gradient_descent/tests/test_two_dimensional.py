from utils.gradient_descent import gradient_descent
import numpy as np


def test_f_function():
    minimum = gradient_descent(gradient_f, [10, 10], 0.1)
    assert([int(x) for x in minimum] == [0, 0])


def f(x):
    return x[0]**2+x[1]**2


def gradient_f(x):
    return np.array([2*x[0], 2*x[1]])
