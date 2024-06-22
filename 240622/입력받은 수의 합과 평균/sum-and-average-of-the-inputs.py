n = int(input())
sum = 0

for i in range(n):
    a = int(input())
    sum += a

print("%d %.1f" % (sum, sum/n))