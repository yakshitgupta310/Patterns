# n=int(input())

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="\t")
    for k in range(1, 2 * (n - i)):
        print("", end="\t")
    if j == n:
        j -= 1
    for l in range(j, 0, -1):
        print(l, end="\t")
    print()
