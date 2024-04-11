from main import add, multiply, divide

def test_add_two_integers():
    assert add(2, 3) == 5, "Expected add(2, 3) to return 5"

def test_add_zero():
    assert add(0, 0) == 0, "Expected add(0, 0) to return 0"

def test_add_negative_numbers():
    assert add(-1, -2) == -3, "Expected add(-1, -2) to return -3"

def test_add_positive_negative():
    assert add(3, -2) == 1, "Expected add(3, -2) to return 1"

def test_multiply_two_integers():
    assert multiply(2, 4) == 8, "Expected multiply(2, 4) to return 8"

def test_multiply_with_zero():
    assert multiply(0, 5) == 0, "Expected multiply(0, 5) to return 0"

def test_multiply_negative_numbers():
    assert multiply(-1, 3) == -3, "Expected multiply(-1, 3) to return -3"

def test_multiply_positive_negative():
    assert multiply(3, -2) == -6, "Expected multiply(3, -2) to return -6"

def test_divide_two_integers():
    assert divide(10, 2) == 5, "Expected divide(10, 2) to return 5"

def test_divide_by_zero():
    try:
        divide(5, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False, "Expected ZeroDivisionError when dividing by zero"

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5, "Expected divide(-10, 2) to return -5"

def test_divide_positive_negative():
    assert divide(10, -2) == -5, "Expected divide(10, -2) to return -5"