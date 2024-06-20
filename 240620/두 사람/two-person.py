age1, gen1 = map(str, input().split())
age2, gen2 = map(str, input().split())

if (int(age1) >= 19 and gen1 == 'M') or (int(age2) >= 19 and gen2 == 'M'):
    print(1)
else:
    print(0)