for i in range(1, 20):
    for j in range(1, 20):
        print(f"{i} * {j} = {i*j}", end=' ')
        
        if j == 19:
            print(' ', end=' ')
        elif j % 2 == 1:
            print('/', end=' ')
        else:
            print(' ', end=' ')


        if j % 2 == 0:
            print()
    print()