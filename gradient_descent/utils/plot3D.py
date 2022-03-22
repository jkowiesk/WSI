"""
plot3D.py - simple class for 3d plots
"""
import matplotlib.pyplot as plt
import numpy as np


class Plot3D:
    def __init__(self, x, y, z, borders):
        self.borders = borders
        self.ax = plt.axes(projection='3d')

        self.ax.set_xlim(borders["x"][0], borders["x"][1])
        self.ax.set_ylim(borders["y"][0], borders["y"][1])
        self.ax.set_zlim(borders["z"][0], borders["z"][1])

        self.ax.scatter(x[:-1], y[:-1], z[:-1], color="red", alpha=1)
        self.ax.scatter(x[-1], y[-1], z[-1], color="green", alpha=1)

    def save_to_file(self, file_name):
        plt.savefig(file_name)
        plt.cla()

    def show(self):
        plt.show()

    def draw_function(self, function):
        X = np.array([x for x in range(self.borders["x"][0], self.borders["x"][1])])
        Y = np.array([y for y in range(self.borders["y"][0], self.borders["y"][1])])
        X, Y = np.meshgrid(X, Y)
        Z = np.array([function([x, y]) for x, y in zip(X, Y)])
        self.ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                             cmap='viridis', edgecolor='none')
