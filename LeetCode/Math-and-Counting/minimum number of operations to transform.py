"""
🔗 Problem: minimum number of operations to transform
📂 Category: Math-and-Counting
🎯 Difficulty: Hard
🔗 URL: https://leetcode.com/problems/minimum-number-of-operations-to-transform/

📝 Description:
   Min one-bit operations to transform number to zero.
"""

class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans ^= n
            n >>= 1
        return ans
