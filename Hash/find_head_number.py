# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록


# 1st sol
# right but time exceed
def solution1(phone_book):
  replaced_book = [x.replace(' ', '') for x in phone_book]
  for phone_number in replaced_book:
    for a in replaced_book:
      if a != phone_number and a.startswith(phone_number):
        return False
  return True


# 2nd sol
# right but time exceed
def solution2(phone_book):
  new_dict = {}

  for x in phone_book:
    non_spaced_x = x.replace(' ', '')
    len_x = len(non_spaced_x)
    if new_dict.get(len_x) is None:
      new_dict[len_x] = [non_spaced_x]
    else:
      new_dict[len_x].append(non_spaced_x)

  for k, v in new_dict.items():
    for com_v in v:
      for ok, ov in new_dict.items():
        if ok > k:
          for x in ov:
            if x.startswith(com_v):
              return False

  return True


# 3rd sol
# right
def solution3(phone_book):
  sorted_list = sorted(phone_book)

  for index, x in enumerate(sorted_list):
    try:
      if sorted_list[index + 1].startswith(x):
        return False
    except:
      return True

  return True


# 4th sol
# 3에서 enumerate 사용하고, try-except 문 사용하는 대신 zip 사용하면 쉽게 구현 가능
def solution4(phone_book):
  sorted_list = sorted(phone_book)

  for a, b in zip(sorted_list, sorted_list[1:]):
    if b.startswith(a):
      return False
  return True


# 5th sol ★★
# hash 사용
def solution5(phone_book):
  dict = {}

  for phone_number in phone_book:
    dict[phone_number] = 1

  for phone_number in phone_book:
    temp = ''
    for number in phone_number:
      temp += number
      if temp != phone_number and temp in dict:
        return False

  return True


# 5th -2 sol
# with list
def solution(phone_book):
  for phone_number in phone_book:
    temp = ''
    for number in phone_number:
      temp += number
      if temp != phone_number and temp in phone_book:
        return False

  return True


print(solution(["119", "97674223", "1195524421", "112"]))