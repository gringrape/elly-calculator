from main import calculate_sum, calculate_multiplication

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5, 'Test failed for inputs 2, 3'
    assert calculate_sum(0, 0) == 0, 'Test failed for inputs 0, 0'
    assert calculate_sum(-1, -1) == -2, 'Test failed for inputs -1, -1'
    assert calculate_sum(100, 200) == 300, 'Test failed for inputs 100, 200'

def test_calculate_multiplication():
    assert calculate_multiplication(2, 3) == 6, 'Test failed for inputs 2, 3'
    assert calculate_multiplication(0, 0) == 0, 'Test failed for inputs 0, 0'
    assert calculate_multiplication(-1, -1) == 1, 'Test failed for inputs -1, -1'
    assert calculate_multiplication(100, 200) == 20000, 'Test failed for inputs 100, 200'
