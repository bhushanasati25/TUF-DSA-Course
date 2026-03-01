"""
🔗 Problem: Longest Subarray of 1's After Deleting One Element
📂 Category: Dynamic-Programming
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

📝 Description:
   Find longest subarray of 1s after deleting exactly one element.
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zero_count = 0
        best = 0

        for right, v in enumerate(nums):
            if v == 0:
                zero_count += 1

            # shrink window until it has at most one zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # must delete one element (either the single zero or a one if none)
            best = max(best, (right - left + 1) - 1)

        return best
