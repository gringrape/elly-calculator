def enhanced_calculator(a, b, operation):
    import math
    valid_operations = ['+', '-', '*', '/', 'log']
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
    elif operation == 'log':
        if b > 1 and a > 0:
            return math.log(a, b)
        else:
            raise ValueError('로그 연산 오류: 올바른 베이스(>1)와 양의 값이 필요합니다.')

if __name__ == '__main__':
    while True:
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        operation = input("연산자를 입력하세요 (+, -, *, /, log): ")
        if operation in ['+', '-', '*', '/', 'log']:
            result = enhanced_calculator(num1, num2, operation)
            print("결과는", result)
            break
        else:
            print("지원하지 않는 연산자입니다. 다시 입력해주세요.")