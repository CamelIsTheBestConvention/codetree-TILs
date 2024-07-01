arr = list(map(float, input().split()))
sum = 0

for i in arr:
    sum += i

print("%.1f" % (sum/8))