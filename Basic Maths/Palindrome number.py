"""
📝 Question:
Given an integer n, determine if it is a palindrome.
A palindrome number reads the same forwards and backwards.

Example:
  Input:  121
  Output: True

  Input:  123
  Output: False
"""

# Check if a Number is Palindrome

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome(121))   # True
    print(is_palindrome(123))   # False
