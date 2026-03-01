"""
🔗 Problem: Power of Four
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/power-of-four/

📝 Description:
   Check if a number is a power of four.
"""

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0
