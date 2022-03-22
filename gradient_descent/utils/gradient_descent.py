"""
gradient_descent.py - gradient descent algorithm
"""
from typing import Tuple
import numpy as np

RANGE = 1000


def gradient_descent(gradient_f, start_x, step_size) -> float:
    x = np.array(start_x, dtype=np.float64)
    for i in range(RANGE):
        x -= step_size * np.array(gradient_f(x), dtype=np.float64)
    return x


def gradient_descent_for_charts(gradient_f,
                                start_x, step_size) -> Tuple[float, list]:
    x = np.array(start_x, dtype=np.float64)
    x_list = [np.copy(x)]
    for i in range(RANGE):
        x -= step_size * np.array(gradient_f(x), dtype=np.float64)
        x_list.append(np.copy(x))
    return x, x_list
