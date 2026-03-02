"""
📝 Question:
Given a non-negative integer n, compute n! (factorial) using recursion.

Example:
  Input:  5
  Output: 120  (5 × 4 × 3 × 2 × 1)
"""

# Factorial of a Given Number (Recursive)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    for n in [0, 1, 5, 10]:
        print(f"{n}! = {factorial(n)}")
