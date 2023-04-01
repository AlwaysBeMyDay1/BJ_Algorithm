def cantor(n):
    if n < 1: return '-'
    return cantor(n - 1) + ' ' * 3**(n - 1) + cantor(n - 1)


nl = [int(i) for i in open(0).read().split()]
for n in nl:
    print(cantor(n))
