"""
🔗 Problem: Minimum Time Visiting All Points
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/minimum-time-visiting-all-points/

📝 Description:
   Min time to visit all points moving in 8 directions.
"""

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            total_time += max(dx, dy)
        
        return total_time
        