# 빠른 A + B
# for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
import sys

def aplusb_versfast():
    time = int(sys.stdin.readline().rstrip())
    result_list = []
    for i in range(time):
        result_list.append(sys.stdin.readline().rstrip())

    for result in result_list:
        print(sum([int(i) for i in result.split(' ')]))


# 구구단
def times_table():
    time = int(input())

    for i in range(1, 10):
        print(f"{time} * {i} = {time*i}")

# A + B - 3
def aplusb_vers3():
    time = int(input())
    result_list = []
    for i in range(time):
        result_list.append(input())

    for result in result_list:
        print(sum([int(i) for i in result.split(' ')]))

# 합
def n_sum():
    n = int(input())
    print(sum(list(range(n + 1))))

# 영수증
def receipt():
    total_cost = int(input())
    total_num = int(input())
    
    result_list = []
    for i in range(total_num):
        result_list.append(input())

    answer = 0
    for result in result_list:
        price, num = [int(i) for i in result.split(' ')]
        answer += price * num

    if answer == total_cost:
        print('Yes')
    else:
        print('No')
        
# 코딩은 체육과목입니다
def coding_is_pe():
    N = int(input())
    print(int(N / 4) * "long " + "int")

def aplusb_vers8():
    time = int(sys.stdin.readline().rstrip())
    result_list = []
    for i in range(time):
        result_list.append(sys.stdin.readline().rstrip())

    for index, result in enumerate(result_list):
        splited_list = [int(i) for i in result.split(' ')]
        print(f"Case #{index + 1}: {splited_list[0]} + {splited_list[1]} = {sum(splited_list)}")

def aplusb_vers5():
    result_list = []
    while not "0 0" in result_list:
        result_list.append(sys.stdin.readline().rstrip())
    result_list.remove("0 0")
    for result in result_list:
        print(sum([int(i) for i in result.split(' ')]))

import sys
def make_star_vers2():
    time = int(sys.stdin.readline().rstrip())

    for i in range(1, time + 1):
        print(' ' * (time - i) + '*' * i)
make_star_vers2()