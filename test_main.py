from main import add


def test_add_two_integers():
    assert add(2, 3) == 5, "Expected add(2, 3) to return 5"

def test_add_zero():
    assert add(0, 0) == 0, "Expected add(0, 0) to return 0"

def test_add_negative_numbers():
    assert add(-1, -2) == -3, "Expected add(-1, -2) to return -3"

def test_add_positive_negative():
    assert add(3, -2) == 1, "Expected add(3, -2) to return 1"
