n = 5
for i in range(0, n):
    if i <= (n // 2):
        for j in range(((n) // 2) - i):
            print("", end="\t")
        for k in range(i + 1):
            print("*", end="\t")
        for l in range(i):
            print("*", end="\t")
    else:
        for j in range(i - ((n - 1) // 2)):
            print("", end="\t")
        for k in range(n - i):
            print("*", end="\t")
        for l in range(n - i - 1):
            print("*", end="\t")
    print()
