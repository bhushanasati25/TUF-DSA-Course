"""
🔗 Problem: Count Binary Substrings
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/count-binary-substrings/

📝 Description:
   Count substrings with equal consecutive 0s and 1s.
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        curr = 1
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1
        ans += min(prev, curr)
        return ans