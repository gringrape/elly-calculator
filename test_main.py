from main import add, multiply

def test_add_two_integers():
    assert add(2, 3) == 5, "Expected add(2, 3) to return 5"

def test_add_zero():
    assert add(0, 0) == 0, "Expected add(0, 0) to return 0"

def test_add_negative_numbers():
    assert add(-1, -...}) == -6, "Expected multiply(3, -2) to return -6"

def test_subtract_two_integers():
    assert subtract(5, 3) == 2

def test_divide_two_integers():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(10, 0) == 'undefined'