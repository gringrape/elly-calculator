def test_sum_function():
    from main import sum_function
    assert sum_function(2, 3) == 5
    assert sum_function(0, 0) == 0
    assert sum_function(-5, 5) == 0
    assert sum_function(100, 200) == 300