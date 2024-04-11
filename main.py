def sum(a, b):
    return a + b


def main():
    first_number = int(input("첫 번째 숫자를 입력하세요: "))
    second_number = int(input("두 번째 숫자를 입력하세요: "))
    result = sum(first_number, second_number)
    print(f"두 숫자의 합은 {result}입니다.")

if __name__ == "__main__":
    main()