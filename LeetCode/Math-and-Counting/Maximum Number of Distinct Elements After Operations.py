"""
🔗 Problem: Maximum Number of Distinct Elements After Operations
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

📝 Description:
   Max distinct elements after adding [-k,k] to each element.
"""

class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        last = float('-inf')
        count = 0

        for num in nums:
            place = max(last + 1, num - k)
            if place <= num + k:
                count += 1
                last = place

        return count
