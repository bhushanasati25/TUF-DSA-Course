"""
🔗 Problem: Valid Triangle Number
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/valid-triangle-number/

📝 Description:
   Count triplets that can form valid triangles.
"""

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
