# 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# sol.3
# correct
# list 순회 도중 remove 하게 되면 이미 지나간 index를 채우는 방식으로 코드가 진행되어 건너뛰는 원소가 생김. 즉, 새로운 list 생성해야함
def solution(n, lost, reserve):
    common = set(lost).intersection(reserve)
    for i in common:
        lost.remove(i)
        reserve.remove(i)

    new_lost = sorted(lost)
    reserve.sort()
    for i in new_lost:
        if i - 1 in reserve:
            lost.remove(i)
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            lost.remove(i)
            reserve.remove(i + 1)
    return n - len(lost)
    
# sol.2
# correct
# sol.1이 정답이기 위해서는 sorting 되어 있다는 전제조건이 있다.
def solution2(n, lost, reserve):
    common = set(lost).intersection(reserve)
    for i in common:
        lost.remove(i)
        reserve.remove(i)

    lost.sort()
    reserve.sort()
    for i in lost:
        if i - 1 in reserve:
            lost.remove(i)
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            lost.remove(i)
            reserve.remove(i + 1)
    return n - len(lost)

# sol.1
# incorrect
def solution1(n, lost, reserve):
    common = set(lost).intersection(reserve)
    for i in common:
        lost.remove(i)
        reserve.remove(i)

    for i in lost:
        if i - 1 in reserve:
            lost.remove(i)
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            lost.remove(i)
            reserve.remove(i + 1)

    return n - len(lost)
