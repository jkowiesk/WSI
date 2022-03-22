from utils.network import Network
from utils.activation_functions import sigmoid, d_sigmoid, ReLu, d_ReLu
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

FIRST_LAYER = 64
LAST_LAYER = 10


def translateX(X, alpha):
    X += alpha


def main():
    hidden_layers = [[50, 40, 30, 20], [50, 30, 30, 30, 20]]
    alphas = [0.5, 0.1]
    sample_sizes = [3, 5]
    X = load_digits().data
    translateX(X, -8)
    y = load_digits().target
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33)
    X_test, X_validate, Y_test, Y_validate = train_test_split(X_test, Y_test, test_size=0.5)
    best_params = {"hidden_layer": None, "alpha": None, "sample_size": None, "counter": -1}
    for hidden_layer in hidden_layers:
        for alpha in alphas:
            for sample_size in sample_sizes:
                counter = 0
                network = Network([FIRST_LAYER, hidden_layer, LAST_LAYER], sigmoid, d_sigmoid, alpha)
                i = 0
                for j in range(sample_size, len(X_train), sample_size):
                    network.learn(X_train[i:j], Y_train[i:j])
                    i = j

                for x_validate, y_validate in zip(X_validate, Y_validate):
                    predicted = network.predict(x_validate)
                    predicted_value = predicted.index(max(predicted))
                    if predicted_value == y_validate:
                        counter += 1

                print(f"Hidden Layer: {hidden_layer}, Alpha: {alpha}, Sample Size: {sample_size}")
                print(counter, len(X_validate))
                print()
                if counter > best_params["counter"]:
                    best_params["hidden_layer"] = hidden_layer
                    best_params["alpha"] = alpha
                    best_params["sample_size"] = sample_size
                    best_params["counter"] = counter
    network = Network([FIRST_LAYER, best_params['hidden_layer'], LAST_LAYER], sigmoid, d_sigmoid, best_params['alpha'])
    i = 0
    for j in range(best_params['sample_size'], len(X_train), best_params['sample_size']):
        network.learn(X_train[i:j], Y_train[i:j])
        i = j
    for x_test, y_test in zip(X_test, Y_test):
        predicted = network.predict(x_test)
        predicted_value = predicted.index(max(predicted))
        if predicted_value == y_test:
            counter += 1
    print()
    print("Best Params:")
    print(f"Hidden Layer: {best_params['hidden_layer']}, Alpha: {best_params['alpha']}, Sample Size: {best_params['sample_size']}")
    print(counter, len(X_test))


if __name__ == "__main__":
    main()
