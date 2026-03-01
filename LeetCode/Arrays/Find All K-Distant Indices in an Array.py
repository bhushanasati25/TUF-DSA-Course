"""
🔗 Problem: Find All K-Distant Indices in an Array
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

📝 Description:
   Find indices within distance k of an element equal to a key.
"""

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        start = 0

        for i in range(n):
            if nums[i] == key:
                left = max(0, i - k)
                right = min(n - 1, i + k)

                while start <= right:
                    if start >= left:
                        result.append(start)
                    start += 1

        return result
