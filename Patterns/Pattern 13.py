"""
📝 Question:
Print a triangle with incrementing numbers across rows.

For n = 4:
  1
  2 3
  4 5 6
  7 8 9 10
"""

# Pattern 13: Incrementing Number Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10

def pattern13(n):
    num = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" ".join(row))

pattern13(5)
