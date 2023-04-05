# 쉬운 계단 수
def stair_num():
    n = int(input())
    L = [[0] + [1] * 9]
    for i in range(1, n + 1):
        l = []
        for j in range(10):
            if j == 0:
                l.append(L[i - 1][1])
            elif j == 9:
                l.append(L[i - 1][8])
            else:
                l.append(L[i - 1][j - 1] + L[i - 1][j + 1])
        L.append(l)

    print(sum(L[n - 1]) % 1000000000)


# 계단 오르기
def shortest_climbing_stairs():
    import sys
    a = b = c = 0
    n = int(sys.stdin.readline())
    for i in range(n):
        t = int(sys.stdin.readline())
        a, b, c = c, a + t, max(a, b) + t
    print(c)


def climbing_stairs():
    n = int(input())  # 계단 개수
    s = [int(input()) for _ in range(n)]  # 계단 리스트
    dp = [0] * (n)  # dp 리스트
    if len(s) <= 2:  # 계단이 2개 이하일땐 그냥 다 더해서 출력
        print(sum(s))
    else:  # 계단이 3개 이상일 때
        dp[0] = s[0]  # 첫째 계단 수동 계산
        dp[1] = s[0] + s[1]  # 둘째 계단까지 수동 계산
        for i in range(2, n):  # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
            dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
        print(dp[-1])


# goood ! but..
# 3,[10,20,25] => 45가 나와야 하지만 35가 나옴
def climbing_stairs_vers1():
    n, *O = map(int, open(0).read().split())
    dp = [O[0]]
    for i in range(1, n):
        if i % 3 == 0:
            dp.append(dp[-1] + O[i] + max(O[i - 1], O[i - 2]))

    if n <= 2:
        print(sum(O))
    elif n == 3:
        print(max(O[0], O[1]) + O[2])
    else:
        r = (n - 1) % 3
        if r == 0:
            print(dp[-1])
        else:
            print(dp[-1] + O[-1])


# incorrect
def climbing_stairs_vers2():
    n, *O = map(int, open(0).read().split())
    dp = [0]
    for i in range(0, n):
        if (i + 1) % 3 == 0:
            dp.append(dp[-1] + O[i] + max(O[i - 1], O[i - 2]))
    if n % 3 == 0:
        print(dp[-1])
    else:
        print(dp[-1] + O[-1])


# 정수 삼각형
def int_triangle():
    n = int(input())
    O = []
    for i in range(n):
        O.append(list(map(int, input().split())))
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0: O[i][j] += O[i - 1][j]
            elif j == i: O[i][j] += O[i - 1][j - 1]
            else: O[i][j] += max(O[i - 1][j], O[i - 1][j - 1])
    print(max(O[-1]))


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
