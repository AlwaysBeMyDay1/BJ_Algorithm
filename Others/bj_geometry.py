# 세 막대
def three_sticks():
    o = sorted(map(int, input().split()))
    print(sum(o)) if o[2] < o[0] + o[1] else print(2 * (o[0] + o[1]) - 1)


def three_sticks_vers1():
    a, b, c = sorted(map(int, input().split()))
    print(a + b + min(c, a + b - 1))


# 대지
def get_area_width_vers2():
    n, *l = map(int, open(0).read().split())
    s = lambda i: max(i) - min(i)
    print(s(l[::2]) * s(l[1::2]))


def get_area_width():
    n, *o = map(int, open(0).read().split())
    nx = min(o[::2])
    ny = min(o[1::2])
    xx = max(o[::2])
    xy = max(o[1::2])
    print((xx - nx) * (xy - ny))


# 네 번째 점
def complete_square():
    xl, yl = [], []
    for i in range(3):
        x, y = map(int, input().split())
        if x in xl: xl.remove(x)
        else: xl += [x]
        if y in yl: yl.remove(y)
        else: yl += [y]
    print(xl[0], yl[0])


# 직사각형에서 탈출
def escape_square():
    x, y, w, h = map(int, input().split())
    print(min(w - x, h - y, x, y))
