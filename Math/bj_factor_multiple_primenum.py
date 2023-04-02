# 최소공배수
# 1. 유클리드 호제법을 사용해 최대공약수 구하기
# 2. 두 수의 곱을 최대공약수로 나누기
import sys


def lcm_vers2():
    T = int(input())

    for i in range(T):
        a, b = map(int, sys.stdin.readline().split())
        aa, bb = a, b

        while a % b != 0:
            a, b = b, a % b

        print(aa * bb // b)


# 시간 초과
def lcm_vers1():
    for i in range(int(input())):
        a, b = map(int, input().split())
        for j in range(max(a, b), a * b + 1):
            if j % a == 0 and j % b == 0:
                print(j)
