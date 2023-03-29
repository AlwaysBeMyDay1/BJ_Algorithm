# 평균
def final_exam_avg():
    N=int(input())
    score_list=[int(i) for i in input().split()]

    max_score = max(score_list)
    fixed_score_list = list(map(lambda x:x/max_score*100, score_list))
    print(sum(fixed_score_list)/N)

final_exam_avg()

# 바구니 뒤집기
def reverse_basket():
    N,M=map(int,input().split())
    R=list(range(1,N+1))
    for _ in [0]*M:
        i,j=map(int,input().split())
        R[i-1:j] = reversed(R[i-1:j])
    print(*R)


# 나머지
def different_mod():
    R=[]
    for _ in range(10):
        i=int(input())
        R.append(i%42)
    print(len(list(set(R))))

    
# 과제 안 내신 분..?
def check_report():
    R=list(range(1,31))
    for _ in range(28):
        i=int(input())
        R.remove(i)
    print(R[0])
    print(R[1])


# 공 바꾸기
def change_a_ball():
    N,M=map(int,input().split())
    R=list(range(1,N+1))
    for _ in [0]*M:
        i,j=map(int,input().split())
        R[i-1],R[j-1]=R[j-1],R[i-1]
    print(*R)

    
# 공 넣기
def shortest_put_a_ball():
    p,_,*l=map(int,open(0).read().split())
    L=[0]*p
    while l:p,q,r,*l=l;L[p-1:q]=[r]*(q-p+1)
    print(*L)
    
def compact_put_a_ball():
    N,M=map(int,input().split())
    R=[0]*(N+1)
    for _ in [0]*M:
        i,j,k=map(int,input().split())
        R[i:j+1]=[k]*(j-i+1)
    print(*R[1:])

import sys
def put_a_ball():
    N, M = [int(i) for i in (sys.stdin.readline().rstrip()).split(' ')]

    basket_dict = {}
    for i in range(N):
        basket_dict[i + 1] = '0'
        
    order_list = []
    for i in range(M):
        order_list.append((sys.stdin.readline().rstrip()))

    for order in order_list:
        i, j, k = order.split(' ')
        for n_i in range(int(i), int(j) + 1):
            basket_dict[n_i] = k
    
    print(f"{' '.join(basket_dict.values()).strip(' ')}")


# 최댓값
import sys
def find_max_value():
    N_list = []
    for i in range(9):
        N_list.append(int(sys.stdin.readline().rstrip()))
    
    max_value = max(N_list)
    print(f"{max_value}")
    print(f"{N_list.index(max_value) + 1}")


# 최소, 최대
import sys
def min_max():
    N_length = int(sys.stdin.readline().rstrip())
    N_list = [int(i) for i in (sys.stdin.readline().rstrip()).split(' ')]

    print(f"{min(N_list)} {max(N_list)}")


# X보다 작은 수
import sys
def find_smaller():
    N_length, X = [int(i) for i in (sys.stdin.readline().rstrip()).split(' ')]
    N_list = [int(i) for i in (sys.stdin.readline().rstrip()).split(' ')]

    result = []
    smaller_list = list(map(lambda x:str(x) if x<X else 0, N_list))
    smaller_list = [str(x) for x in N_list if x < X]
    while 0 in smaller_list:
        smaller_list.remove(0)
    print(' '.join(smaller_list).strip(' '))


# 개수 세기
import sys
def count_v():
    N_length = int(sys.stdin.readline().rstrip())
    N_list = [int(i) for i in (sys.stdin.readline().rstrip()).split(' ')]
    v = int(sys.stdin.readline().rstrip())

    print(N_list.count(v))