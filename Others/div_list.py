def solution1(num_list, n):
    answer = []
    count = 0
    test = []
    for i in num_list:
        count += 1
        test.append(i)
        if count == n:
            count = 0
            answer += [test]
            test = []

    return answer

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))