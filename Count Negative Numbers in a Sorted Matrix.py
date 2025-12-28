class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        count = 0

        while i >= 0 and j < n:
            if grid[i][j] < 0:
                # all elements to the right are also negative
                count += (n - j)
                i -= 1
            else:
                j += 1

        return count
