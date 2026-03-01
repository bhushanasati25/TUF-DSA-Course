"""
🔗 Problem: Number of Zero-Filled Subarrays
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/number-of-zero-filled-subarrays/

📝 Description:
   Count subarrays filled entirely with zeros.
"""

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        run = 0
        for x in nums:
            if x == 0:
                run += 1      # extend current zero-run
                ans += run    # add subarrays ending here
            else:
                run = 0       # reset on non-zero
        return ans
