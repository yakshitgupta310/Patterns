x=65
for i in range (0,5):
    for j in range(0,i+1):
        print(chr(x),end=" ")
        x=x+1
    print("\r")
