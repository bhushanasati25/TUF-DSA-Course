"""
📝 Question:
Given a string, reverse it using recursion (without slicing shortcuts).

Example:
  Input:  'hello'
  Output: 'olleh'
"""

# Reverse a String (Recursive)

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse_string("hello"))    # "olleh"
    print(reverse_string("Python"))   # "nohtyP"
