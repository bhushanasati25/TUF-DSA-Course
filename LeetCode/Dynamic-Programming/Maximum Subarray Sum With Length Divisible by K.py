"""
🔗 Problem: Maximum Subarray Sum With Length Divisible by K
📂 Category: Dynamic-Programming
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

📝 Description:
   Find max subarray sum with length divisible by k.
"""

class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        pref = 0

        INF = float('inf')
        min_pref = [INF] * k
        min_pref[0] = 0 

        ans = -INF

        for i, x in enumerate(nums):
            pref += x
            idx = i + 1
            r = idx % k

            if min_pref[r] != INF:
                candidate = pref - min_pref[r]
                if candidate > ans:
                    ans = candidate

            if pref < min_pref[r]:
                min_pref[r] = pref

        if ans == -INF:
            return 0
        return ans
