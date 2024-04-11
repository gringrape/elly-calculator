# Existing Test Code from the repository

# Function to test: 'calculate_sum'
# Specifications: This function should take two integers and return their sum.
def test_calculate_sum():
    assert calculate_sum(1, 2) == 3, "Test for sum of 1 and 2 should return 3"
    assert calculate_sum(-1, 1) == 0, "Test for sum of -1 and 1 should return 0"
    assert calculate_sum(0, 0) == 0, "Test for sum of 0 and 0 should return 0"

# Function to test: 'multiply_numbers'
# Specifications: This function should take two integers and return their product.
def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12, "Test for multiplication of 3 and 4 should return 12"
    assert multiply_numbers(-1, -1) == 1, "Test for multiplication of -1 and -1 should return 1"
    assert multiply_numbers(0, 5) == 0, "Test for multiplication of 0 and 5 should return 0"

# New tests required for a function named 'divide_numbers'
# Specification: This function should take two integers. It should return their division result. It should handle division by zero by returning 'None'.
# Write the new test code

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5, "Test for division of 10 by 2 should return 5"
    assert divide_numbers(5, 0) is None, "Test for division by zero should return None"
