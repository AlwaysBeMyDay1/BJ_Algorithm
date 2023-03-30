# 좌표 압축
# https://www.acmicpc.net/problem/18870
def compress_coordinate():
    n, *l = map(int, open(0).read().split())
    sl = sorted(list(set(l)))
    dic = {sl[i]: i for i in range(len(sl))}
    for o in l:
        print(dic[o], end=' ')


# 시간 초과
def compress_coordinate_vers1():
    n, *l = map(int, open(0).read().split())
    sl = sorted(list(set(l)))

    al = []
    for o in l:
        al.append(sl.index(o))
    print(*al)
