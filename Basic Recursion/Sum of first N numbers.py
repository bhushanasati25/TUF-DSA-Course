"""
📝 Question:
Given a positive integer N, find the sum of all numbers from 1 to N
using recursion.

Example:
  Input:  10
  Output: 55  (1 + 2 + ... + 10)
"""

# Sum of First N Numbers (Recursive)

def sum_n(n):
    if n <= 0:
        return 0
    return n + sum_n(n - 1)


if __name__ == "__main__":
    print(sum_n(10))  # 55
    print(sum_n(5))   # 15
