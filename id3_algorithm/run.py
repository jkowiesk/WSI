from utils.id3 import ID3
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from utils.plot import Plot
import numpy as np


def main():
    unique_class_values_len = len(np.unique(load_iris().target))
    X = [[str(elem) for elem in x] for x in load_iris().data]
    y = load_iris().target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    X_test, X_validate, y_test, y_validate = train_test_split(X_test, y_test, test_size=0.5)
    depth = 0
    best_model = dict()
    best_model["value"] = float("-inf")

    while depth <= 4:
        matrix = np.zeros((unique_class_values_len, unique_class_values_len))
        value = 0

        id3 = ID3(depth)
        id3.build_tree(X_train, y_train)
        for x, y in zip(X_validate, y_validate):
            predicted_value = id3.predict(x)
            matrix[y][predicted_value] += 1
        for i in range(unique_class_values_len):
            value += matrix[i][i]
        if value > best_model["value"]:
            best_model["depth"] = depth
            best_model["value"] = value
        plot = Plot(matrix, f"Validate for depth: {depth}")
        plot.manipulate_plot(labels={"x": "predicted classes",
                             "y": "expected classes"})
        plot.show()
        depth += 1

    id3 = ID3(best_model["depth"])
    id3.build_tree(X_train, y_train)
    value = 0
    matrix = np.zeros((unique_class_values_len, unique_class_values_len))

    for x, y in zip(X_test, y_test):
        predicted_value = id3.predict(x)
        matrix[y][predicted_value] += 1
    for i in range(unique_class_values_len):
        value += matrix[i][i]
    plot = Plot(matrix, f"Test for depth: {best_model['depth']}")
    plot.manipulate_plot(labels={"x": "predicted classes",
                                 "y": "expected classes"})
    plot.show()
    print(f"{int(value / len(X_test) * 100)}%")


if __name__ == "__main__":
    main()
