from main import calculate_sum

def test_calculate_sum():
    assert calculate_sum(3, 2) == 5, 'Expected sum of 3 and 2 to be 5'
    assert calculate_sum(-1, 1) == 0, 'Expected sum of -1 and 1 to be 0'
    assert calculate_sum(0, 0) == 0, 'Expected sum of 0 and 0 to be 0'
    assert calculate_sum(-5, 6) == 1, 'Expected sum of -5 and 6 to be 1'
    assert calculate_sum(100, 200) == 300, 'Expected sum of 100 and 200 to be 300'