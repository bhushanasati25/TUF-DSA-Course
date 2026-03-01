"""
🔗 Problem: Partition Array According to Given Pivot
📂 Category: Arrays
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/partition-array-according-to-given-pivot/

📝 Description:
   Rearrange array so elements < pivot come before elements > pivot.
"""

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        equal = []
        greater = []
        
        # Traverse the array and classify numbers
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        # Concatenate the three lists to get the final result
        return less + equal + greater
