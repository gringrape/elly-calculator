def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/' and b != 0:
        return a / b
    return None

if __name__ == '__main__':
    # Basic testing
    print(calculate(4, 3, '+'))  # Output should be 7
    print(calculate(5, 2, '-'))  # Output should be 3
    print(calculate(6, 7, '*'))  # Output should be 42
    print(calculate(8, 2, '/'))  # Output should be 4
    print(calculate(5, 0, '/'))  # Output should be None