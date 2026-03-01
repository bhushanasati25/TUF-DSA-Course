"""
🔗 Problem: Number of Substrings With Only 1s
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/number-of-substrings-with-only-1s/

📝 Description:
   Count substrings consisting entirely of 1s.
"""

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        streak = 0  
        
        for ch in s:
            if ch == '1':
                streak += 1          
                ans = (ans + streak) % MOD  
            else:
                streak = 0          
        
        return ans
