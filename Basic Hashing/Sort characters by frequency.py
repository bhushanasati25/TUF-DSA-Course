"""
📝 Question:
Given a string, sort the characters by their frequency in descending order.
If two characters have the same frequency, sort them alphabetically.
Return the sorted list of characters.

Example:
  Input:  'tree'
  Output: ['e', 'r', 't']  (e appears 2 times, r and t appear 1 time each)
"""

# Sort Characters by Frequency

from collections import Counter

def frequency_sort(s):
    count = Counter(s)
    # Sort by frequency (desc), then alphabetically
    return sorted(count.keys(), key=lambda c: (-count[c], c))


if __name__ == "__main__":
    print(frequency_sort("tree"))    # ['e', 'r', 't']
    print(frequency_sort("aabbcc")) # ['a', 'b', 'c']
