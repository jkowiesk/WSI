from utils.gray import genetic_to_dec


def test_genetic_to_dec():
    individual = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1,
                  1, 1, 0, 0, 1, 1, 1, 0, 0]
    result = genetic_to_dec(individual)
    assert result == [7, 7, 7, 7]