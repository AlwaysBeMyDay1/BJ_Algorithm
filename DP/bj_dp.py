# 알고리즘 수업 - 피보나치 수 1
def compare_recursive_dp_vers2():
    n=int(input())
    a,b=0,1
    for i in range(n):a,b=b,a+b
    print(a,n-2)


def compare_recursive_dp_vers1():
    c1=0
    def fr(n):
        if n<3:
            global c1
            c1+=1
            return 1
        return fr(n-1)+fr(n-2)
        
    def fd(n):
        f=[0,1,1]
        c2=0
        for i in range(3,n+1):
            c2+=1
            f.append(f[i-1]+f[i-2])
        return c2,f[n]
    
    n=int(input())
    fr(n)
    c2,fn=fd(n)
    print(c1,c2,fn)