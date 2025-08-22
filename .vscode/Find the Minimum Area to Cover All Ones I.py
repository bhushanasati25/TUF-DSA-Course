class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0

        top = m
        bottom = -1
        left = n
        right = -1

        for r in range(m):
            row = grid[r]
            for c in range(n):
                if row[c] == 1:
                    if r < top: top = r
                    if r > bottom: bottom = r
                    if c < left: left = c
                    if c > right: right = c

        if bottom == -1:  # no 1s present
            return 0

        return (bottom - top + 1) * (right - left + 1)
