n = int(input())
a, b, c, d = map(int, input().split())

print(1 if n > a else 0)
print(1 if n > b else 0)
print(1 if n > c else 0)
print(1 if n > d else 0)