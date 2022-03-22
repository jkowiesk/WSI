import numpy as np


class Layer:
    def __init__(self, size, prev_size=None):
        if prev_size:
            self.weights = np.random.randn(size, prev_size)
            self.biases = np.random.randn(size)
        else:
            self.weights = None
            self.biases = None

        self.size = size
        self.results = []
        self.activations = []
