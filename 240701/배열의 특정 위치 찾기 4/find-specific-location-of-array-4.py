arr = list(map(int, input().split()))
arr2 = []
cnt = 0
sum = 0

for i in arr:
    if i == 0:
        break
    else:
        arr2.append(i)

for i in arr2:
    if i % 2 == 0:
        sum += i
        cnt += 1

print(cnt, sum)