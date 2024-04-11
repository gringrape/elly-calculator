from main import enhanced_calculator

def test_enhanced_calculator_with_log():
    assert enhanced_calculator(10, 2, 'log') == 1.0, "Should return the base 10 logarithm of 10 / 2"
    assert enhanced_calculator(100, 10, 'log') == 1.0, "Should return the base 10 logarithm of 100 / 10"
    assert enhanced_calculator(2, 2, 'log') == 0.0, "Should return the base 10 logarithm of 2 / 2"