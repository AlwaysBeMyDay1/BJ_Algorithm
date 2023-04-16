# 모험가 길드
def guild():
    n,*l=map(int,open(0).read().split())
    l.sort()
    
    # result: 그룹 수, count: 현재 그룹의 사람 수
    result,count=0,0
    
    for i in l:
        count+=1
        if count >= i:
            result+=1
            count=0
    print(result)  