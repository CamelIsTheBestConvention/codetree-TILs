arr = list(map(int, input().split()))
sum = 0
cnt = 0

for i in arr:
    if i == 0:
        break
    else:
        sum += i
        cnt += 1

print(sum, end=' ')
print("%.1f" % (sum/cnt))