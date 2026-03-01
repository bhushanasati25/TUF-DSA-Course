"""
🔗 Problem: Number of Ways to Paint N × 3 Grid
📂 Category: Dynamic-Programming
🎯 Difficulty: Hard
🔗 URL: https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

📝 Description:
   Count ways to paint an N×3 grid with 3 colors, no adjacent same.
"""

class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        typeA = 6
        typeB = 6

        for _ in range(1, n):
            newA = (typeA * 3 + typeB * 2) % MOD
            newB = (typeA * 2 + typeB * 2) % MOD
            typeA, typeB = newA, newB

        return (typeA + typeB) % MOD
