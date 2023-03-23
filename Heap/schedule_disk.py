# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

# sol.1
# correct
from collections import deque

def solution(jobs):
    jobs = deque(jobs)
    
    answer = 0
    time, on_work_time = 0, 0
    for i in jobs:
        if i[0] <= time:
            popped_job = jobs.popleft()
    return answer