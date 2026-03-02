"""
📝 Question:
Given an array of integers, count the number of odd elements in the array.

Example:
  Input:  [1, 2, 3, 4, 5]
  Output: 3
"""

# Count of Odd Numbers in Array

def count_odd(arr):
    return sum(1 for x in arr if x % 2 == 1)


if __name__ == "__main__":
    print(count_odd([1, 2, 3, 4, 5]))  # 3
