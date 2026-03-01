"""
🔗 Problem: Smallest Number With All Set Bits
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/smallest-number-with-all-set-bits/

📝 Description:
   Find smallest number ≥ n with all bits set (2^k - 1).
"""

class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (1 << n.bit_length()) - 1
