n = 13

for i in range(n):
    if i <= (n // 2):
        for j in range((n // 2) - i + 1):
            print("*", end="\t")
        for k in range(i + 1):
            print("", end="\t")
        for l in range(i):
            print("", end="\t")
        for m in range((n // 2) + 1 - i):
            print("*", end="\t")
    else:
        for j in range(i - (n // 2) + 1):
            print("*", end="\t")
        for k in range(n - i):
            print("", end="\t")
        for l in range(n - i - 1):
            print("", end="\t")
        for m in range(i - (n // 2) + 1):
            print("*", end="\t")
    print()
