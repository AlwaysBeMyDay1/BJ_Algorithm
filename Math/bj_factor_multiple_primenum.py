# 베르트랑 공준
def bertrand_chebyshev_theorem():
    import math
    
    m = 123456
    
    array1 = [True for _ in range(2 * m + 1)]
    array1[0], array1[1] = False, False
    
    for i in range(2, int(math.sqrt(2 * m) + 1)):
        if array1[i]:
            j = 2
            while i * j <= 2 * m:
                array1[i * j] = False
                j += 1
    
    while True:
        n = int(input())
        if n == 0:
            break
    
        count = 0
    
        for i in range(n+1, 2 * n + 1):
            if array1[i]: 
                count += 1
        print(count) 
        
    import math


# more compact
def find_prime_between_us_vers2():
    x, y = map(int, input().split())

    for i in range(x, y + 1):
        if i == 1:
            continue
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)


# correct
def find_prime_between_us():
    import math

    def is_prime(a):
        if a == 0 or a == 1:
            return False
        for j in range(2, int(math.sqrt(a)) + 1):
            if a % j == 0:
                return False
        else:
            return True

    m, n = map(int, input().split())
    al = []
    for a in range(m, n + 1):
        if is_prime(a):
            al += [a]
    print(*al, sep='\n')


# 다음 소수
# correct
def find_next_primenum_vers2():
    import math
    n, *L = map(int, open(0).read().split())
    for i in range(n):
        a = L[i]

        while True:
            for j in range(2, int(math.sqrt(a)) + 1):
                if a % j == 0: break
            else: break
            a += 1
        print(a)


# incorrect
def find_next_primenum():
    import math
    n, *L = map(int, open(0).read().split())
    for i in range(n):
        a = L[i]
        while True:
            for j in range(2, int(math.sqrt(a)) + 1):
                if a % j == 0:
                    break
            else:
                break
            a += 1
        print(a)


# 가로수
def plant_street_trees():
    import math

    n, *L = map(int, open(0).read().split())
    sl = []
    gcd = 0
    for i in range(n - 1):
        sub = L[i + 1] - L[i]
        sl.append(sub)
        if i == 0:
            gcd = sub
        else:
            gcd = math.gcd(gcd, sub)
    print(sum([s // gcd - 1 for s in sl]))


# 분수 합
def sum_of_fraction():

    def gcd(x, y):  #최대공약수, 유클리드 호제
        mod = x % y
        while mod > 0:
            x = y
            y = mod
            mod = x % y
        return y

    A, B = map(int, input().split())
    C, D = map(int, input().split())
    N = gcd(A * D + C * B, B * D)
    print((A * D + C * B) // N, B * D // N)


# 최소공배수
# 1. 유클리드 호제법을 사용해 최대공약수 구하기
# 2. 두 수의 곱을 최대공약수로 나누기
import sys


def lcm_vers2():
    T = int(input())

    for i in range(T):
        a, b = map(int, sys.stdin.readline().split())
        aa, bb = a, b

        while a % b != 0:
            a, b = b, a % b

        print(aa * bb // b)


# 시간 초과
def lcm_vers1():
    for i in range(int(input())):
        a, b = map(int, input().split())
        for j in range(max(a, b), a * b + 1):
            if j % a == 0 and j % b == 0:
                print(j)
