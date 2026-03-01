"""
🔗 Problem: Count Partitions with Even Sum Difference
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/count-partitions-with-even-sum-difference/

📝 Description:
   Count ways to partition array where sum difference is even.
"""

class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = sum(nums)

        if total % 2 != 0:
            return 0 

        return len(nums) - 1