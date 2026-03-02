"""
📝 Question:
Print a reverse alphabet triangle.
Each row starts from a decreasing letter up to the last letter.

For n = 4 (last letter = D):
  D
  C D
  B C D
  A B C D
"""

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
