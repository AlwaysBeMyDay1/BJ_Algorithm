# 킹, 퀸, 룩, 비숍, 나이트, 폰
def chess():
    found_num_list = [int(i) for i in input().split(' ')]

    piece_num_list = [1,1,2,2,2,8]

    answer = []
    for piece_num, found_num in zip(piece_num_list, found_num_list):
        answer.append(str(int(piece_num - found_num)))

    print(' '.join(answer).strip(' '))

# 별 찍기 - 7
import sys
def print_stars_vers7():
    N = int(sys.stdin.readline().rstrip())

    for i in range(1, 2 * N):
        space_num = abs(N - i)
        star_num = 2*N - 1 - 2*space_num
        print(' ' * space_num + '*' * star_num)
    
# 바구니 순서 바꾸기
import sys
def change_basket_order():
    N, M = [int(i) for i in (sys.stdin.readline().rstrip()).split(' ')]

    N_list = [str(i) for i in range(1, N + 1)]
    order_list = []
    for i in range(1, M + 1):
        order_list.append(sys.stdin.readline().rstrip())

    for order in order_list:
        i, j, k = [int(o)-1 for o in order.split(' ')]
        N_list = N_list[:i] + N_list[k:j+1] + N_list[i:k] + N_list[j+1:]

    print(' '.join(N_list).strip())

change_basket_order()