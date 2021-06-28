# n=int(input())
n = 7
for i in range(n):
    if i < (n // 2):
        for j in range(n):
            if j == 0 or j == n - 1:
                print("*", end="\t")
            else:
                print("", end="\t")
    else:
        for j in range(n):
            if j == 0 or j == n - 1:
                print("*", end="\t")
            elif j == i:
                print("*", end="\t")
            elif j == (n - i - 1):
                print("*", end="\t")
            else:
                print("", end="\t")
    print()
