# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

# sol.3
# use heapq
import heapq

def solution3(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    if scoville[0] >= K:
        return answer
        
    while len(scoville) != 1:
        answer += 1
        
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        made_scoville = min1 + (min2 * 2)
        heapq.heappush(scoville, made_scoville)
        
        if scoville[0] >= K:
            return answer
        else:
            pass
    return -1
    
# sol.2-1
# 80.8(정확성), 0(효율성)
from collections import deque

def solution(scoville_list, K):
    scoville = deque(scoville_list)
    answer = 0
    
    while len(scoville) != 1:
        scoville = deque(sorted(scoville))
        min1 = scoville.popleft()
        if min1 >= K:
            break
        if len(scoville) < 2:
            return -1
        min2 = scoville.popleft()
        made_scoville = min1 + (min2 * 2)
        scoville.append(made_scoville)
        answer += 1
        
    return answer
    
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