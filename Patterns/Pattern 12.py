"""
📝 Question:
Print a number mirror pattern.

For n = 4:
  1      1
  12    21
  123  321
  12344321
"""

# Pattern 12: Number Mirror
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

def pattern12(n):
    for i in range(1, n + 1):
        left = "".join(str(j) for j in range(1, i + 1))
        right = "".join(str(j) for j in range(i, 0, -1))
        spaces = " " * (2 * (n - i))
        print(left + spaces + right)

pattern12(5)
