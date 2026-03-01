"""
🔗 Problem: Longest Harmonious Subsequence
📂 Category: Two-Pointers
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/longest-harmonious-subsequence/

📝 Description:
   Find longest subsequence where max-min = 1.
"""

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)  # Count the frequency of each number
        max_length = 0
        
        for num in freq:
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])
        
        return max_length
