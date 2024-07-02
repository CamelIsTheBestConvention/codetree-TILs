arr = list(map(int, input().split()))
sum = 0
avg = 0
cnt = 0

for i in range(len(arr)):
    if (i + 1) % 2 == 0:
        sum += arr[i]

    if (i + 1) % 3 == 0:
        avg += arr[i]
        cnt += 1

if cnt != 0:
    avg /= cnt

print(sum, end=' ')
print("%.1f" % avg)