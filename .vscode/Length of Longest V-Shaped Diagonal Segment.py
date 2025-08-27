class Solution(object):
    def lenOfVDiagonal(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        DIRS = ((-1, 1), (1, 1), (1, -1), (-1, -1))  # NE, SE, SW, NW
        memo = {}

        def dfs(i, j, turned, expect, dir_idx):
            key = (i, j, turned, expect, dir_idx)
            if key in memo:
                return memo[key]

            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != expect:
                return 0

            nxt = 0 if expect == 2 else 2
            dx, dy = DIRS[dir_idx]
            best = 1 + dfs(i + dx, j + dy, turned, nxt, dir_idx)

            if not turned:
                ndir = (dir_idx + 1) % 4
                ndx, ndy = DIRS[ndir]
                best = max(best, 1 + dfs(i + ndx, j + ndy, True, nxt, ndir))

            memo[key] = best
            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d in range(4):
                        dx, dy = DIRS[d]
                        ans = max(ans, 1 + dfs(i + dx, j + dy, False, 2, d))
        return ans
