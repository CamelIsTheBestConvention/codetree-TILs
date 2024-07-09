n = int(input())
arr = list(map(int, input().split()))
a = arr[0]
b = 0

for i in arr:
    if i < a:
        a = i
    elif i - a > b:
        b = i - a

print(b)