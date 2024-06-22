a, b = map(int, input().split())
moon = 1

for i in range(1, b+1):
    if i % a == 0:
        moon *= i

print(moon)