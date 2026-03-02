"""
📝 Question:
Given an array, reverse the order of its elements and return the reversed array.

Example:
  Input:  [1, 2, 3, 4, 5]
  Output: [5, 4, 3, 2, 1]
"""

# Reverse an Array

def reverse_array(arr):
    return arr[::-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"Original: {arr}")
    print(f"Reversed: {reverse_array(arr)}")
