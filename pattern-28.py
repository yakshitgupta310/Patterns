n = 7
for i in range(2 * n):
    if i < (n):
        for j in range(i + 1):
            print("*", end=" ")
        for k in range((2 * n) - i - 1):
            if k <= (2 * (n - i - 1) - 1):
                print(" ", end=" ")
            else:
                print("*", end=" ")
    else:
        for j in range((2 * n) - i):
            print("*", end=" ")
        for k in range(i):
            if k < (2 * (i - n)):
                print(" ", end=" ")
            else:
                print("*", end=" ")

    print()
