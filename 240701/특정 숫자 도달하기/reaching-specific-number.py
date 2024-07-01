arr = list(map(int, input().split()))
sum = 0
cnt = 0

for i in arr:
    if i >= 250:
        break
    else:
        sum += i
        cnt += 1
    
print(sum, end=' ')
print("%.1f" % (sum/cnt), end=' ')