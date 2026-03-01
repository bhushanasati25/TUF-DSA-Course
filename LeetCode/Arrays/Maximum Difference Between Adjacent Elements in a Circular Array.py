"""
🔗 Problem: Maximum Difference Between Adjacent Elements in a Circular Array
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

📝 Description:
   Find max absolute difference between adjacent elements in circular array.
"""

class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_diff = abs(nums[0] - nums[-1])  # circular difference

        for i in range(1, n):
            max_diff = max(max_diff, abs(nums[i] - nums[i - 1]))

        return max_diff
