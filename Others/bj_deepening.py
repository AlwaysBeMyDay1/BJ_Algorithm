# 너의 평점은
def calc_univ_score():
    rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
    grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
    
    total = 0	# 학점 총합을 담을 변수
    result = 0	# (학점 * 과목평점) 총합을 담을 변수
    for _ in range(20) :
        s, p, g = input().split()
        p = float(p)
        if g != 'P' :	# 등급이 P인 과목은 계산 안함
            total += p
            result += p * grade[rating.index(g)]
    
    print('%.6f' % (result / total))

# 그룹 단어 체커
def check_word_group_vers2():
    cnt=0
    for i in range(int(input())):
        word=input()
        cnt+=list(word)==sorted(word,key=word.find)
    print(cnt)
    
def check_word_group():
    n=int(input())
    wl=[]
    for i in range(n):
        wl.append(input())
    ans=0
    for w in wl:
        alpl=list(w)
        for alp in alpl:
            w=w.lstrip(alp)
            if alp in w:
                break
        else:
            ans+=1
    print(ans)
    

# 크로아티아 알파벳
def count_croatia_alphabet():
    a=input()
    for ca in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
        a=a.replace(ca,'*')
    print(len(a))


# 평균은 넘겠지
def find_over_avg():
    n=int(input())
    al=[]
    for i in range(n):
        n,*s=map(int, input().split())
        ac=sum(s)/len(s)
        gs=sum([1 if sc>ac else 0 for sc in s])
        al.append(round(gs/n*100,3))
    for a in al:
        print(f"{a:.3f}%")


# 단어 공부
def most_used_letter_vers2():
    C=input().upper()
    A=list(set(C));B=[]
    [B.append(C.count(i)) for i in A]
    print('?' if B.count(max(B))>1 else A[B.index(max(B))])

def most_used_letter_vers1():
    s=input().upper()
    d={}
    for i in set(s):
        c=s.count(i)
        d[i]=c
    mx=max(d.values())
    if list(d.values()).count(mx)>1:
        print('?')
    else:
        for k, v in d.items():
            if v == mx:
                print(k)


# 팰린드롬인지 확인하기
# 팰린드롬(like 기러기):그리스어 'Palin' 의 '뒤 (Back)', 또는 '다시 (again)' 라는 뜻과 '방향 (direction)'을 뜻하는 'dromos' 어원을 두고 있음.
def is_palindrome():
    s=input()
    # if s==s[::-1]:print(1)
    # else:print(0)
    print(+(s==s[::-1]))


# 킹, 퀸, 룩, 비숍, 나이트, 폰
def chess():
    found_num_list = [int(i) for i in input().split(' ')]

    piece_num_list = [1,1,2,2,2,8]

    answer = []
    for piece_num, found_num in zip(piece_num_list, found_num_list):
        answer.append(str(int(piece_num - found_num)))

    print(' '.join(answer).strip(' '))

# 별 찍기 - 7
import sys
def print_stars_vers7():
    N = int(sys.stdin.readline().rstrip())

    for i in range(1, 2 * N):
        space_num = abs(N - i)
        star_num = 2*N - 1 - 2*space_num
        print(' ' * space_num + '*' * star_num)
    
# 바구니 순서 바꾸기
import sys
def change_basket_order():
    N, M = [int(i) for i in (sys.stdin.readline().rstrip()).split(' ')]

    N_list = [str(i) for i in range(1, N + 1)]
    order_list = []
    for i in range(1, M + 1):
        order_list.append(sys.stdin.readline().rstrip())

    for order in order_list:
        i, j, k = [int(o)-1 for o in order.split(' ')]
        N_list = N_list[:i] + N_list[k:j+1] + N_list[i:k] + N_list[j+1:]

    print(' '.join(N_list).strip())

# change_basket_order()