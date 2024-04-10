def calculate():
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    operation = input("사칙연산을 선택하세요 (+, -, *, / 중 하나를 입력): ")

    if operation in ['+', '-', '*', '/']:
        result = eval(str(num1) + operation + str(num2))
        print(f"결과: {result}")
    else:
        print("유효한 연산자를 입력하세요.")

calculate()