"""
🔗 Problem: Count Elements With Maximum Frequency
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/count-elements-with-maximum-frequency/

📝 Description:
   Count elements that have the maximum frequency.
"""

from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)               
        max_freq = max(freq.values())         
        return sum(v for v in freq.values() if v == max_freq)
