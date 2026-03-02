"""
📝 Question:
Given an array of integers, find the element that occurs the most number of times.
If multiple elements have the same highest frequency, return the smallest one.

Example:
  Input:  [1, 3, 2, 1, 4, 1, 3, 3]
  Output: 1 (frequency 3, but 1 < 3)
"""

# Highest Occurring Element in an Array

from collections import Counter

def most_frequent(nums):
    count = Counter(nums)
    max_freq = max(count.values())
    # Return smallest element with max frequency
    return min(k for k, v in count.items() if v == max_freq)


if __name__ == "__main__":
    print(most_frequent([1, 3, 2, 1, 4, 1, 3, 3]))  # 1
