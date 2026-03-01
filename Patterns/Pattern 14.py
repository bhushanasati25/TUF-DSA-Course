# Pattern 14: Alphabet Triangle
# A
# A B
# A B C
# A B C D

def pattern14(n):
    for i in range(n):
        print(" ".join(chr(ord('A') + j) for j in range(i + 1)))

pattern14(5)
