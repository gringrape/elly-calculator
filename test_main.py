request : from main import calculate_sum, calculate_multiplication

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5, 'Test failed for inputs 2, 3'
    assert calculate_sum(0, 0) == 0, 'Test failed for inputs 0, 0'
    assert calculate_sum(-1, -1) == -2, 'Test failed for inputs -1, -1'
    assert calculate_sum(100, 200) == 300, 'Test failed for inputs 100, 200'

def test_calculate_multiplication():
    assert calculate_multiplication(2, 3) == 6, 'Test failed for inputs 2, 3'
    assert calculate_multiplication(0, 0) == 0, 'Test failed for inputs 0, 0'
    assert calculate_multiplication(-1, ... 1, 'Test failed for inputs -1, -1'
    assert calculate_multiplication(100, 200) == 20000, 'Test failed for inputs 100, 200'
previous_test_code : 
def test_arithmetic_operations():
    assert add(1, 1) == 2, 'Test failed for adding 1 + 1'
    assert subtract(2, 1) == 1, 'Test failed for subtracting 2 - 1'
    assert multiply(3, 4) == 12, 'Test failed for multiplying 3 * 4'
    assert divide(10, 2) == 5, 'Test failed for dividing 10 / 2'
