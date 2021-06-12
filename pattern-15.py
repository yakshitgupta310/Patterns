n = 5

for i in range(n):
    for j in range(i + 1):
        if i == j:
            print("*", end="\t")
        else:
            print("a", end="\t")
    print()
