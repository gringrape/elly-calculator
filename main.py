def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def main():
    print("안녕하세요, 세계")
    a = int(input("첫 번째 수를 입력하세요: "))
    b = int(input("두 번째 수를 입력하세요: "))
    op = input("연산자를 입력하세요 (+, *): ")
    if op == '+':
        result = add(a, b)
        print(f"{a} + {b} = {result}")
    elif op == '*':
        result = multiply(a, b)
        print(f"{a} * {b} = {result}")

if __name__ == "__main__":
    main()