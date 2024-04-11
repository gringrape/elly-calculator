def calculator():
    num1 = int(input('첫 번째 숫자를 입력해주세요: '))
    num2 = int(input('두 번째 숫자를 입력해주세요: '))
    operation = input('어떤 연산을 하시겠습니까? (+, -, *, /): ')
    if operation == '+':
        result = num1 + num2
        print('두 숫자의 합은:', result)
    elif operation == '-':
        result = num1 - num2
        print('두 숫자의 차는:', result)
    elif operation == '*':
        result = num1 * num2
        print('두 숫자의 곱은:', result)
    elif operation == '/':
        result = num1 / num2
        print('두 숫자의 나눗셈 결과는:', result)
    else:
        print('잘못된 연산자 입력입니다.')

calculator()