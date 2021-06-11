"""
    *
   ***
  *****
 *******
*********
"""
for i in range(7):
    for j in range(7 - i):
        print(" ", end="")
    for k in range((2 * i) + 1):
        print("*", end="")
    print()
