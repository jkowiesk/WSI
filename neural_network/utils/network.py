from utils.layer import Layer
import numpy as np


class Network:
    def __init__(self, sizes, activation_func, d_activation_func, alpha=0.5):
        self.layers = []
        self.layers.append(Layer(sizes[0]))
        new_sizes = []
        for size in sizes:
            if isinstance(size, list):
                for x in size:
                    new_sizes.append(x)
            else:
                new_sizes.append(size)
        sizes = new_sizes

        for x, y in zip(sizes[:-1], sizes[1:]):
            self.layers.append(Layer(y, x))

        self.activation_func = activation_func
        self.d_activation_func = d_activation_func
        self.layers_num = len(self.layers)
        self.alpha = alpha

    def predict(self, example):
        self.layers[0].activations = [self.activation_func(x) for x in example]
        for prev_layer, layer in zip(self.layers[:-1], self.layers[1:]):
            results = np.dot(layer.weights, prev_layer.activations)
            results = np.add(results, layer.biases)
            layer.results = results
            layer.activations = [self.activation_func(x) for x in results]
        return self.layers[-1].activations

    def learn(self, examples, values):
        examples_gradients = []
        for example, value in zip(examples, values):
            layer_gradients = []
            d_costs = self.get_d_costs(example, [1 if x == value else 0 for x in range(self.layers[-1].size)])
            for prev_layer, layer in zip(self.layers[::-1][1:], self.layers[::-1][:-1]):
                gradients = [[], []]
                new_d_costs = []
                for j in range(layer.size):
                    weight_gradient = []
                    d_activation = self.d_activation_func(layer.results[j])
                    bias_gradient = d_activation * d_costs[j]
                    gradients[1].append(bias_gradient)
                    for k in range(prev_layer.size):
                        weight_gradient.append(prev_layer.activations[k] * bias_gradient)
                    gradients[0].append(weight_gradient)
                layer_gradients.append(gradients)

                for k in range(prev_layer.size):
                    activation_gradient = 0
                    for j in range(layer.size):
                        d_activation = self.d_activation_func(layer.results[j])
                        activation_gradient += layer.weights[j][k] * d_activation * d_costs[j]
                    new_d_costs.append(activation_gradient)
                d_costs = new_d_costs
            examples_gradients.append(layer_gradients)

        avg_gradients = self.calculate_avg_gradients(examples_gradients)
        self.change_weights_and_biases(avg_gradients)

        return

    def calculate_avg_gradients(self, examples_gradients):
        examples_num = len(examples_gradients)
        avg_gradients = examples_gradients[0]

        for example_gradients in examples_gradients[1:]:
            for i in range(self.layers_num - 1):
                avg_gradients[i][0] = np.add(avg_gradients[i][0], example_gradients[i][0])
                avg_gradients[i][1] = np.add(avg_gradients[i][1], example_gradients[i][1])

        for i in range(self.layers_num - 1):
            avg_gradients[i][0] = np.dot(avg_gradients[i][0], 1/examples_num)
            avg_gradients[i][1] = np.dot(avg_gradients[i][1], 1/examples_num)

        return avg_gradients

    def change_weights_and_biases(self, avg_gradients):
        for layer, avg_gradient in zip(self.layers[::-1][:-1], avg_gradients):
            layer.weights = np.add(layer.weights, -self.alpha*avg_gradient[0])
            layer.biases = np.add(layer.biases, -self.alpha*avg_gradient[1])

    def get_d_costs(self, example, desired_output: list):
        activations = self.predict(example)
        d_costs = []
        for activation, y in zip(activations, desired_output):
            d_costs.append(2*(activation - y))
        return d_costs

    def calculate_cost(self, example, desired_output: list):
        activations = self.predict(example)
        cost = 0
        for activation, y in zip(activations, desired_output):
            cost += (activation - y)**2
        return cost
