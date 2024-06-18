a, b, c = map(int, input().split("."))

temp = a
a = b
b = c
c = temp

print("%d-%d-%d" % (a, b, c))