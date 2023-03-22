def solution(priorities, location):
    indexed_list = [[index, priority] for index, priority in enumerate(priorities)]

    answer = 0
    while True:
        p = indexed_list.pop(0)
        if any(p[1] < q[1] for q in queue):
            queue.append(p)
        else:
            answer += 1
            if p[0] == location:
                return answer
            
        
        
    

# sol.1
# priority와 처음 index 모두 고려한다면 이 풀이법이 맞음
def solution1(priorities, location):
    indexed_list = [[index, priority] for index, priority in enumerate(priorities)]

    printing_queue = []
    big = 0
    while len(indexed_list)!=0:
        big = 0
        waiting_queue = []
        for i in range(len(indexed_list)):
            popped_print = indexed_list.pop(0)
            if popped_print[1] > big:
                indexed_list += waiting_queue
                waiting_queue = []
                waiting_queue.append(popped_print)
                big = popped_print[1]
            else:
                waiting_queue.append(popped_print)
                
        printing_queue.append(waiting_queue.pop(0))
        
        indexed_list += waiting_queue

    for index, i in enumerate(printing_queue):
        if i[0] == location:
            return index
        

    
