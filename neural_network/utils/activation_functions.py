import numpy as np


def sigmoid(x) -> float:
    return 1/(1 + np.exp(-x))


def d_sigmoid(x) -> float:
    return sigmoid(x) * (1 - sigmoid(x))


def ReLu(x) -> float:
    return max(0, x)


def d_ReLu(x) -> float:
    if x < 0:
        return 0
    elif x > 0:
        return 1
    else:
        raise Exception("Arg of d_ReLu cant be 0")
