# sort() 는 Timsort 라는 정렬 알고리즘 사용.
# Timsort 알고리즘은 O(n) 으로 되는 경우도 있긴 하지만(데이터가 정렬되어 있으면 비교를 하지 않음)
# 평균적으로 nlogn, 최악인 경우에도 nlogn 을 보장

# 수 정렬하기2
import sys


def sort_number_vers2():
    N = int(sys.stdin.readline().rstrip())

    num_list = []
    for i in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))

    num_list.sort()
    print(*num_list, sep='\n')


# 커트라인
def find_cutoff_score():
    N, k = map(int, input().split())
    score_list = list(map(int, input().split()))

    print(sorted(score_list, reverse=True)[k - 1])


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
