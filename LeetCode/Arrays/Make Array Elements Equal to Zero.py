"""
🔗 Problem: Make Array Elements Equal to Zero
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/make-array-elements-equal-to-zero/

📝 Description:
   Count ways to choose starting position to make all elements zero.
"""

class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0
        ans = 0

        for x in nums:
            if x == 0:
                right = total - left  # since x == 0, right = sum(nums[i+1:])
                diff = abs(left - right)
                if diff == 0:
                    ans += 2
                elif diff == 1:
                    ans += 1
            left += x

        return ans
