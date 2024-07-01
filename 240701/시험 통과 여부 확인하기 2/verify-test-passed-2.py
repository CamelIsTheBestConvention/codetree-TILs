n = int(input())
hap = 0

for i in range(n):
    arr = list(map(int, input().split()))
    sum = 0

    for j in arr:
        sum += j

    if (sum/4) >= 60:
        print("pass")
        hap += 1
    else:
        print("fail")

print(hap)