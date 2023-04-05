# https://www.acmicpc.net/problem/1463
# 1로 만들기

# DP - BottomUp(for문 사용)
def to_one_bottomup():
    x=int(input())
    d=[0]*(x+1)
    for i in range(2,x+1):
        d[i]=d[i-1]+1
        if i%2==0:
            d[i]=min(d[i],d[i//2]+1)
        if i%3==0:
            d[i]=min(d[i],d[i//3]+1)
    print(d[x])
    

# DP - TopDown(재귀)
def to_one_topdown():
    x=int(input())
    dp={1:0}
    def rec(n):
        if n in dp.keys():
            return dp[n]
        if (n%3==0) and (n%2==0):
            dp[n]=min(rec(n//3)+1, rec(n//2)+1)
        elif n%3==0:
            dp[n]=min(rec(n//3)+1, rec(n-1)+1)
        elif n%2==0:
            dp[n]=min(rec(n//2)+1, rec(n-1)+1)
        else:
            dp[n]=rec(n-1)+1
        return dp[n]
    print(rec(x))
    

# BFS
def to_one_bfs():
    from collections import deque
    x=int(input())
    Q=deque([x])
    visited=[0]*(x+1)
    while Q:
        c=Q.popleft()
        if c==1:
            break
        if c%3==0 and visited[c//3]==0:
            Q.append(c//3)
            visited[c//3]=visited[c]+1
        if c%2==0 and visited[c//2]==0:
            Q.append(c//2)
            visited[c//2]=visited[c]+1
        if visited[c-1]==0:
            Q.append(c-1)
            visited[c-1]=visited[c]+1
    print(visited[1])


# incorrect
def to_one_vers1():
    x=int(input())
    i=0
    while x!=1:
        i+=1
        if x==2:x-=1
        elif x%3==1 or x%3==2:x-=1
        elif x%3==0:x/=3
        elif x%2==0:x/=2
    print(i)
    