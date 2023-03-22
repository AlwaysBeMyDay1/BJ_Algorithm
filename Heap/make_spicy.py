# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

# sol.3
# use heapq
def solution3(scoville_list, K):
    scoville = deque(scoville_list)

# sol.2
# 80.8(정확성), 0(효율성)
from collections import deque

def solution2(scoville_list, K):
    scoville = deque(scoville_list)
    answer = 0
    if all(x >= K for x in scoville):
            return answer
        
    while len(scoville) != 1:
        scoville = deque(sorted(scoville))
        answer += 1
        min1 = scoville.popleft()
        min2 = scoville.popleft()
        made_scoville = min1 + (min2 * 2)
        
        scoville.append(made_scoville)
        if all(x >= K for x in scoville):
            return answer
        else:
            pass
    return -1
    
# sol.1
# 61.5(정확성), 0(효율성)
def solution1(scoville, K):
    answer = 0
    while len(scoville) != 1:
        scoville.sort()
        answer += 1
        min1 = scoville.pop(0)
        min2 = scoville.pop(0)
        made_scoville = min1 + (min2 * 2)
        
        scoville.append(made_scoville)
        if all(x >= K for x in scoville):
            return answer
        else:
            pass
    return -1