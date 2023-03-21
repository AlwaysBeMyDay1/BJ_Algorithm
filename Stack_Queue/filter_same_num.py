# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906


# 1st sol
# right
def solution1(arr):
  answer = []
  for i in arr:
    if answer == []:
      answer.append(i)
    if answer[-1] != i:
      answer.append(i)
  return answer


# 1st sol - improved
# slicing 사용하면 빈 리스트인지 체크 안 해도됨
def solution(arr):
  answer = []
  for i in arr:
    if answer[-1:] != [i]:
      answer.append(i)
  return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))