from main import sum

def test_sum():
    assert sum(3, 4) == 7, "sum(3, 4) should be 7"
    assert sum(-1, 1) == 0, "sum(-1, 1) should be 0"
    assert sum(0, 0) == 0, "sum(0, 0) should be 0"