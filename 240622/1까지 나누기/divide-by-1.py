n = int(input())
a = n

for i in range(1, n+1):
    a //= i
    if a <= 1:
        print(i)
        break