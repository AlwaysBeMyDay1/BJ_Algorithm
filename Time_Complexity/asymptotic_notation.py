# 점근적 표기법 : 상수 계수와 중요하지 않은 항목을 제거한 것
# https://dev-mandos.tistory.com/125

# 알고리즘 수업 - 점근적 표기 1
import sys
def asymp_not():
    a1, a0 = [int(x) for x in input().split(' ')]
    c = int(sys.stdin.readline().rstrip())
    n0 = int(sys.stdin.readline().rstrip())

    if a1 * n0 + a0 <= c * n0 and c >= a1:
        return 1
    else:
        return 0

print(asymp_not())