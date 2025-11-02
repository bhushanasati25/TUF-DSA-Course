class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        EMPTY, WALL, GUARD = 0, 1, 2

        grid = [[EMPTY] * n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = WALL
        for r, c in guards:
            grid[r][c] = GUARD

        seen = [[False] * n for _ in range(m)]

        # Row sweeps
        for r in range(m):
            active = False
            for c in range(n):
                if grid[r][c] == WALL:
                    active = False
                elif grid[r][c] == GUARD:
                    active = True
                else:
                    if active:
                        seen[r][c] = True

            active = False
            for c in range(n - 1, -1, -1):
                if grid[r][c] == WALL:
                    active = False
                elif grid[r][c] == GUARD:
                    active = True
                else:
                    if active:
                        seen[r][c] = True

        # Column sweeps
        for c in range(n):
            active = False
            for r in range(m):
                if grid[r][c] == WALL:
                    active = False
                elif grid[r][c] == GUARD:
                    active = True
                else:
                    if active:
                        seen[r][c] = True

            active = False
            for r in range(m - 1, -1, -1):
                if grid[r][c] == WALL:
                    active = False
                elif grid[r][c] == GUARD:
                    active = True
                else:
                    if active:
                        seen[r][c] = True

        # Count cells that are empty and unseen
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == EMPTY and not seen[r][c]:
                    ans += 1
        return ans
