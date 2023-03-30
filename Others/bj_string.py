# 단어의 개수
def print_word_num():
    N = input()
    print(max([int(n[::-1])for n in N.split()]))

print_word_num()


# 문자열 반복
def repeat_string():
    N = int(input())
    order_list = []
    for _ in range(N):
        order_list.append(input())

    for order in order_list:
        print(*list(map(lambda x: x*int(order.split()[0]), order.split()[1])), sep='')

        
# 알파벳 찾기
def find_alphabet2():
    s=input()
    a=list(range(97,123))
    for i in a:
        print (s.find(chr(i)))
    
from string import ascii_lowercase
def find_alphabet():
    alphabet_list = list(ascii_lowercase)
    alphabet_dict = {}
    for i in alphabet_list:
        alphabet_dict[i] = -1
        
    s = input()
    for alphabet in s:
        alphabet_dict[alphabet] = s.index(alphabet)

    print(*alphabet_dict.values())


# 숫자의 합
def print_stringfied_sum():
    n = input()
    s = input()
    answer = 0
    for num in s:
        answer += int(num)        
    print(answer)


# 아스키 코드
def print_ascii():
    s = input()
    print(ord(s))


# 문자열
import sys
def print_string():
    N = int(sys.stdin.readline().rstrip())
    result_list = []
    for i in range(0, N):
        input_string = input()
        result_list.append(input_string[0] + input_string[-1])
    print(*result_list, sep='\n')