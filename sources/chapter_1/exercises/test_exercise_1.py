from exercise_1 import sum_terms


def test_sum_returns_smallest_term():
    A = "X"
    B = "XY"
    assert A == sum_terms(A, B)


def test_sum_returns_sum_of_terms():
    A = "X"
    B = "ZW"
    assert A + '+' + B == sum_terms(A, B)
