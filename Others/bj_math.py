import sys


# 10진수 -> n진수
def convert_10_to_n():
    system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    N, B = map(int, sys.stdin.readline().split())
    answer = str()
    while N != 0:
        answer += system[N % B]
        N //= B
    print(answer[::-1])


# n진수 -> 10진수
def convert_n_to_10():
    n, b = input().split()
    print(int(n, int(b)))
