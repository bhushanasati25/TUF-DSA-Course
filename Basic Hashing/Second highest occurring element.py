"""
📝 Question:
Given an array of integers, find the element with the second highest frequency.
If multiple elements have the same second-highest frequency, return the smallest.

Example:
  Input:  [1, 1, 2, 2, 2, 3]
  Output: 1 (frequency 2, which is second to 3's frequency of 3)
"""

# Second Highest Occurring Element in Array

from collections import Counter

def second_most_frequent(nums):
    count = Counter(nums)
    freqs = sorted(set(count.values()), reverse=True)
    if len(freqs) < 2:
        return -1
    second_freq = freqs[1]
    return min(k for k, v in count.items() if v == second_freq)


if __name__ == "__main__":
    print(second_most_frequent([1, 1, 2, 2, 2, 3]))  # 1
