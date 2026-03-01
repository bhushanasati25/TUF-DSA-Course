"""
🔗 Problem: Count Number of Trapezoids I
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/count-number-of-trapezoids-i/

📝 Description:
   Count quadrilaterals forming trapezoids from given points.
"""

from collections import Counter

class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        ycount = Counter()
        for x, y in points:
            ycount[y] += 1

        segs = []
        for cnt in ycount.values():
            if cnt >= 2:
                segs.append(cnt * (cnt - 1) // 2)

        total = 0
        prefix = 0
        for s in segs:
            total = (total + s * prefix) % MOD
            prefix = (prefix + s) % MOD

        return total
