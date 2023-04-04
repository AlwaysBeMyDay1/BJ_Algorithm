# RGB거리
def street_of_rgb():
    n = int(input())
    O = []
    for i in range(n):
        O.append(list(map(int, input().split())))
    for i in range(1, n):
        print(O)
        O[i][0] += min(O[i - 1][1], O[i - 1][2])
        O[i][1] += min(O[i - 1][0], O[i - 1][2])
        O[i][2] += min(O[i - 1][0], O[i - 1][2])
        print(O)
    print(min(O[-1][0], O[-1][1], O[-1][2]))


# 연속합
def continuous_sum():
    n, *O = map(int, open(0).read().split())
    d = [O[0]]
    for o in O[1:]:
        d.append(max(d[-1] + o, o))
    print(max(d))


# 파도반 수열
def padoban():
    n, *O = map(int, open(0).read().split())
    N = max(O)
    L = [0, 1, 1, 1, 2]
    for i in range(4, N):
        L.append(L[i] + L[i - 4])
    for o in O:
        print(L[o])


# 01타일
def tile():
    L = [0, 1, 2]
    n = int(input())
    for i in range(2, n + 1):
        L[i] = (L[i - 1] + L[i - 2]) % 15746
    print(L[n])


# 신나는 함수 실행
def cw():
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)
        if dp[a][b][c]:
            return dp[a][b][c]
        if a < b < c:
            dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return dp[a][b][c]
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(
            a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]

    while True:
        a, b, c = map(int, input().split())
        if a == b == c == -1: break
        ans = w(a, b, c)
        print(f"w({a}, {b}, {c}) = {ans}")


# 알고리즘 수업 - 피보나치 수 1
def compare_recursive_dp_vers2():
    n = int(input())
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    print(a, n - 2)


def compare_recursive_dp_vers1():
    c1 = 0

    def fr(n):
        if n < 3:
            global c1
            c1 += 1
            return 1
        return fr(n - 1) + fr(n - 2)

    def fd(n):
        f = [0, 1, 1]
        c2 = 0
        for i in range(3, n + 1):
            c2 += 1
            f.append(f[i - 1] + f[i - 2])
        return c2, f[n]

    n = int(input())
    fr(n)
    c2, fn = fd(n)
    print(c1, c2, fn)
