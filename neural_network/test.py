from utils.network import Network
from utils.activation_functions import sigmoid, d_sigmoid, ReLu, d_ReLu
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

FIRST_LAYER = 64
LAST_LAYER = 10


def translateX(X, alpha):
    X += alpha


def main():
    X = load_digits().data
    translateX(X, -8)
    y = load_digits().target
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33)
    # X_test, X_validate, y_test, y_validate = train_test_split(X_test, y_test, test_size=0.5)
    network = Network([FIRST_LAYER, 50, 40, 30, 20, LAST_LAYER], sigmoid, d_sigmoid)
    y_list = [1 if x == Y_test[0] else 0 for x in range(LAST_LAYER)]
    i = 0
    for j in range(10, len(X_train), 10):
        network.learn(X_train[i:j], Y_train[i:j])
        i = j
        if i % 10 == 0:
            cost = network.calculate_cost(X_test[0], y_list)
            test = network.predict(X_test[0])
            print(cost)
            print(test)

    for x_test, y_test in zip(X_test[:20], Y_test[:20]):
        predicted = network.predict(x_test)
        print(predicted)
        print(predicted.index(max(predicted)), y_test)


if __name__ == "__main__":
    main()
