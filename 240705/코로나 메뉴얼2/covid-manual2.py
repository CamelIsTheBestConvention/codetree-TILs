arr = [0] * 4

for i in range(3):
    a, b = input().split()

    if int(b) >= 37:
        if a == 'Y':
            arr[0] += 1
        else:
            arr[1] += 1
    else:
        if a == 'Y':
            arr[2] += 1
        else:
            arr[3] += 1

print(*arr, end=' ')
if arr[0] >= 2:
    print('E')