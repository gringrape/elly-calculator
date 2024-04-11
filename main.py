def sum_function(a, b):
    return a + b

def main():
    a = int(input('첫 번째 숫자를 입력하세요: '))
    b = int(input('두 번째 숫자를 입력하세요: '))
    result = sum_function(a, b)
    print(f'두 숫자의 합은 {result}입니다.')

if __name__ == '__main__':
    main()