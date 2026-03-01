"""
🔗 Problem: Divide an Array Into Subarrays With Minimum Cost I
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

📝 Description:
   Split array into 3 subarrays to minimize sum of first elements.
"""

class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = nums[0]
        min1 = float('inf')
        min2 = float('inf')
        
        for x in nums[1:]:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
        
        return first + min1 + min2
