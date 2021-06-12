# n=int(input())
n = 5
for i in range(n):
    for j in range(n - i):
        if j == n - i - 1:
            print("*", end="\t")
        else:
            print("a", end="\t")
    print()
