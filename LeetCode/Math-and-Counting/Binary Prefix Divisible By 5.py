"""
🔗 Problem: Binary Prefix Divisible By 5
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/binary-prefix-divisible-by-5/

📝 Description:
   Check if each binary prefix is divisible by 5.
"""

class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = []
        val = 0

        for b in nums:
            val = ((val << 1) + b) % 5
            res.append(val == 0)

        return res
