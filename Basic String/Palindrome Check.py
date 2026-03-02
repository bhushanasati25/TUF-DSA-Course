"""
📝 Question:
Given a string s, check if it is a palindrome.
A palindrome reads the same forwards and backwards.

Example:
  Input:  'racecar'
  Output: True
"""

# Check if a String is Palindrome

def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))    # False
