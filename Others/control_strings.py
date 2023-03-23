# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 문자열 다루기 기본

# sol.1
# correct
def solution1(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()


# sol.2
# correct
# regex 사용 ->  // ^와 $는 문자열의 처음과 끝을 의미. \d는 숫자를 의미. {4}|{6}은 숫자가 4번 혹은 6번 반복되는 것을 의미함.

import re
def solution(s):
    return bool(re.match("^(\d{4}|\d{6})$", s))