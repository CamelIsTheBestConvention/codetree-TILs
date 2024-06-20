a, b, c = map(int, input().split())
re1 = 0
re2 = 0

if a < b and a < c:
    re1 = 1
else:
    re1 = 0

if a == b and b == c:
    re2 = 1
else:
    re2 = 0

print(re1, re2)