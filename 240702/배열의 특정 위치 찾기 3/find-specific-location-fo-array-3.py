arr = list(map(int, input().split()))
arr2 = []
sum = 0

for i in range(len(arr)):
    if arr[i] == 0:
        break
    else:
        arr2.append(arr[i])

for i in arr2:
    sum += i

print(sum)