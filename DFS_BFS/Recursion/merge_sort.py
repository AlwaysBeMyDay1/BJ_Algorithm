# https://www.acmicpc.net/problem/24060
# 알고리즘 수업 - 병합 정렬 1
# ref)https://velog.io/@wngud4950/%EB%B0%B1%EC%A4%80-24060.-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%EB%B3%91%ED%95%A9%EC%A0%95%EB%A0%AC1
# ref)https://www.daleseo.com/sort-merge/

a=[]
def merge_sort(list):
    if len(list) < 2:
        return list
    mid=(len(list)+1)//2
    low=merge_sort(list[:mid])
    high=merge_sort(list[mid:])

    merged_list=[]
    l=h=0
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merged_list.append(low[l])
            a.append(low[l])
            l+=1
        else:
            merged_list.append(high[h])
            a.append(high[h])
            h+=1
    merged_list += low[l:]
    for i in low[l:]:
        a.append(i)
    merged_list += high[h:]
    for i in high[h:]:
        a.append(i)
    return merged_list

n,k,*l=map(int,open(0).read().split())
merge_sort(l)
if len(a)>=k:
    print(a[k-1])
else:
    print(-1)



# 다른 방법
def find(s,e):
    global K
    if s == e:return
    m=(s+e)//2
    find(s,m)
    find(m+1,e)
    if K <=e-s+1:
        J=sorted(I[s:e+1])
        print(J[K-1])
        exit()
    K -= e-s+1

N,K=map(int,input().split())
I=list(map(int,input().split()))
find(0, N-1)
print(-1)