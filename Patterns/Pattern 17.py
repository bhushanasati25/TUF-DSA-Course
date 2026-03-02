"""
📝 Question:
Print an alphabet pyramid (diamond letters centered).

For n = 4:
     A
    ABA
   ABCBA
  ABCDCBA
"""

# Pattern 17: Alphabet Pyramid (Diamond letters)
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

def pattern17(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        left = "".join(chr(ord('A') + j) for j in range(i + 1))
        right = "".join(chr(ord('A') + j) for j in range(i - 1, -1, -1))
        print(spaces + left + right)

pattern17(5)
