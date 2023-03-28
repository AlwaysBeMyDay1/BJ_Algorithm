# fibonacci with Recursion
def fibonacci(num):
    if num < 3:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def solution(num):
    return fibonacci(num)


print(solution(6))