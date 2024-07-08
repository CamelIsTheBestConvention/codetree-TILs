arr = list(map(int, input().split()))
a = 0
b = max(arr)

for i in arr:
    if i > 500 and b > i:
        b = i
    if i < 500 and a < i:
        a = i

print(a, b)