# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수열

# sol.1
# answer
# test 13,14 -> 360.22ms/457mb, 336.09ms/439mb
from collections import deque

def solution1(n):
    result = deque([0, 1])
    while len(result) != n + 1:
        result.append(result[-1] + result[-2])
    return result[-1] % 1234567

# sol.1-2
# list 사용
# test 13,14 -> 495.67ms/456MB, 474.53ms/439MB
def solution2(num):
    answer=[0,1]
    while len(answer) != num + 1:
        answer.append(answer[-1]+answer[-2])
    return answer[-1] % 1234567


# sol.1-3
# without list or queue
# test 13,14 -> 82.85ms/10.2MB, 79.56ms/10.2MB
def solution(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a % 1234567