"""
🔗 Problem: Maximum Value of an Ordered Triplet II
📂 Category: Arrays
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

📝 Description:
   Find max value of (nums[i]-nums[j])*nums[k] for i<j<k.
"""

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_i = nums[0]
        max_diff = float('-inf')
        result = 0

        for j in range(1, n - 1):
            max_diff = max(max_diff, max_i - nums[j])
            result = max(result, max_diff * nums[j + 1])
            max_i = max(max_i, nums[j])

        return result
