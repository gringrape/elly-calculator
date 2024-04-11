def enhanced_calculator(a, b, operation):
    valid_operations = ['+', '-', '*', '/']
    if operation not in valid_operations:
        raise ValueError('지원하지 않는 연산자입니다.')
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError('0으로 나눌 수 없습니다')

if __name__ == '__main__':
    while True:
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        operation = input("연산자를 입력하세요 (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            result = enhanced_calculator(num1, num2, operation)
            print("결과는", result)
            break
        else:
            print("지원하지 않는 연산자입니다. 다시 입력해주세요.")