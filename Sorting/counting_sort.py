# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
# 참고 https://somjang.tistory.com/entry/Mxmxmxm
import sys

N = int(sys.stdin.readline())
d = {}
for i in range(N):
    n = int(sys.stdin.readline())
    if d.get(n):
        d[n] += 1
    else:
        d[n] = 1

for i in range(10001):
    if d.get(i):
        for _ in range(d[i]):
            print(i)


# <><><><><><><><><><><><><><><>< failed for time&memory exceed ><><><><><><><><><><><><><><><>
# 시간 초
def sort_number_vers3():
    N = int(open(0).read())
    num_list = []
    for i in range(N):
        num_list.append(int(open(0).read()))

    num_list.sort()
    print(*num_list, sep='\n')

# 메모리 초과
import sys
N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

count_dict = {}
for num in arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

result = []
for num in range(max(arr) + 1):
    while num in count_dict and count_dict[num] != 0:
        result.append(num)
        count_dict[num] -= 1

print(*result, sep='\n')