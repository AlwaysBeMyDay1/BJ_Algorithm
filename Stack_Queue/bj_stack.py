# 스택 수열
# 1~k 까지 pl에 입력하며
# 각 입력마다 nl[0]과 비교.
# 만약 nl[0]과 같다면 nl.pop(0), pl.pop(-1)
def filter_sequence():
    k,*nl=map(int,open(0).read().split())
    pl,al=[],[]
    for i in range(1,k+1):
        pl.append(i)
        al.append('+')
        while pl[-1]==nl[0]:
            nl.pop(0)
            pl.pop(-1)
            al.append('-')
            if nl==[] or pl==[]:
                break
    
    if nl!=[]:
        print('NO')
    else:
        print(*al,sep='\n')
    



# 괄호
def filter_bracket():
    while True:
        s=input()
        if s=='.':break
        r=[]
        for a in s:
            if a in ['(',')']:
                n=1
                if a=='(':r.append(n)
                else:
                    if r!=[]:
                        p=r.pop()
                        if p!=n:
                            print('no')
                            break
                    else:
                        print('no')
                        break
            elif a in ['[',']']:
                n=2
                if a=='[':r.append(n)
                else:
                    if r!=[]:
                        p=r.pop()
                        if p!=n:
                            print('no')
                            break
                    else:
                        print('no')
                        break
        else:
            if r!=[]:
                print('no')
            else:
                print('yes')
            

# 제로
def get_sum_of_stack():
    k,*nl=map(int,open(0).read().split())
    a=[]
    for n in nl:
        if n==0:
            a.pop()
        else:
            a.append(n)
    print(sum(a))