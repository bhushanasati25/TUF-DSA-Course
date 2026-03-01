"""
🔗 Problem: Keep Multiplying Found Values by Two
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/keep-multiplying-found-values-by-two/

📝 Description:
   Starting from original, keep doubling if value exists in array.
"""

class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        while original in nums:
            original *= 2

        return original
        