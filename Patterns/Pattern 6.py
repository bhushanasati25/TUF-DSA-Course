"""
📝 Question:
Print an inverted right-angled triangle with incrementing numbers.

For n = 4:
  1 2 3 4
  1 2 3
  1 2
  1
"""

# Pattern 6: Inverted Right Triangle of Numbers
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def pattern6(n):
    for i in range(n, 0, -1):
        print(" ".join(str(j) for j in range(1, i + 1)))

pattern6(5)
