n = int(input())
arr = list(map(int, input().split()))
cnt = 0
min = arr[0]

for i in arr:
    if min > i:
        min = i

cnt = arr.count(min)

print(min, cnt)