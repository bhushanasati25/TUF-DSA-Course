"""
📝 Question:
Given a positive integer n, count how many of its digits are odd.

Example:
  Input:  12345
  Output: 3  (digits 1, 3, 5 are odd)
"""

# Count Number of Odd Digits in a Number

def count_odd_digits(n):
    count = 0
    n = abs(n)
    while n > 0:
        if (n % 10) % 2 == 1:
            count += 1
        n //= 10
    return count


if __name__ == "__main__":
    print(count_odd_digits(12345))  # 3 (1, 3, 5)
