def recursion(s, l, r, c):
    c += 1
    if l >= r:
        return 1, c
    elif s[l] != s[r]:
        return 0, c
    else:
        return recursion(s, l + 1, r - 1, c)


n, *o = open(0).read().split()
for i in o:
    print(*recursion(i, 0, len(i) - 1, 0))
