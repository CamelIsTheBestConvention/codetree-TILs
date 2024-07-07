arr = list(map(int, input().split()))
max = 0
min = arr[0]

for i in arr:
    if i == 999 or i == -999:
        break
    
    if max < i:
        max = i
    if min > i:
        min = i

print(max, min)