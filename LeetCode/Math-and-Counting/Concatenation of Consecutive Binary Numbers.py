"""
🔗 Problem: Concatenation of Consecutive Binary Numbers
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

📝 Description:
   Concatenate binary of 1 to n and return result mod 10^9+7.
"""

class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        length = 0
        
        for i in range(1, n + 1):
            # if i is power of 2
            if (i & (i - 1)) == 0:
                length += 1
            
            ans = ((ans << length) | i) % MOD
        
        return ans