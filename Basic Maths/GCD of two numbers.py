"""
📝 Question:
Given two positive integers a and b, find their GCD (Greatest Common Divisor),
i.e., the largest number that divides both a and b.

Example:
  Input:  a = 12, b = 8
  Output: 4
"""

# GCD (Greatest Common Divisor) of Two Numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print(gcd(12, 8))   # 4
    print(gcd(54, 24))  # 6
