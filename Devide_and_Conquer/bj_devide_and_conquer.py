# 종이의 개수
def num_of_paper():
    N=int(input())
    paper=[list(map(int,input().split())) for _ in range(N)]
    
    rl=[0,0,0]
    def rcrs(x,y,N):
        start=paper[x][y]
        for i in range(x,x+N):
            for j in range(y,y+N):
                if paper[i][j] != start:
                    N//=3
                    for k in range(3):
                        for l in range(3):
                            rcrs(x+k*N,y+l*N,N)
                    return
        rl[start]+=1
    
    rcrs(0,0,N)
    print(rl[-1])
    print(rl[0])
    print(rl[1])