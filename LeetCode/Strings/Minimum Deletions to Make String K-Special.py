"""
🔗 Problem: Minimum Deletions to Make String K-Special
📂 Category: Strings
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

📝 Description:
   Min deletions so max and min char frequencies differ by ≤ k.
"""

class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        from collections import Counter

        freq = Counter(word).values()
        freq = list(freq)
        min_deletions = float('inf')

        for base in range(max(freq) + 1):
            deletions = 0
            for f in freq:
                if f < base:
                    deletions += f  # delete all occurrences
                elif f > base + k:
                    deletions += f - (base + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
