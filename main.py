def enhanced_calculator(a, b, operation):
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
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    operation = input("연산자를 입력하세요 (+, -, *, /): ")
    result = enhanced_calculator(num1, num2, operation)
    print("결과는", result)