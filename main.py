def main():
    print("hello, world")

def add_two_numbers(num1, num2):
    return num1 + num2

def test_add_two_numbers():
    assert add_two_numbers(3, 4) == 7, "두 양수를 더하는 테스트 실패"
    assert add_two_numbers(-5, -6) == -11, "두 음수를 더하는 테스트 실패"
    assert add_two_numbers(-5, 5) == 0, "양수와 음수를 더하는 테스트 실패"
    assert add_two_numbers(0, 0) == 0, "0들을 더하는 테스트 실패"
    assert add_two_numbers(1000, 2000) == 3000, "큰 수를 더하는 테스트 실패"

    print("모든 덧셈 테스트 통과!")

if __name__ == '__main__':
    test_add_two_numbers()