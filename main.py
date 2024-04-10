def main():
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    operation = input("사칙연산을 선택하세요 (+, -, *, / 중 하나를 입력): ")

    if operation in ['+', '-', '*', '/']:
        result = calculate(num1, num2, operation)
        print_result(num1, num2, operation, result)
    else:
        print("잘못된 연산자입니다.")


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2


def print_result(num1, num2, operation, result):
    print(f"{num1} {operation} {num2} = {result}")

main()