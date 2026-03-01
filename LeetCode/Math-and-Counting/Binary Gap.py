"""
🔗 Problem: Binary Gap
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/binary-gap/

📝 Description:
   Find longest distance between consecutive 1s in binary representation.
"""

class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:]
        prev = None
        ans = 0

        for i, bit in enumerate(b):
            if bit == '1':
                if prev is not None:
                    ans = max(ans, i - prev)
                prev = i

        return ans