from main import calculate

def test_calculate_operations():
    # Testing addition
    assert calculate(4, 3, '+') == 7, "Addition failed"
    # Testing subtraction
    assert calculate(5, 2, '-') == 3, "Subtraction failed"
    # Testing multiplication
    assert calculate(6, 7, '*') == 42, "Multiplication failed"
    # Testing division
    assert calculate(8, 2, '/') == 4, "Division by non-zero failed"
    # Testing division by zero
    assert calculate(5, 0, '/') == None, "Division by zero should return None"
