# Examine the Functionality of a Basic Calculator

def add_two_numbers(num1, num2):
    return num1 + num2

def test_add_two_numbers():
    # Test adding positive numbers
    assert add_two_numbers(3, 4) == 7, "Test for adding two positive numbers failed"
    # Test adding negative numbers
    assert add_two_numbers(-5, -6) == -11, "Test for adding two negative numbers failed"
    # Test adding positive and negative number
    assert add_two_numbers(-5, 5) == 0, "Test for a mixed pair failed"
    # Test adding zero
    assert add_two_numbers(0, 0) == 0, "Test for adding zeros failed"
    # Test adding large numbers
    assert add_two_numbers(1000, 2000) == 3000, "Test for adding large numbers failed"

    print("All tests for add_two_numbers passed!")

if __name__ == '__main__':
    test_add_two_numbers()
