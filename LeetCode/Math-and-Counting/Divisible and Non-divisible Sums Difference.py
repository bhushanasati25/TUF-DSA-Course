"""
🔗 Problem: Divisible and Non-divisible Sums Difference
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

📝 Description:
   Difference of sums: not divisible by m minus divisible by m.
"""

class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        total_sum = n * (n + 1) // 2
        k = n // m
        sum_div = m * k * (k + 1) // 2
        return total_sum - 2 * sum_div
