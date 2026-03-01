"""
🔗 Problem: Maximum Difference Between Increasing Elements
📂 Category: Arrays
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/maximum-difference-between-increasing-elements/

📝 Description:
   Find max difference nums[j]-nums[i] where i<j and nums[i]<nums[j].
"""

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        max_diff = -1
        
        for x in nums[1:]:
            if x > min_val:
                max_diff = max(max_diff, x - min_val)
            else:
                min_val = x
                
        return max_diff
