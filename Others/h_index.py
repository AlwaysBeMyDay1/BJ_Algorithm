# https://school.programmers.co.kr/learn/courses/30/lessons/42747#fn1
# H-Index

# answer2
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
    
# answer1
# more solid
# 인용 횟수가 아무리 많아도, 그만큼 논문 수가 따라주지 않으면 h-index는 낮음. 즉, 인용횟수가 논문 수를 넘을 수 없으니, index(논문 수)를 return 하면 됨.
def solution2(citations):
  sorted_citations = sorted(citations, reverse=True)
  for i in range(len(sorted_citations)):
    if sorted_citations[i] <= i: 
      return i
  return len(sorted_citations)

# sol.1
# correct
from collections import deque

def solution1(citations):
    citations = deque(citations)
    min_val = min(citations)
    max_val = max(citations)
    dict = {}
    for i in range(min_val, max_val + 1):
        dict[i] = sum(list(map(lambda x: 1 if x >= i else 0, citations)))

    answer = 0
    for index, dict_val in enumerate(dict.items()):
        if dict_val[0] > dict_val[1]:
            if index == 0:
                answer = dict_val[1]
                break
            answer = dict_val[0] - 1
            break
    else:
        answer = dict_val[0]

    return answer