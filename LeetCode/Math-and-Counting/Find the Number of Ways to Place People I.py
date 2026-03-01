"""
🔗 Problem: Find the Number of Ways to Place People I
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

📝 Description:
   Count valid placements of Alice and Bob enclosing no other points.
"""

class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort by x ascending, then y descending
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0

        for i in range(n):
            yi = points[i][1]
            maxY = float("-inf")
            for j in range(i + 1, n):
                yj = points[j][1]
                # We only count pairs when yj is strictly between yi and maxY
                if yi >= yj > maxY:
                    ans += 1
                    maxY = yj
        return ans
