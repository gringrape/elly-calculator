def calculate_sum(num1, num2):
    return num1 + num2

def main():
    num1 = int(input('첫 번째 숫자를 입력하세요: '))
    num2 = int(input('두 번째 숫자를 입력하세요: '))
    result = calculate_sum(num1, num2)
    print(f'{num1}와 {num2}의 합은 {result}입니다.')

if __name__ == '__main__':
    main()