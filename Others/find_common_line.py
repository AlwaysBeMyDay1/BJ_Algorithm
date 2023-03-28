def solution(lines):
    dict = {}
    answer = 0
    for line in lines:
        for i in range(line[0], line[1]):
            mid_range = (i + i + 1) / 2
            if dict.get(mid_range):
                dict[mid_range] += 1
            else:
                dict[mid_range] = 1

    for k, v in dict.items():
        if v >= 2:
            answer += 1
    return answer
