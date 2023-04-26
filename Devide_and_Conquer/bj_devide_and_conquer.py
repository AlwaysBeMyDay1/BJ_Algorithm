# 곱셈
def multiple_dnc_vers2():
    a,b,c=map(int,input().split())
    
    def dnc(a,b,c):
        if b==1:
            return a%c
        elif b%2==0:
            return (dnc(a,b//2,c)**2)%c
        else:
            return ((dnc(a,b//2,c)**2)*a)%c
            
    print(dnc(a,b,c))


# RecursionError
def multiple_dnc_vers1():
    a,b,c=map(int,input().split())
    
    def rcrs(a,aa,time,div):
        if time==0:
            print(aa)
            return
        rcrs(a,a*aa%div,time-1,div)
        
    rcrs(a,1,b,c)



# 종이의 개수
def num_of_paper():
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]

    rl = [0, 0, 0]

    def rcrs(x, y, N):
        start = paper[x][y]
        for i in range(x, x + N):
            for j in range(y, y + N):
                if paper[i][j] != start:
                    N //= 3
                    for k in range(3):
                        for l in range(3):
                            rcrs(x + k * N, y + l * N, N)
                    return
        rl[start] += 1

    rcrs(0, 0, N)
    print(rl[-1])
    print(rl[0])
    print(rl[1])
