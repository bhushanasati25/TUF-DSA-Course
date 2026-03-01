"""
🔗 Problem: Count Covered Buildings
📂 Category: Arrays
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/count-covered-buildings/

📝 Description:
   Count buildings covered by taller buildings in all four directions.
"""

class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """

        row_min = {}
        row_max = {}

        col_min = {}
        col_max = {}

        for x, y in buildings:
            if x in row_min:
                if y < row_min[x]:
                    row_min[x] = y
                if y > row_max[x]:
                    row_max[x] = y
            else:
                row_min[x] = row_max[x] = y

            if y in col_min:
                if x < col_min[y]:
                    col_min[y] = x
                if x > col_max[y]:
                    col_max[y] = x
            else:
                col_min[y] = col_max[y] = x

        covered = 0
        for x, y in buildings:

            if row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]:
                covered += 1

        return covered
