# 색종이 만들기
# if all(1) -> result_1+=1
# elif all(0) -> result_0+=1
# else -> 해당 종이를 n/2 하기
import sys

ip = sys.stdin.readline()
N = int(ip())
blue = 0
white = 0
board = [list(map(int, ip().split())) for _ in range(N)]


def recursion(x, y, N):
    global white, blue
    color = board[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != board[i][j]:
                recursion(x, y, N // 2)
                recursion(x, y + N // 2, N // 2)
                recursion(x + N // 2, y, N // 2)
                recursion(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


recursion(0, 0, N)
print(white)
print(blue)
