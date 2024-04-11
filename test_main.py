from main import calculate_sum, calculate_multiplication, calculate_division

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5, 'Test failed for inputs 2, 3'
    assert calculate_sum(0, 0) == 0, 'Test failed for inputs 0, 0'
    assert calculate_sum(-1, -1)...ate_division(10, 2) == 5, 'Test failed for inputs 10, 2'
    assert calculate_division(20, 5) == 4, 'Test failed for inputs 20, 5'
    assert calculate_division(9, 3) == 3, 'Test failed for inputs 9, 3'
    assert calculate_division(0, 10) == 0, 'Test failed for inputs 0, 10'
