# Pattern 16: Same Letter Triangle
# A
# B B
# C C C
# D D D D

def pattern16(n):
    for i in range(n):
        ch = chr(ord('A') + i)
        print((ch + " ") * (i + 1))

pattern16(5)
