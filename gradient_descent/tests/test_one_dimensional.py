from utils.gradient_descent import gradient_descent
import numpy as np
from math import cos, pi, sin


def test_g_function():
    minimum = gradient_descent(lambda x: 2*x+20*pi*sin(2*pi*x), [10], 0.001)
    assert(minimum == np.array(9.948716357505246))

