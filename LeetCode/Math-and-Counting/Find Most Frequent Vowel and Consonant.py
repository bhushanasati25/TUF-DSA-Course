"""
🔗 Problem: Find Most Frequent Vowel and Consonant
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

📝 Description:
   Find max sum of most frequent vowel and consonant frequencies.
"""

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        counts = Counter(s)
        vowels = set("aeiou")

        # compute maximum safely without default keyword
        max_vowel = 0
        for c in vowels:
            if c in counts and counts[c] > max_vowel:
                max_vowel = counts[c]

        max_cons = 0
        for c, v in counts.items():
            if c not in vowels and v > max_cons:
                max_cons = v

        return max_vowel + max_cons
