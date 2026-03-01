"""
🔗 Problem: Longest Balanced Subarray I
📂 Category: Dynamic-Programming
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/longest-balanced-subarray-i/

📝 Description:
   Find longest subarray with equal count of two values.
"""

class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        for i in range(n):
            vis = set()
            cnt = [0, 0]
            for j in range(i, n):
                if nums[j] not in vis:
                    vis.add(nums[j])
                    cnt[nums[j] & 1] += 1
                if cnt[0] == cnt[1]:
                    ans = max(ans, j - i + 1)
        return ans