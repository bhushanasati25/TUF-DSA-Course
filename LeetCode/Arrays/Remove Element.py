"""
🔗 Problem: Remove Element
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/remove-element/

📝 Description:
   Remove all occurrences of a value in-place and return new length.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # next write position for a kept element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
