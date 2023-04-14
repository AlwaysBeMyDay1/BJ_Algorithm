
# 동전 0
def div_coin():
    n,k,*l=map(int,open(0).read().split())
    
    count = 0
    for i in reversed(range(n)):
        count += k//l[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
        k = k%l[i] # K는 동전으로 나눈 나머지로 계속 반복
    
    print(count)