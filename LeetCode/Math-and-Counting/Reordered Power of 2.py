"""
🔗 Problem: Reordered Power of 2
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/reordered-power-of-2/

📝 Description:
   Check if digits can be reordered to form a power of 2.
"""

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def count_digits(x):
            cnt = [0] * 10
            while x:
                x, d = divmod(x, 10)
                cnt[d] += 1
            return cnt

        target = count_digits(n)
        i = 1
        while i <= 10**9:  # covers all powers of 2 within constraints
            if count_digits(i) == target:
                return True
            i <<= 1  # multiply by 2
        return False
