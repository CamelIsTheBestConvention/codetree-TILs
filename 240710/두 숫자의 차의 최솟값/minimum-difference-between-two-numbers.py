n = int(input())
arr = list(map(int, input().split()))
min = arr[1] - arr[0]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] - arr[i] < min:
            min = arr[j] - arr[i]

print(min)