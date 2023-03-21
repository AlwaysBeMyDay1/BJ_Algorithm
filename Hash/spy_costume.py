# 1st sol
# right but time exceed
from itertools import combinations


def multiply(arr):
  ans = 1
  for n in arr:
    ans *= n
  return ans


def solution1(clothes_list):
  new_dict = {}

  for clothes in clothes_list:
    if clothes[1] in new_dict:
      new_dict[clothes[1]] += 1
    else:
      new_dict[clothes[1]] = 1

  calc_num = len(new_dict)
  dict_values = new_dict.values()
  answer = multiply(dict_values)
  for i in range(1, calc_num):
    comb_list = list(combinations(dict_values, i))
    for comb in comb_list:
      answer += multiply(comb)

  return answer


# 2nd sol
# right
def solution2(clothes_list):
  new_dict = {}

  for clothes in clothes_list:
    if clothes[1] in new_dict:
      new_dict[clothes[1]] += 1
    else:
      new_dict[clothes[1]] = 1

  dict_values = new_dict.values()
  answer = 1
  for i in dict_values:
    answer *= i + 1
  return answer - 1


# answer
# no need to make dictionary directly
# there is COUNTER
from collections import Counter


def solution(clothes_list):
  new_dict = Counter([x[1] for x in clothes_list])

  dict_values = new_dict.values()
  answer = 1
  for i in dict_values:
    answer *= i + 1
  return answer - 1


print(
  solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"]]))
