x = 0
for i in range(5):
    for j in range(i + 1):
        print(chr(x + 65), end=" ")
        x += 1
    print()
