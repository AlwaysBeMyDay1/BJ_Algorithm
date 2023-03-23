# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기

# sol.3
# 68.8/100
def solution(s):
    answer = ''
    word_list = s.split(' ')
    for word in word_list:
        if word != '':
            for index, i in enumerate(word):
                if index % 2 == 0:
                    answer += i.upper()
                else:
                    answer += i.lower()
            answer += ' '
    return answer.rstrip(' ')

# sol.2
# 68.8/100
def solution2(s):
    answer = ''
    word_list = s.split(' ')
    for word in word_list:
        for index, i in enumerate(word):
            if index % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
        answer += ' '
    return answer.rstrip(' ')

# sol.1
# 56.3/100
def solution1(s):
    answer = ''
    word_list = s.split(' ')
    for word in word_list:
        for index, i in enumerate(word):
            if index % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
        answer += ' '
    return answer.strip(' ')