def solution(lines):
    answer = 0
    for line in lines:
        for left, right in lines:
            if left < line[1]:
                print(line)
                answer += abs(min(line[1], right) - max(line[0], left))
    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))