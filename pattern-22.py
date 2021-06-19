# n=int(input())

n = 7
for i in range(n):
    y = i - (n // 2) + 1
    if i <= (n // 2):
        x = i + 1
        for j in range((n // 2) - i):
            print("", end="\t")
        for k in range(i + 1):
            print(x, end="\t")
            x += 1
        x -= 2
        for l in range(i):
            print(x, end="\t")
            x -= 1
    else:
        x = n - i
        for j in range(i - (n // 2)):
            print("", end="\t")
        for k in range(n - i):
            print(x, end="\t")
            x += 1
        x -= 2
        for l in range(n - 1 - i):
            print(x, end="\t")
            x -= 1
    print()
