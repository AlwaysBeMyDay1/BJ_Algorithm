# https://www.acmicpc.net/problem/11729
# 하노이 탑 이동 순서

# sol.1
N = int(input())


def hanoi(plate_num, start, end, other):
    if plate_num == 0:
        return
    else:
        hanoi(plate_num - 1, start, other, end)

        print(start, end)

        hanoi(plate_num - 1, other, end, start)


print(2**N - 1)
hanoi(N, 1, 3, 2)