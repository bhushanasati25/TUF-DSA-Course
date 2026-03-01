"""
🔗 Problem: Count Hills and Valleys in an Array
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

📝 Description:
   Count hills (local max) and valleys (local min) in the array.
"""

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        last = 0  # index of last distinct element

        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue  # skip duplicates ahead

            if nums[i] > nums[last] and nums[i] > nums[i + 1]:
                count += 1  # hill
            elif nums[i] < nums[last] and nums[i] < nums[i + 1]:
                count += 1  # valley

            last = i  # update last distinct index

        return count
