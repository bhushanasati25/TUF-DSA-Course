"""
🔗 Problem: Find Minimum Operations to Make All Elements Divisible by Three
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

📝 Description:
   Min +1/-1 operations to make all elements divisible by 3.
"""

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Count elements that are not divisible by 3
        return sum(1 for x in nums if x % 3 != 0)
