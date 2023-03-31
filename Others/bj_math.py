# 달팽이는 올라가고 싶다
import math
def time_for_snail():
    n,b,h=map(int,input().split())
    print(math.ceil((h-n)/(n-b))+1)

def time_for_snail_vers1():
    n,b,h=map(int,input().split())
    i=1
    while n<h:
        if i%2==0:
            h-=n
        else:
            h+=b
        i+=1
    
    print(i//2+1)

# 분수찾기
def find_fraction():
    N=int(input())
    i=0
    while N>0:
        i+=1
        N-=i
    if i%2==0:
        t=i+N
        b=i-(i+N-1)
    else:
        t=i-(i+N-1)
        b=i+N
    print(f"{t}/{b}")

    
# 분수찾기
# 지그재그 다르게 함
def find_fraction_vers1():
    N=int(input())
    i=0
    while N>0:
        i+=1
        N-=i
    print(i,N)
    u=i+N
    d=i-u+1
    print(f"{u}/{d}")
    


# 벌집
def honeycomb():
    N=int(input())
    s,e,i=1,7,2
    if N==1:
        print(1)
    else:
        while not s < N <= e:
            s=e
            e=s+6*i
            i+=1
        print(i)
        

# 중앙 이동 알고리즘
def calc_dot_num():
    N=int(input())
    print((2**N+1)**2)


# 세탁소 사장 동혁
# 쿼터(Quarter, $0.25), 다임(Dime, $0.10), 니켈(Nickel, $0.05), 페니(Penny, $0.01)
def calc_change():
    n, *l = map(int, open(0).read().split())
    for m in l:
        print(f"{int(m//25)} {int(m%25//10)} {int(m%25%10//5)} {int(m%25%10%5//1)}")