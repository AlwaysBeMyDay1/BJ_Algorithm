# 수 정렬하기2
import sys
def sort_number_vers2():
    N = int(sys.stdin.readline().rstrip())

    num_list = []
    for i in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))

    num_list.sort()
    print(*num_list, sep='\n')
sort_number_vers2()

# 커트라인
def find_cutoff_score():
    N,k=map(int,input().split())
    score_list = list(map(int,input().split()))
    
    print(sorted(score_list, reverse=True)[k-1])

# 대표값2
import sys
def find_representative_value():
    num_list = []
    for i in range(5):
        num_list.append(int(sys.stdin.readline().rstrip()))

    num_list.sort()
    print(f"{int(sum(num_list) / len(num_list))}\n{num_list[2]}")

    
# 수 정렬하기
import sys
def sort_number():
    N = int(sys.stdin.readline().rstrip())

    num_list = []
    for i in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))

    num_list.sort()
    print(*num_list, sep='\n')