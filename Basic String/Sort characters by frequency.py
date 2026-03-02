"""
📝 Question:
Given a string, return the characters sorted by their frequency
in descending order. Break ties alphabetically.

Example:
  Input:  'tree'
  Output: ['e', 'r', 't']
"""

# Sort Characters by Frequency

from collections import Counter

def frequency_sort(s):
    count = Counter(s)
    return sorted(count.keys(), key=lambda c: (-count[c], c))


if __name__ == "__main__":
    print(frequency_sort("tree"))    # ['e', 'r', 't']
