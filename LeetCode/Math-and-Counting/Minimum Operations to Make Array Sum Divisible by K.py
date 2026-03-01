"""
🔗 Problem: Minimum Operations to Make Array Sum Divisible by K
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

📝 Description:
   Min operations to make array sum divisible by k.
"""

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(nums) % k
