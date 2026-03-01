"""
🔗 Problem: Count Odd Numbers in an Interval Range
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

📝 Description:
   Count odd numbers in the inclusive range [low, high].
"""

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high + 1) // 2 - (low // 2)