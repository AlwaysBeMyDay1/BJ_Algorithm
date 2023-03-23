# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# k진수에서 소수 개수 구하기

# sol.1
# correct but time exceed with find_prime_num1
# answer with find_prime_num
import math
from collections import deque

def convert_decimal_to_others1(decimal_num, k):
    converted_num = deque([])
    while decimal_num != 0:
        converted_num.appendleft(str(decimal_num % k))
        decimal_num //= k
    return ''.join(converted_num)

# %, // 두 번 하는 대신 divmod 사용 가능
def convert_decimal_to_others(decimal_num, k):
    rev_base = ''
    while decimal_num > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1] 
    
def find_prime_num1(num):
    num_list = str(num).split('0')
    count = 0
    for num in num_list:
        if num != '' and num != '1':
            num = int(num)
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                count += 1
    return count

# 소수를 구할 때 약수 검사는 제곱근 까지만 해봐도 됨.
def find_prime_num(num):
    num_list = str(num).split('0')
    count = 0
    for num in num_list:
        if num != '' and num != '1':
            num = int(num)
            for i in range(2, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    break
            else:
                count += 1
    return count
    
def solution(n, k):
    answer = 0
    if k == 10:
        answer = find_prime_num(n)
    else:
        converted_num = convert_decimal_to_others(n, k)
        print(converted_num)
        answer = find_prime_num(converted_num)
    return answer

