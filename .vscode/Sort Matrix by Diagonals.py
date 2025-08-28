class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        if not grid or not grid[0]:
            return grid

        m, n = len(grid), len(grid[0])

        # (A) Main diagonal (0,0) -> descending
        i = j = 0
        vals = []
        while i < m and j < n:
            vals.append(grid[i][j])
            i += 1; j += 1
        vals.sort(reverse=True)
        i = j = 0
        k = 0
        while i < m and j < n:
            grid[i][j] = vals[k]
            i += 1; j += 1; k += 1

        # (B) Diagonals starting on the top row (j >= 1) -> ascending
        for start_j in range(1, n):
            i, j = 0, start_j
            vals = []
            while i < m and j < n:
                vals.append(grid[i][j])
                i += 1; j += 1
            vals.sort()
            i, j = 0, start_j
            k = 0
            while i < m and j < n:
                grid[i][j] = vals[k]
                i += 1; j += 1; k += 1

        # (C) Diagonals starting on the first column (i >= 1) -> descending
        for start_i in range(1, m):
            i, j = start_i, 0
            vals = []
            while i < m and j < n:
                vals.append(grid[i][j])
                i += 1; j += 1
            vals.sort(reverse=True)
            i, j = start_i, 0
            k = 0
            while i < m and j < n:
                grid[i][j] = vals[k]
                i += 1; j += 1; k += 1

        return grid
