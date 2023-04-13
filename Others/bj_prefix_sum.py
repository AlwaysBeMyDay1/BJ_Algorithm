# 구간합 구하기 5
def prefix_sum5():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arr[
                i - 1][j - 1]

    for k in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 -
                                                                           1]
        print(result)


def failed_prefix_sum5():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    arr = []
    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)

    dp = []
    for i in range(n):
        k = 0
        dp_e = []
        for j in range(n):
            k += arr[i][j]
            dp_e.append(k)
        dp.append(dp_e)

    print(dp)
    for k in range(m):
        x1, y1, x2, y2 = map(int, input().split())

        result = 0
        for x in range(x1 - 1, x2):
            result += (dp[x][y2 - 1] - dp[x][y1 - 2])
            print(result)
        print(result)


# 나머지 합
def sum_of_mod():
    n, m, *l = map(int, open(0).read().split())
    a = 0
    dp = [0] * m
    for i in range(n):
        a += l[i]
        dp[a % m] += 1
    result = dp[0]
    for i in dp:
        result += i * (i - 1) // 2
    print(result)


# memory exceed
def sum_of_mod_vers2():
    n, m, *l = map(int, open(0).read().split())
    dp = []
    for idx, i in enumerate(l):
        dp.append(i)
        for j in range(1, idx + 1):
            dp.append(dp[-1] + l[idx - j])

    print(sum(r % m == 0 for r in dp))


# time exceed
def sum_of_mod_vers1():
    n, m, *l = map(int, open(0).read().split())
    dp = []
    for idx, i in enumerate(l):
        for j in range(idx + 1):
            dp.append(sum(l[j:idx + 1]))
    print(sum(r % m == 0 for r in dp))


# 인간-컴퓨터 상호작용
def hnc_interaction_vers2():
    S, _, *qs = open(0)
    dp = [[0] * 26]
    for s in S[:-1]:
        dp.append(dp[-1][:])
        dp[-1][ord(s) - 97] += 1
    for q in qs:
        c, a, b = q.split()
        a, b = int(a), int(b)
        c = ord(c)
        print(dp[b + 1][c - 97] - dp[a][c - 97])


# task 2 time exceed?
def hnc_interaction_vers1():
    import sys
    input = sys.stdin.readline

    str = input().rstrip()
    q = int(input())
    dict = {}
    for idx, s in enumerate(str):
        if dict.get(s):
            dict[s].append(idx)
        else:
            dict[s] = [idx]

    for i in range(q):
        a, start, end = input().split()
        start = int(start)
        end = int(end)
        if dict.get(a):
            print(sum(start <= j <= end for j in dict[a]))
        else:
            print(0)


# 수열
def matrix():
    n, k, *l = map(int, open(0).read().split())
    ps = [sum(l[:k])]
    for i in range(n - k):
        ps.append(ps[i] - l[i] + l[i + k])
    print(max(ps))


# 구간합 구하기 4
# 시간 초과 (시간 복잡도 m * n)
def prefix_sum4_vers2():
    import sys
    input = sys.stdin.readline

    m, n = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(n):
        a, b = map(int, input().split())
        print(sum(arr[a - 1:b]))


def prefix_sum4_vers1():
    import sys
    input = sys.stdin.readline

    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix_sum = [0]  # init prefix_sum

    temp = 0
    for i in arr:  # accumulate arr section
        temp += i
        prefix_sum.append(temp)

    for i in range(n):
        a, b = map(int, input().split())
        print(prefix_sum[b] - prefix_sum[a - 1])
