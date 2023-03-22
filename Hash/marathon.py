# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수


def solution(participant, completion):
    new_dict = {}
    for i in completion:
        if new_dict.get(i):
            new_dict[i] += 1
        else:
            new_dict[i] = 1

    for i in participant:
        if not new_dict.get(i):
            return i
        else:
            if new_dict.get(i) == 0:
                return i
            else:
                new_dict[i] -= 1


# 1st try
# right but overed time
def solution1(participant, completion):
    for x in participant:
        if x in completion:
            completion.remove(x)
        else:
            return x
    return 'no answer'


# 2nd try
# right but overed time
def solution2(participant, completion):
    for x in participant:
        if participant.count(x) != completion.count(x):
            return x


# 3rd try
# succeed
def solution3(participant, completion):
    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)

    for index, x in enumerate(sorted_participant):
        try:
            if x != sorted_completion[index]:
                return x
        except:
            return x


# answer 1
import collections


def solution_a1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# answer 2
def solution_a2(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
