"""
🔗 Problem: Count Total Number of Colored Cells
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/count-total-number-of-colored-cells/

📝 Description:
   Count colored cells after n minutes of diamond-pattern coloring.
"""

class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """

        return n * n + (n - 1) * (n - 1)
        