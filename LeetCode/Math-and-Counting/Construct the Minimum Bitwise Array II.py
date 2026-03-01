"""
🔗 Problem: Construct the Minimum Bitwise Array II
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

📝 Description:
   Efficiently construct minimum bitwise array for large inputs.
"""

class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            if n == 2:
                res.append(-1)
            else:
                lowest_bit_above_trailing_ones = (n + 1) & -(n + 1)
                res.append(n - (lowest_bit_above_trailing_ones >> 1))
        
        return res