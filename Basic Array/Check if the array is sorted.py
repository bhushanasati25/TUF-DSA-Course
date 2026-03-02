"""
📝 Question:
Given an array of integers, check whether the array is sorted in non-decreasing order.
Return True if the array is sorted, otherwise return False.

Example:
  Input:  [1, 2, 3, 4, 5]
  Output: True

  Input:  [1, 3, 2, 4]
  Output: False
"""

# Check if the Array is Sorted

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(is_sorted([1, 2, 3, 4, 5]))   # True
    print(is_sorted([1, 3, 2, 4, 5]))   # False
