# https://www.acmicpc.net/problem/2447
# 별 찍기 - 10


# 메모리 초과
def R(n):
    if n == 0: return ['*']
    l = []
    pl = R(n - 1)
    for i in range(3):
        if i == 1:
            for ps in pl:
                l.append(f"{ps}{' '*3**(n-1)}{ps}")
        else:
            for ps in pl:
                l.append(ps * 3)
    return l


n = int(input())
print(*R(int(n**(1 / 3))), sep='\n')


# 
def R(n):
    if n == 1: return ['*']
    S = R(n // 3)
    L = []
    for s in S:
        L.append(s * 3)
    for s in S:
        L.append(s + ' ' * (n // 3) + s)
    for s in S:
        L.append(s * 3)
    return L


print('\n'.join(R(int(input()))))