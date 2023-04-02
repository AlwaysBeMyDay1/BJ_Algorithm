# 프린터 큐
def print_priority():
    from collections import deque
    n=int(input())
    for i in range(n):
        n,m=map(int,input().split())
        q=deque(map(int,input().split()))
        i=0
        while m!=-1:
            e=q.popleft()
            mx=max(q) if q else e
            if e >= mx:
                m-=1
                i+=1
            else:
                q.append(e)
                if m==0:
                    m=len(q)-1
                else:
                    m-=1
        print(i)
            

# 요세푸스 문제 0
def Josephus_vers2():
    from collections import deque
    n, k = map(int, input().split())
    s = deque([])
    for i in range(1, n + 1):
        s.append(i)
    print('<', end='')
    while s:
        for i in range(k - 1):
            s.append(s[0])
            s.popleft()
        print(s.popleft(), end='')
        if s:
            print(', ', end='')
    print('>')

def Josephus_vers1():
    from colle.ctions import deque
    n, k = map(int, input().split())
    q = deque(range(1, n + 1))
    i = 0
    a = []
    while len(q) != 0:
        i += 1
        e = q.popleft()
        if i % k == 0:
            a.append(e)
            i = 0
        else:
            q.append(e)
    print("<", end='')
    print(*a, sep=', ', end='>\n')


# 카드 2
def card2():
    from collections import deque
    n = int(input())
    q = deque(range(1, n + 1))
    while len(q) != 1:
        q.popleft()
        q.append(q.popleft())
    print(q[0])
