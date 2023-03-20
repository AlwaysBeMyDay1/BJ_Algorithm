day = int(input())
a = list(map(int, input().split()))

print(len([i for i in a if day==i]))