"""
📝 Question:
Given a non-negative integer n, compute n! (n factorial).
n! = 1 × 2 × 3 × ... × n. By convention, 0! = 1.

Example:
  Input:  5
  Output: 120
"""

# Factorial of a Given Number (Iterative)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    for n in [0, 1, 5, 10]:
        print(f"{n}! = {factorial(n)}")
