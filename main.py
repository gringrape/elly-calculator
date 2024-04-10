def calculator():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    operation = input('Choose an arithmetic operation (+, -, *, /): ')

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    if operation in operations:
        result = operations[operation](num1, num2)
        print('Result: ', result)
    else:
        print('Invalid operation')


calculator()