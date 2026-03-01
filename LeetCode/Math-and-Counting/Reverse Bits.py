"""
🔗 Problem: Reverse Bits
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/reverse-bits/

📝 Description:
   Reverse all 32 bits of a given unsigned integer.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res        