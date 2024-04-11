def add(x, y):
    return x + y

def main():
    print("hello, world")
    a = int(input("첫 번째 수를 입력하세요: "))
    b = int(input("두 번째 수를 입력하세요: "))
    result = add(a, b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()