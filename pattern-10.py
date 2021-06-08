# n=int(input())
n = 7
for i in range(n):
    if i <= (n // 2):
        if i == 0:
            for j in range(n):
                print("*", end="\t")
        else:
            for j in range(n - i):
                if j == i or j == (n - i - 1):
                    print("*", end="\t")
                else:
                    print("", end="\t")
    else:
        if i == (n - 1):
            for j in range(n):
                print("*", end="\t")
        else:
            for j in range(i + 1):
                if j == (n - 1 - i) or j == (i):
                    print("*", end="\t")
                else:
                    print("", end="\t")

    print()
