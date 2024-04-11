from main import add, multiply

def test_add_two_integers():
    assert add(2, 3) == 5, "Expected add(2, 3) to return 5"

def test_add_zero():
    assert add(0, 0) == 0, "Expected add(0, 0) to return 0"

def test_add_negative_numbers():
    assert add(-1, -2)...btract_two_integers():
    assert subtract(2, 3) == -1, "Expected subtract(2, 3) to return -1"

def test_subtract_with_zero():
    assert subtract(5, 0) == 5, "Expected subtract(5, 0) to return 5"

def test_subtract_negative_numbers():
    assert subtract(-1, 3) == -4, "Expected subtract(-1, 3) to return -4"
