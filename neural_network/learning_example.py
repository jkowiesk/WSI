from utils.network import Network
from utils.activation_functions import sigmoid, d_sigmoid, ReLu, d_ReLu
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from random import shuffle

FIRST_LAYER = 64
LAST_LAYER = 10


def translateX(X, alpha):
    X += alpha


def main():
    num1 = int(input("First number to recognition: "))
    num2 = int(input("Second number to recognition:"))
    X = load_digits().data
    translateX(X, -8)
    y = load_digits().target
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33)
    new_X_train, new_Y_train = [], []
    for x, y in zip(X_train, Y_train):
        if y == num1:
            new_X_train.append(x)
            new_Y_train.append(y)
        if y == num2:
            new_X_train.append(x)
            new_Y_train.append(y)
    X_train, Y_train = new_X_train, new_Y_train
    network = Network([FIRST_LAYER, 50, 40, 30, 20, LAST_LAYER], sigmoid, d_sigmoid)
    i = 0
    for j in range(2, len(X_train), 2):
        network.learn(X_train[i:j], Y_train[i:j])
        i = j

    for x_test, y_test in zip(X_test[:30], Y_test[:30]):
        predicted = network.predict(x_test)
        print(predicted)
        print(predicted.index(max(predicted)), y_test)


if __name__ == "__main__":
    main()
