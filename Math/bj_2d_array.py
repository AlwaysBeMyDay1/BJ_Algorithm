# 색종이
import sys
input = sys.stdin.readline

paper = [[0]*101 for i in range(101)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] = 1

r = 0
for i in paper:
    r += sum(i)
print(r)

# incorrect
def colored_paper():
    cp = []
    for _ in range(100):
        cp.append([0]*100)
    
    o=[]
    N=int(input())
    for _ in range(N):
        o.append(list(map(int, input().split())))
    
    for x,y in o:
        for i in cp[89-y:99-y]:
            i[x:x+10]=[1]*10
    
    answer=0
    for i in cp:
        answer+=i.count(0)
    
    print(10000-answer)


# 세로읽기
def read_vertical():
    A=[]
    for _ in range(5):
        A.append(list(input()))
    r=''
    while not all(x==[] for x in A):
        for a in A:
            if a != []:
                r+=a.pop(0)
    print(r)

# 최댓값
# correct (max=0 -> max=-1)
def find_max_value():
    A = []
    for row in range(9):
        row = list(map(int, input().split()))
        A.append(row)
    
    g,s,max=0,0,-1
    for y in range(9):
        for x in range(9):
            if A[y][x] > max:
                max = A[y][x]
                g=x+1
                s=y+1
    
    print(max)
    print(s, g)
    
# 이렇게 하면 위치가 안 나옴
def find_max_value_vers1():
    A = []
    for row in range(9):
        row = list(map(int, input().split()))
        A.append(row)
    
    g,s,max=0,0,0
    for y in range(9):
        for x in range(9):
            if A[y][x] > max:
                max = A[y][x]
                g=x+1
                s=y+1
    
    print(max)
    print(s, g)


# 행렬 덧셈
def matrix_sum():
    A, B = [], []
    N, M = map(int, input().split())
    
    for row in range(N):
        row = list(map(int, input().split()))
        A.append(row)
    
    for row in range(N):
        row = list(map(int, input().split()))
        B.append(row)
    
    result = []
    for i in range(N):
        r = []
        for a,b in zip(A[i],B[i]):
            r.append(a+b)
        result.append(r)
    
    for i in result:
        print(*i)