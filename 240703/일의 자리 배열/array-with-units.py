arr = list(map(int, input().split()))

print(arr[0], arr[1], end=' ')

for i in range(2, 10):
    arr.append((arr[i-2] + arr[i-1]) % 10)
    print(arr[i], end=' ')