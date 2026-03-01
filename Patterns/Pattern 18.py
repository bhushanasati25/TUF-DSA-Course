# Pattern 18: Reverse Alphabet Triangle
# E
# D E
# C D E
# B C D E
# A B C D E

def pattern18(n):
    for i in range(n):
        start = chr(ord('A') + n - 1 - i)
        end = chr(ord('A') + n - 1)
        print(" ".join(chr(ord(start) + j) for j in range(i + 1)))

pattern18(5)
