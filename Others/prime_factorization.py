# https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 소인수분해

# sol.1
# correct
import math
def solution(n):
    prime_num_list = []
    for i in range(2, n + 1):
        for x in range(2, int(math.sqrt(i) + 1)):
            if i % x == 0:
                break
        else:
            prime_num_list.append(i)

    answer = []
    for prime_num in prime_num_list:
        if n == 1:
            break
        if n % prime_num == 0:
            answer.append(prime_num)
    return answer

print(solution(420))