"""
🔗 Problem: Adjacent Increasing Subarrays Detection II
📂 Category: Arrays
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

📝 Description:
   Find max k such that two adjacent increasing subarrays of length k exist.
"""

class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        ans = 0
        pre = 0  
        cur = 1   

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
            
                ans = max(ans, cur // 2, min(pre, cur))
                pre, cur = cur, 1

        ans = max(ans, cur // 2, min(pre, cur))
        return ans
