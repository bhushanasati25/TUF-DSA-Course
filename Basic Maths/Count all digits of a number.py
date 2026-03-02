"""
📝 Question:
Given a non-negative integer n, count the total number of digits in it.

Example:
  Input:  12345
  Output: 5

  Input:  0
  Output: 1
"""

# Count All Digits of a Number

def count_digits(n):
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        n //= 10
        count += 1
    return count


if __name__ == "__main__":
    print(count_digits(12345))  # 5
    print(count_digits(0))      # 1
