def calculate_sum(a, b):
    return a + b

def calculate_multiplication(a, b):
    return a * b

def calculate_subtraction(a, b):
    return a - b

def calculate_division(a, b):
    if b == 0:
        return None  # Avoid division by zero
    return a / b

def main():
    try:
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        result_sum = calculate_sum(num1, num2)
        result_multiplication = calculate_multiplication(num1, num2)
        result_subtraction = calculate_subtraction(num1, num2)
        result_division = calculate_division(num1, num2)
        print(f"두 숫자의 합: {result_sum}")
        print(f"두 숫자의 곱: {result_multiplication}")
        print(f"두 숫자의 차: {result_subtraction}")
        if result_division is not None:
            print(f"두 숫자의 나눗셈: {result_division}")
        else:
            print("0으로 나눌 수 없습니다.")
    except ValueError:
        print("숫자만 입력해주세요.")

if __name__ == "__main__":
    main()