for i in range(9):
    if i < 5:
        for j in range(i + 1):
            print("*", end=" ")
    else:
        for j in range(9 - i):
            print("*", end=" ")
    print()
