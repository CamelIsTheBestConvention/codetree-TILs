a = int(input())

for i in range(a*2-1):
    if i < a:
        star = 2 * i + 1
    else:
        star = 2 * (a*2-1 - i - 1) + 1
    space = (a*2-1 - star) // 2
    print(' ' * space + '*' * star + ' ' * space)