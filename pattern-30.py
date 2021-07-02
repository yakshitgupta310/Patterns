"""
        A
      A B A
    A B C A B
  A B C D A B C
A B C D E A B C D
"""

x = 5
z = ord('A')
for i in range(z, z + x):
    for j in range((z + x) - i - 1):
        print(" ", end=" ")
    for k in range(i - z + 1):
        print(chr(z + k), end=" ")
    for l in range(i - z):
        print(chr(z + l), end=" ")
    print()
