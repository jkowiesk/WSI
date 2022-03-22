from utils.gradient_descent import gradient_descent


def test_quadratic_function():
    minimum = gradient_descent(lambda x: 2*x, [5], 0.1)
    assert(int(minimum) == 0)


def test_linear_function():
    minimum = gradient_descent(lambda x: 2, [100], 100)
    assert(int(minimum) == -199900)


def test_cubic_function():
    minimum = gradient_descent(lambda x: 4*(x**3), [5], 0.01)
    assert(int(minimum) == 0)
