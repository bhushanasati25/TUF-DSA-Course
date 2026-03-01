"""
🔗 Problem: Smallest Missing Non-negative Integer After Operations
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

📝 Description:
   Find smallest missing non-negative integer after adding k multiples.
"""

from collections import Counter

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        cnt = Counter(n % value for n in nums)  # remainders multiset

        x = 0
        while True:
            r = x % value
            if cnt[r] > 0:
                cnt[r] -= 1
                x += 1
            else:
                return x
