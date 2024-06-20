a,b = map(int,input().split())
c = 0
d = 0

if a < b:
    c = 1
else:
    c = 0

if a == b:
    d = 1
else:
    d = 0

print(c, d)