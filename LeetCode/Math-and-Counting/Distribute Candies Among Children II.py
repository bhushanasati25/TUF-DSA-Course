"""
🔗 Problem: Distribute Candies Among Children II
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/distribute-candies-among-children-ii/

📝 Description:
   Count ways to distribute n candies to 3 children with limit.
"""

class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
    
        def ways(m):
            if m < 0:
                return 0
            return (m + 2) * (m + 1) // 2

        if n > 3 * limit:
            return 0

        t = limit + 1
        total = ways(n)
        total -= 3 * ways(n - t)
        total += 3 * ways(n - 2 * t)
        total -= ways(n - 3 * t)
        return total
