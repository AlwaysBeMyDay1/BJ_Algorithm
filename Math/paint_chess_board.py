# 체스판 다시 칠하기
# without numpy
def paint_chess_board_npx():
    n, m = map(int, input().split())
    l = []
    mini = []
    
    for _ in range(n):
        l.append(input())
    
    for a in range(n - 7):
        for i in range(m - 7):
            idx1 = 0
            idx2 = 0
            for b in range(a, a + 8):
                for j in range(i, i + 8):              # 8X8 범위를 B와 W로 번갈아가면서 검사
                    if (j + b)%2 == 0:
                        if l[b][j] != 'W': idx1 += 1  
                        if l[b][j] != 'B': idx2 += 1
                    else :
                        if l[b][j] != 'B': idx1 += 1
                        if l[b][j] != 'W': idx2 += 1
            mini.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
            mini.append(idx2)                          # B로 시작했을 때 칠해야 할 부분
    
    print(min(mini))

# with numpy
import numpy as np
def paint_chess_board():
    l = open(0).read().split()
    x, y = int(l[0]), int(l[1])
    board = l[2:]
    
    chess_board_w = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    chess_board_b = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
    
    answer_list=[]
    for nx in range(x - 7):
        for ny in range(y - 7):
            new_board = list(map(lambda x:x[ny:ny+8],board[nx:nx+8]))
            cmp_b = 0
            cmp_w = 0
            # new_board와 chess_board 두 가지 비교해서 몇 개 다른 지 체크
            for index, line in enumerate(new_board):
                different_list_b = np.equal(list(line), list(chess_board_b[index]))
                different_list_w = np.equal(list(line), list(chess_board_w[index]))
                cmp_b+=sum([1 for i in different_list_b if i==False])
                cmp_w+=sum([1 for i in different_list_w if i==False])
            answer_list.append(cmp_w)
            answer_list.append(cmp_b)
            
    print(min(answer_list))
paint_chess_board()