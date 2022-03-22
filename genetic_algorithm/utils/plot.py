"""
plot.py - simple class for 2d plots
"""
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, keys, values, plot_label=None):
        self.plot_label = plot_label
        plt.scatter(keys, values, marker='o', color="r")
        plt.xlabel(plot_label)
        plot = plt.gca()
        plot.spines['top'].set_color('none')
        plot.spines['bottom'].set_position('zero')
        plot.spines['left'].set_position('zero')
        plot.spines['right'].set_color('none')

    def save_to_file(self, file_name):
        plt.savefig(file_name)
        plt.cla()

    def show(self):
        plt.show()

    def draw_function(self, function, borders, accuracy):
        length = abs(borders["right"] - borders["left"])
        keys = [x for x in np.linspace(borders["left"], borders["right"], accuracy * length)]
        values = [function(x) for x in keys]
        plt.plot(keys, values, label="function", markerfacecolor='blue')

    def manipulate_plot(self, grid: bool = None,
                        yscale: str = None, labels: dict = None):
        if grid:
            plt.grid()

        if yscale:
            plt.yscale(yscale)

        if labels:
            if labels["x"]:
                plt.xlabel(labels["x"])
            if labels["y"]:
                plt.ylabel(labels["y"])
