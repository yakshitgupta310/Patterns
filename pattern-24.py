#n=int(input())
n=5

for i in range(1,n+1):
    if i<(n//2)+1:
        for j in range(1,(n//2)+1):
            print("",end="\t")
        for k in range(1,i+1):
            print("*",end="\t")
    elif i==(n//2)+1:
        for j in range(1,n+1):
            print("*",end="\t")
    else:
        for j in range(1,(n//2)+1):
            print("",end="\t")
        for k in range(n+1-i):
            print("*",end="\t")
    print()
