"""
📝 Question:
Given an array of strings, find the longest common prefix string
amongst them. If there is no common prefix, return an empty string.

Example:
  Input:  ['flower', 'flow', 'flight']
  Output: 'fl'
"""

# Longest Common Prefix

def longest_common_prefix(strs):
    if not strs:
        return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    prefix = ""
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            break
        prefix += first[i]
    return prefix


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
    print(longest_common_prefix(["dog", "car", "race"]))        # ""
