"""
🔗 Problem: Find Closest Person
📂 Category: Arrays
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/find-closest-person/

📝 Description:
   Find the person closest to a given position.
"""

class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        dx = abs(x - z)
        dy = abs(y - z)
        
        if dx == dy:
            return 0
        return 1 if dx < dy else 2
