result = []
while True:
  a = list(map(int, input().split()))
  if len(a) == 0:
    break
  else:
    result.append(sum(a))

for i in result:
  print(i)