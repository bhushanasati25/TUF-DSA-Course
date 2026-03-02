"""
📝 Question:
Print a binary triangle with alternating 1s and 0s.
Odd rows start with 1, even rows start with 0.

For n = 4:
  1
  0 1
  1 0 1
  0 1 0 1
"""

# Pattern 11: Binary Triangle (alternating 1 and 0)
# 1
# 0 1
# 1 0 1
# 0 1 0 1

def pattern11(n):
    for i in range(n):
        start = 1 if i % 2 == 0 else 0
        row = []
        for j in range(i + 1):
            row.append(str(start))
            start = 1 - start
        print(" ".join(row))

pattern11(5)
