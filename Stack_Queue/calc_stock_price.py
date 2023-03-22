# 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# answer 2
# enumerate()는 반복 자료형 내 원소를 하나씩 다 봐야하니까 O(n) 인 반면, range()는 O(1)
# answer 1보다 빠름
from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        popped_price = queue.popleft()
        time = 0
        for i in queue:
            time += 1
            if i < popped_price:
                answer.append(time)
                break
        else:
            answer.append(len(queue))
    return answer

# answer 1
# deque 사용
from collections import deque

def solution4(prices):
    queue = deque(prices)
    answer = []
    while queue:
        popped_price = queue.popleft()
        
        for index, i in enumerate(queue):
            if i < popped_price:
                answer.append(index+1)
                break
        else:
            answer.append(len(queue))
    return answer

# sol.3
# correct
def solution3(prices):
    answer = []
    while len(prices) != 0:
        popped_price = prices.pop(0)
        
        for index, i in enumerate(prices):
            if i < popped_price:
                answer.append(index+1)
                break
        else:
            answer.append(len(prices))
    return answer

# sol.2
# correct but time exceed
def solution2(prices):
    answer = []
    while len(prices) != 0:
        popped_price = prices.pop(0)
        print(popped_price)
        if all(popped_price <= price for price in prices):
            print('🔴')
            answer.append(len(prices))
        else:
            print('🔵')
            for index, i in enumerate(prices):
                if i < popped_price:
                    print(i, index)
                    answer.append(index+1)
                    break
    return answer
    
# sol.1
# incorrect
def solution1(prices):
    answer = []
    while len(prices) != 0:
        popped_price = prices.pop(0)
        if any(popped_price < price for price in prices):
            answer.append(len(prices))
        else:
            count = 0
            for index, i in enumerate(prices):
                if i < popped_price:
                    answer.append(index + 1)
    answer.append(0)
    return answer