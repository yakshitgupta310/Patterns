# m=int(input())
m = 5


def comb(n, r):
    z = n - r
    fn = 1
    fr = 1
    fz = 1
    for i in range(1, n + 1):
        fn = (fn * i)
        if i == r:
            fr = fn
        if i == z:
            fz = fn

    return (fn // (fr * fz))


for i in range(m):
    for j in range(i + 1):
        a = comb(i, j)
        print(a, end="\t")
    print()
