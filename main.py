def add_two_numbers(a, b):
    return a + b

def main():
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    result = add_two_numbers(num1, num2)
    print("두 숫자의 합은", result)

if __name__ == "__main__":
    main()