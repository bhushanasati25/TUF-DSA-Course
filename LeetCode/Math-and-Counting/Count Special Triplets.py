"""
🔗 Problem: Count Special Triplets
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/count-special-triplets/

📝 Description:
   Count triplets (i,j,k) satisfying special conditions.
"""

from collections import Counter

class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        left = Counter()
        right = Counter(nums)
        ans = 0

        for x in nums:
            right[x] -= 1

            target = x * 2
            ans = (ans + left[target] * right[target]) % MOD
            left[x] += 1

        return ans
