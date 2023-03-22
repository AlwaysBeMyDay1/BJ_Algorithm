# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586


# 1st sol
# incorrect
def solution1(progresses, speeds):
    result = []
    for progress, speed in zip(progresses, speeds):
        day = int((100 - progress) / speed)
        result.append(day)

    calc_num = 0
    answer = []
    for index, i in enumerate(result):
        calc_num += 1
        if index == len(result) - 1:
            answer.append(calc_num)
            break
        if i >= result[index + 1]:
            pass
        else:
            answer.append(calc_num)
            calc_num = 0
    return answer


# 2nd
# correct
# sol.1의 방식처럼 앞과 뒤만 비교하면 [5,3,4] 같은 경우는 해당안
def solution2(progresses, speeds):
    result = []
    for progress, speed in zip(progresses, speeds):
        day = int((100 - progress) /
                  speed) if (100 - progress) % speed == 0 else int(
                      (100 - progress) / speed) + 1
        result.append(day)

    calc_num = 0
    std_num = result[0]
    answer = []
    for index, i in enumerate(result):
        calc_num += 1
        if index == len(result) - 1:
            answer.append(calc_num)
            break
        if std_num >= result[index + 1]:
            pass
        else:
            answer.append(calc_num)
            std_num = result[index + 1]
            calc_num = 0
    return answer


# improved sol.2nd
def solution3(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


# sol. with pop()
def solution(progresses, speeds):
    answer = []

    count = 0
    time = 0
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


print(solution([1, 1, 1, 2], [10, 15, 12, 3]))
