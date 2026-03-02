"""
📝 Question:
Given a string num representing a large integer, return the largest-valued
odd integer that is a non-empty substring of num. If no odd integer exists,
return an empty string.

Example:
  Input:  '52'
  Output: '5'
"""

# Largest Odd Number in String

def largest_odd_num(s):
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 == 1:
            return s[:i + 1].lstrip('0') or '0'
    return ''


if __name__ == "__main__":
    print(largest_odd_num("52"))      # "5"
    print(largest_odd_num("4206"))    # ""
    print(largest_odd_num("35427"))   # "35427"
