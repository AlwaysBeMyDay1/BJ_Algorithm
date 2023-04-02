# https://www.acmicpc.net/problem/5430
# AC
# correct
# R을 할 시에는 배열을 reverse 해준다. 하지만 n번의 연산이 필요하다. R의 최대 횟수 100,000 , 배열의 최대 크기 100 , 테스트케이스 100개
# 즉, 100 100,000 100 = 1,000,000,000 1억번의 시간이 대략 소요가 된다. 시간초과가 날수도 있기때문에 R을 짝수번 했을경우에는 배열을 reverse시키지 않아도 괜찮다.
# 그래서 R이 나오면 카운트만 해주고, D가 나왔을때 R이 짝수일경우에는 popleft, 홀수일경우에는 pop을 한 후, 마지막에 R이 홀수일 경우에 배열을 reverse해서 출력해주면 된다.

def AC_vers3():
    from collections import deque
    
    T, *L = open(0).read().split()
    for i in range(1, int(T) + 1):
        P, n, A = L[3 * i - 3:3 * i]
        if n == '0':
            A = deque([])
        else:
            A = deque(A.strip('[]').split(','))
        P = P.replace('RR', '')
        R = 0
        for p in P:
            if p == 'R':
                R+=1
            elif p == 'D':
                if len(A) == 0:
                    print('error')
                    break
                else:
                    if R%2==0:
                        A.popleft()
                    else:
                        A.pop()
        else:
            if R%2==0:
                print('['+','.join(A)+']')
            else:
                A.reverse()
                print('['+','.join(A)+']')


# R이 두 번 연속이면 안 뒤집는 것과 마찬가지
# 그래서 replace('RR','') 해줬지만
# time exceed,,
def AC_vers2():
    from collections import deque
    
    T, *L = open(0).read().split()
    for i in range(1, int(T) + 1):
        P, n, A = L[3 * i - 3:3 * i]
        if n == '0':
            A = deque([])
        else:
            A = deque(A.strip('[]').split(','))
        P = P.replace('RR', '')
        for p in P:
            if p == 'R':
                A.reverse()
            elif p == 'D':
                if len(A) == 0:
                    print('error')
                    break
                else:
                    A.popleft()
        else:
            print('[', end='')
            print(*A, sep=',', end=']\n')


# time exceed
def AC_vers1():
    from collections import deque

    T, *L = open(0).read().split()
    for i in range(1, int(T) + 1):
        P, n, A = L[3 * i - 3:3 * i]
        if n == 0:
            A = deque([])
        else:
            A = deque(A.strip('[]').split(','))
        for p in P:
            if p == 'R':
                A.reverse()
            elif p == 'D':
                if len(A) == 0:
                    print('error')
                    break
                else:
                    A.popleft()
        else:
            print('[', end='')
            print(*A, sep=',', end=']\n')
