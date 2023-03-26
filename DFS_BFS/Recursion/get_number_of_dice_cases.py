# 10 이하의 자연수 N을 입력받아 주사위를 N번 던져서 나올 수 있는 모든 경우를 출력하는 프로그램을 작성하시오

answer = []
def solution(N):
    dice_throws(N)
    return sorted(answer)

def dice_throws(N, outcome=[]):
    if N < 0:
        return
    else:
        for i in range(1,7):
            dice_throws(N-1, outcome+[i])
        answer.append(outcome)
        