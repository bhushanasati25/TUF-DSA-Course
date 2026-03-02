"""
📝 Question:
Given a string, reverse its characters and return the result.

Example:
  Input:  'hello'
  Output: 'olleh'
"""

# Reverse a String

def reverse_string(s):
    return s[::-1]


if __name__ == "__main__":
    print(reverse_string("hello"))    # "olleh"
    print(reverse_string("Python"))   # "nohtyP"
