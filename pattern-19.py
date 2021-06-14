n = 5
x = 1
y = 1
for i in range(n):
    if i == 0:
        print(0)
        continue
    elif i == 1:
        print(x, end="\t")
        print(y, end="\t")
        print()
        continue
    for j in range(i + 1):
        temp = x
        x = y
        y = x + temp
        print(y, end="\t")
    print()
