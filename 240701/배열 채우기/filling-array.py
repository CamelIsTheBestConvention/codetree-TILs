arr = list(map(int, input().split()))
arr2 = []

for i in range(len(arr)):
    if arr[i] == 0:
        break
    else:
        arr2.append(arr[i])

for i in range(len(arr2)-1, -1, -1):
    print(arr2[i], end=' ')