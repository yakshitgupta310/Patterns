n = 11

for i in range(n):
    if i < (n // 2):
        for j in range((n // 2) + i + 1):
            if j == (n // 2):
                print("*", end=" ")
            elif j == (n // 2) - i or j == (n // 2) + i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    elif i == (n // 2):
        for j in range(n):
            print("*", end=" ")
    else:
        for j in range((2 * i) - 1):
            if j == (n // 2):
                print("*", end=" ")
            elif j == (i - (n // 2)) or j == (n // 2) + (2 * (n // 2) + 1) - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
