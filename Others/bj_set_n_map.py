# 서로 다른 부분 문자열의 개수
def find_different_string_set():
    s=input()
    l=len(s)
    a=set()
    for i in range(1,l+1):
        for j in range(l):
            a.add(s[j:j+i])
    print(len(a))



# 대칭 차집합
# 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다
def set_sub():
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    print(len(a-b)+len(b-a))


# 듣보잡
def who_that_shit():
    n,q,*o = open(0).read().split()
    n=int(n)
    a=sorted(set(o[:n])&set(o[n:]))
    print(len(a))
    print(*a,sep='\n')

# 숫자 카드 2
def find_numcard():
    n, nl, m, ml = open(0)
    d = {}
    for en in nl.split():
        if d.get(en):d[en]+=1
        else:d[en]=1
    for em in ml.split():
        try:
            print(d[em],end=' ')
        except:
            print(0,end=' ')


# 나는야 포켓몬 마스터 이다솜
def search_poketmon():
    n,q,*o = open(0).read().split()
    d={}
    n=int(n)
    for i in range(1,n+1):
        d[o[i-1]]=i
    for l in o[n:]:
        try:print(d[l])
        except:print(o[int(l)-1])
    

# 회사에 있는 사람
# used set()
def fastest_find():
    s = set()
    _, *l = open(0)
    for c in l:
        n, a = c.split()
        if a < 'l': s |= {n}
        else: s -= {n}
    print(*sorted(s)[::-1], sep='\n')


# correct with dict
import sys


def find_employee_vers2():
    n = int(sys.stdin.readline())
    d = {}
    for _ in range(n):
        nm, log = sys.stdin.readline().split()
        if log == 'enter':
            d[nm] = 1
        else:
            d.pop(nm)

    print(*sorted(d.keys(), reverse=True), sep='\n')


# SystemError
def find_employee_vers1():
    n, *o = open(0).read().split('\n')
    dict = {}
    for a in o:
        nm, log = a.split()
        if log == 'enter':
            dict[nm] = 1
        else:
            dict.pop(nm)

    print(*sorted(dict.keys(), reverse=True), sep='\n')


# 문자열 집합
def set_string():
    n, m, *o = open(0).read().split()
    n = int(n)
    s = set(o[:n])
    print(sum(w in s for w in o[n:]))


def set_string_vers1():
    l = open(0).read().split()
    n, m = int(l[0]), int(l[1])
    a = 0
    for i in l[2 + n:]:
        if i in set(l[2:2 + n]):
            a += 1
    print(a)


# 숫자 카드
def find_card():
    n, nl, m, ml = open(0)
    d = {}
    for en in nl.split():
        d[en] = 1

    for em in ml.split():
        try:
            print(d[em], end=' ')
        except:
            print(0, end=' ')


# correct
def in_list():
    p, q, r, s = open(0)
    d = {*q.split()}
    print(*[+(i in d) for i in s.split()])


# time exceed
def is_in_list():
    n, nl, m, ml = open(0)
    print(*[1 if em in nl.split() else 0 for em in ml.split()])


# time exceed
def is_in_list():
    n, nl, m, ml = open(0)
    print(*list(map(lambda x: 1 if x in nl.split() else 0, ml.split())))


# time exceed
def is_in_list():
    n = int(input())
    nl = [int(i) for i in input().split()]
    m = int(input())
    ml = [int(i) for i in input().split()]

    print(*list(map(lambda x: 1 if x in nl else 0, ml)))
