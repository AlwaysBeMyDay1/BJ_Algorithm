# 골드바흐 파티션
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
def goldbach_conjecture():
    n, *L = map(int, open(0).read().split())

    # 에라토스테네스의 체
    m = max(L)
    pl = [1] * (m + 1)
    pl[0] = pl[1] = 0
    for i in range(2, int(m**0.5) + 1):
        if pl[i]:
            for j in range(2 * i, m + 1, i):
                pl[j] = 0

    for l in L:
        c = 0
        for i in range(2, l // 2 + 1):
            if pl[i] and pl[l - i]:
                c += 1
        print(c)


# 베르트랑 공준
def bertrand_chebyshev_theorem():
    import math

    m = 123456

    array1 = [True for _ in range(2 * m + 1)]
    array1[0], array1[1] = False, False

    for i in range(2, int(math.sqrt(2 * m) + 1)):
        if array1[i]:
            j = 2
            while i * j <= 2 * m:
                array1[i * j] = False
                j += 1

    while True:
        n = int(input())
        if n == 0:
            break

        count = 0

        for i in range(n + 1, 2 * n + 1):
            if array1[i]:
                count += 1
        print(count)

    import math