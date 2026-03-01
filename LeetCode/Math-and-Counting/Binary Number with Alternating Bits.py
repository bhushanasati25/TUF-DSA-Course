"""
🔗 Problem: Binary Number with Alternating Bits
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/binary-number-with-alternating-bits/

📝 Description:
   Check if binary representation has alternating 0s and 1s.
"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = -1

        while n:
            bit = n & 1
            if bit == prev:
                return False
            prev = bit
            n >>= 1

        return True
