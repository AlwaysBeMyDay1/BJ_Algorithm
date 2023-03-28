# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 여행 경로

# sol.1
# correct
import collections

answer = []
graph = collections.defaultdict(list)


def solution(tickets):
    answer_list = []
    answer = ['ICN']

    # 목적지 정보를 담고 있는 dictionary 만들기
    route_dict = {}
    for i in tickets:
        dep = i[0]
        arr = i[1]
        if route_dict.get(dep):
            route_dict[dep].append(arr)
        else:
            route_dict[dep] = [arr]
    print(route_dict)

    for k, v in route_dict.items():
        route_dict[k].sort()
    print(route_dict)

    # dictionary 내에서 물고가기
    next_city_list = route_dict["ICN"]

    answer.append()

    return answer

    for dept_city in route_dict[answer[0]]:
        answer.append(dept_city)
        next_city_list = route_dict[dept_city]
        if next_city_list == []:
            if all(i == [] for i in route_dict.values()):
                return answer
            else:
                break
