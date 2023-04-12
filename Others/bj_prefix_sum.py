# 구간합 구하기 4
# 시간 초과 (시간 복잡도 m * n)
def prefix_sum4_vers2():
    import sys
    input = sys.stdin.readline
     
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for i in range(n):
        a, b = map(int, input().split())
        print(sum(arr[a-1:b]))


def prefix_sum4_vers1():
    import sys
    input = sys.stdin.readline
     
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix_sum = [0]    # init prefix_sum    
     
    temp = 0    
    for i in arr:    # accumulate arr section 
        temp += i
        prefix_sum.append(temp)
     
    for i in range(n):
        a, b = map(int, input().split())
        print(prefix_sum[b] - prefix_sum[a-1])


