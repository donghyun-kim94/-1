#!/usr/bin/env python3
"""간단한 사칙연산 계산기 예제"""


def add(x, y):
    """두 수를 더한 값을 반환"""
    return x + y


def subtract(x, y):
    """두 수를 뺀 값을 반환"""
    return x - y


def multiply(x, y):
    """두 수를 곱한 값을 반환"""
    return x * y


def divide(x, y):
    """두 수를 나눈 값을 반환; 0으로는 나눌 수 없음"""
    if y == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return x / y


def main():
    print("간단한 계산기입니다.")
    while True:
        print("1: 더하기, 2: 빼기, 3: 곱하기, 4: 나누기, q: 종료")
        choice = input("선택: ")
        if choice == "q":
            break
        a = float(input("첫 번째 숫자: "))
        b = float(input("두 번째 숫자: "))
        if choice == "1":
            print(f"결과: {add(a, b)}")
        elif choice == "2":
            print(f"결과: {subtract(a, b)}")
        elif choice == "3":
            print(f"결과: {multiply(a, b)}")
        elif choice == "4":
            try:
                print(f"결과: {divide(a, b)}")
            except ValueError as e:
                print("에러:", e)
        else:
            print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
