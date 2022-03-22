"""
plot.py - simple class for 2d plots
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, matrix, plot_label=None):
        self.plot_label = plot_label
        matrix_x = matrix.shape[1]
        matrix_y = matrix.shape[0]
        fig, self._ax = plt.subplots()
        _ = self._ax.imshow(matrix)

        self._ax.set_xticks(np.arange(matrix_y))
        self._ax.set_yticks(np.arange(matrix_x))

        for i in range(matrix_x):
            for j in range(matrix_y):
                text = self._ax.text(j, i, int(matrix[i, j]),
                               ha="center", va="center", color="red")
        self._ax.set_title(plot_label)
        fig.tight_layout()

    def save_to_file(self, file_name):
        plt.savefig(file_name)

    def show(self):
        plt.show()
        self._ax.cla()

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