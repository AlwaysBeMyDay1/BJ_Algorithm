# ATM
def atm():
    n, *l = map(int, open(0).read().split())
    l.sort()
    a = 0
    c = 0
    for i in range(n):
        c += l[i]
        a += c
    print(a)


# 회의실 배정
def allot_room():
    import sys
    input = sys.stdin.readline
    N = int(input())

    L = [[0] * 2 for _ in range(N)]
    for i in range(N):
        s, e = map(int, input().split())
        L[i][0] = s
        L[i][1] = e

    L.sort(key=lambda x: (x[1], x[0]))
    a = 1
    e = L[0][1]
    for i in range(1, N):
        if L[i][0] >= e:
            a += 1
            e = L[i][1]

    print(a)


# 동전 0
def div_coin():
    n, k, *l = map(int, open(0).read().split())

    count = 0
    for i in reversed(range(n)):
        count += k // l[i]  #카운트 값에 K를 동전으로 나눈 몫을 더해줌
        k = k % l[i]  # K는 동전으로 나눈 나머지로 계속 반복

    print(count)
