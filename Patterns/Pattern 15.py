# Pattern 15: Inverted Alphabet Triangle
# A B C D E
# A B C D
# A B C
# A B
# A

def pattern15(n):
    for i in range(n, 0, -1):
        print(" ".join(chr(ord('A') + j) for j in range(i)))

pattern15(5)
