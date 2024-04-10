def main():
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
operation = input("사칙연산을 선택하세요 (+ 또는 *): ")

if operation == '+':
print(num1 + num2)
elif operation == '*':
print(num1 * num2)

main()