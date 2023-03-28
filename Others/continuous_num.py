# 연속된 수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/120923


def solution(num, total):
    for i in range(int(total / num) - num, int(total / num)):
        int_list = list(range(i, i + num))
        sum_int = sum(int_list)
        if sum_int == total:
            return int_list


print(solution(3, 12))