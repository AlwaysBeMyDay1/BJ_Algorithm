# 가장 긴 바이토닉 부분 수열
def LIS_bitonic():
    n, *L = map(int, open(0).read().split())
    rL = L[::-1]
    dp_i = [1] * n
    dp_d = [1] * n

    for i in range(1, n):
        for j in range(i):
            if L[i] > L[j]:
                dp_i[i] = max(dp_i[i], dp_i[j] + 1)
            if rL[i] > rL[j]:
                dp_d[i] = max(dp_d[i], dp_d[j] + 1)

    result = []
    for i in range(n):
        result.append(dp_i[i] + dp_d[n - i - 1] - 1)

    print(max(result))


# 가장 긴 증가하는 부분 수열
def LIS():
    n, *L = map(int, open(0).read().split())
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if L[i] > L[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
