"""
🔗 Problem: Longest Unequal Adjacent Groups Subsequence I
📂 Category: Two-Pointers
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

📝 Description:
   Find longest subsequence with alternating group values.
"""

class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        if not words or not groups:
            return []

        result = [words[0]]
        last_group = groups[0]

        for i in range(1, len(words)):
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]

        return result
