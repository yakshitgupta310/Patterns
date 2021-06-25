# n=int(input())
n = 7
for i in range(n):
    if i <= (n // 2):
        if i == 0:
            for j in range(n):
                if j <= (n // 2) or j == (n - 1):
                    print("*", end="\t")
                else:
                    print("", end="\t")
        elif i == (n // 2):
            for j in range(n):
                print("*", end="\t")
        else:
            for j in range(n):
                if j == (n // 2) or j == n - 1:
                    print("*", end="\t")
                else:
                    print("", end="\t")
    else:
        if i == n - 1:
            for j in range(n):
                if j == 0 or j >= (n // 2):
                    print("*", end="\t")
                else:
                    print("", end="\t")
        else:
            for j in range(n):
                if j == (n // 2) or j == 0:
                    print("*", end="\t")
                else:
                    print("", end="\t")

    print()
