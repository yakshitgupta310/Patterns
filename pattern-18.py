n = 7

for i in range(n):
    if i <= (n // 2):
        for j in range(i + (n // 2) + 1):
            if j == ((n // 2) - i) or j == (i + (n // 2)):
                print("*", end="\t")
            else:
                print("", end="\t")
    else:
        for j in range(n):
            if j == (i - (n // 2)) or j == ((n // 2) * 3) - i:
                print("*", end="\t")
            else:
                print("", end="\t")
    print()
