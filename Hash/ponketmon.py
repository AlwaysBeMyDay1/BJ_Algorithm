from itertools import combinations


# 1st try
# right but overed time
def solution(nums):
  num = int(len(nums) / 2)
  combination = list(combinations(nums, num))
  duplication = [len(list(set(i))) for i in combination]
  answer = max(duplication)
  return answer


# 2nd try
# succeed
def solution2(nums):
  num = int(len(nums) / 2)
  new_num = int(len(list(set(nums))))
  answer = num if num < new_num else new_num
  return answer


# answer
def solution3(ls):
  return min(len(ls) / 2, len(set(ls)))


print(solution3([3, 1, 2, 3]))
