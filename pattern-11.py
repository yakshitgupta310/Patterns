x = 1
for i in range(5):
    for j in range(5 - i):
        print(x, end=" ")
        x += 1
    print()
