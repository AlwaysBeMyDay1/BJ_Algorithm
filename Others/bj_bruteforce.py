# 수학은 비대면강의입니다
def first_order_equation():
    a, b, c, d, e, f = map(int, input().split())
    x = int((c * e - f * b) / (a * e - b * d))
    y = int((c * d - f * a) / (b * d - a * e))
    print(x, y)


# 분해합
def div_sum():
    n = input()
    m = int(n[0]) - 1
    r = m + (len(n) - 1) * 9
    for i in range(int(n) - r, int(n)):
        rn = sum(map(int, str(i))) + i
        if rn == int(n):
            print(i)
            break
    else:
        print(0)


# 블랙잭
from itertools import combinations


def blackjack():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    # n,m,*l=map(int,open(0).read().split())
    print(
        max(
            map(lambda x: sum(x)
                if sum(x) <= m else 0, list(combinations(l, 3)))))
