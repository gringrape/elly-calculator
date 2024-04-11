def calculate_sum(a, b):
    return a + b

def calculate_multiplication(a, b):
    return a * b

def main():
    try:
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        result_sum = calculate_sum(num1, num2)
        result_multiplication = calculate_multiplication(num1, num2)
        print(f"두 숫자의 합: {result_sum}")
        print(f"두 숫자의 곱: {result_multiplication}")
    except ValueError:
        print("숫자만 입력해주세요.")

if __name__ == "__main__":
    main()