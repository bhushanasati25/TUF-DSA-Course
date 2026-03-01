"""
🔗 Problem: Find the Maximum Length of Valid Subsequence II
📂 Category: Dynamic-Programming
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

📝 Description:
   Find longest subsequence where consecutive sum mod k is constant.
"""

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [[0] * k for _ in range(k)]
        ans = 0
        
        for x in nums:
            xm = x % k
            for prev in range(k):
                dp[prev][xm] = dp[xm][prev] + 1
                ans = max(ans, dp[prev][xm])
        
        return ans
