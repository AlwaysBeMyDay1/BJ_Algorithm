# 아스키 코드
import sys
def print_ascii():
    s = input()
    print(ord(s))

print_ascii()

# 문자열
import sys
def print_string():
    N = int(sys.stdin.readline().rstrip())
    result_list = []
    for i in range(0, N):
        input_string = input()
        result_list.append(input_string[0] + input_string[-1])
    print(*result_list, sep='\n')