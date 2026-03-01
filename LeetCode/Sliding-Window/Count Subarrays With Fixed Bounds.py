"""
🔗 Problem: Count Subarrays With Fixed Bounds
📂 Category: Sliding-Window
🎯 Difficulty: Hard
🔗 URL: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

📝 Description:
   Count subarrays where min equals minK and max equals maxK.
"""

class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        res = 0
        min_pos = max_pos = bad_pos = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_pos = i
            if num == minK:
                min_pos = i
            if num == maxK:
                max_pos = i
            res += max(0, min(min_pos, max_pos) - bad_pos)
        
        return res
