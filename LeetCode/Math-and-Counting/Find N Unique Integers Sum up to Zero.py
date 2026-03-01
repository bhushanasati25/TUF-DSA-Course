"""
🔗 Problem: Find N Unique Integers Sum up to Zero
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

📝 Description:
   Return n unique integers that sum to zero.
"""

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, n // 2 + 1):
            res.extend([i, -i])
        if n % 2 == 1:
            res.append(0)
        return res
