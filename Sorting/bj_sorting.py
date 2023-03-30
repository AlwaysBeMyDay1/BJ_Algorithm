# 나이순 정렬
# correct
import sys


def sort_with_age():
    d = {}
    for _ in range(int(input())):
        n = sys.stdin.readline().split()
        age = int(n[0])
        if d.get(age):
            d[age].append(n[1])
        else:
            d[age] = [n[1]]

    for a in range(1, 201):
        if d.get(a):
            for name in d[a]:
                print(f'{a} {name}')


# time exceed
def sort_with_age_vers1():
    l = []
    for _ in range(int(sys.stdin.readline())):
        l.append(sys.stdin.readline().rstrip().split())
    sl = sorted(l, key=lambda x: (x[0], l.index(x)))
    for i in sl:
        print(*i)


# 단어 정렬
def sort_words():
    answer_list = []
    for _ in range(int(input())):
        answer_list.append(input())
    sorted_list = sorted(list(set(answer_list)), key=lambda x: (len(x), x))
    print(*sorted_list, sep='\n')


# 좌표 정렬하기
def sort_coordinates():
    n = int(input())
    answer_list = []
    for _ in range(n):
        answer_list.append([int(i) for i in input().split()])
    sorted_list = sorted(answer_list, key=lambda x: (x[0], x[1]))
    for i in sorted_list:
        print(*i)


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
