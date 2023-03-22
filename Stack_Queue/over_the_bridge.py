# sol.1st
# correct
def solution(bridge_length, weight, waiting_trucks):
    num_of_trucks = len(waiting_trucks)
    time = 0
    time_limit = 0
    on_bridge_queue = []
    over_bridge_queue = []
    while len(over_bridge_queue) != num_of_trucks:
        time += 1
        time_limit += 1

        if waiting_trucks != [] and sum(on_bridge_queue) + waiting_trucks[0] <= weight and len(on_bridge_queue) <= bridge_length:
            popped_truck = waiting_trucks.pop(0)
            on_bridge_queue.append(popped_truck)
        else:
            on_bridge_queue.append(0)
        
        if time_limit == bridge_length:
            time_limit -= 1
            popped_on = on_bridge_queue.pop(0)
            if popped_on != 0:
                over_bridge_queue.append(popped_on)
        
    return time+1