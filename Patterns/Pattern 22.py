"""
📝 Question:
Print a concentric number square pattern.
Each layer is filled with decreasing numbers from the outside in.

For n = 3:
  3 3 3 3 3
  3 2 2 2 3
  3 2 1 2 3
  3 2 2 2 3
  3 3 3 3 3
"""

# Pattern 22: Concentric Number Square
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5

def pattern22(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            val = n - min(i, j, size - 1 - i, size - 1 - j)
            print(val, end=" ")
        print()

pattern22(5)
