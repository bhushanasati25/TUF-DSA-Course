"""
🔗 Problem: Divide Array Into Arrays With Max Difference
📂 Category: Arrays
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

📝 Description:
   Split array into groups of 3 with max element difference ≤ k.
"""

class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            if len(group) == 3 and group[2] - group[0] <= k:
                res.append(group)
            else:
                return []
        return res
