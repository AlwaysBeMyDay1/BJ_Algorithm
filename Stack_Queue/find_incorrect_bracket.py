# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# sol. 1st
# correct
def solution1(s):
    stack = []
    opening = "("
    closing = ")"
    
    for bracket in s:
        if bracket == opening:
            stack.append(1)
        elif bracket == closing:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

# another sol.
# correct
def solution(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1
    return pair == 0