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

# New test functions based on input request "사칙연산을완성해줘." (Complete the four arithmetic operations).
def test_calculate_subtraction():
    assert calculate_subtraction(2, 3) == -1, 'Test failed for inputs 2, 3'
    assert calculate_subtraction(0, 0) == 0, 'Test failed for inputs 0, 0'
    assert calculate_subtraction(5, 1) == 4, 'Test failed for inputs 5, 1'
    assert calculate_subtraction(-1, 1) == -2, 'Test failed for inputs -1, 1'

def test_calculate_division():
    assert calculate_division(6, 3) == 2.0, 'Test failed for inputs 6, 3'
    assert calculate_division(10, 0) == 'undefined', 'Test failed for division by zero'
    assert calculate_division(0, 5) == 0.0, 'Test failed for inputs 0, 5'
    assert calculate_division(-16, -4) == 4.0, 'Test failed for inputs -16, -4'