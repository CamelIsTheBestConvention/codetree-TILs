n = int(input())
arr = list(map(float, input().split()))
result = 0

for i in arr:
    result += i

result = result / n

print("%.1f" % result)
if result >= 4.0:
    print("Perfect")
elif result >= 3.0:
    print("Good")
else:
    print("Poor")