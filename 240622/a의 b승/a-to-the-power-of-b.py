a, b = map(int, input().split())
moon = 1

for i in range(b):
    moon *= a

print(moon)