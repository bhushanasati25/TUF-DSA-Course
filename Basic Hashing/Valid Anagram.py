"""
📝 Question:
Given two strings s and t, return True if t is an anagram of s.
An anagram uses the exact same characters with the same frequencies.

Example:
  Input:  s = 'anagram', t = 'nagaram'
  Output: True
"""

# Check if Two Strings are Valid Anagrams

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
