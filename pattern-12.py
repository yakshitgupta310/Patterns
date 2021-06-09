# N = no. of rows

def pattern(n):
    x = n * (n + 1) / 2

    for i in range(n):
        for j in range(i + 1):
            print(int(x), end=" ")
            x -= 1
        print()


pattern(5)
