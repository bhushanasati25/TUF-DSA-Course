class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        # Area of the tight bounding rectangle of 1s in submatrix [i1..i2] x [j1..j2].
        # If the submatrix has no 1s, return +inf so this split won't be chosen.
        def area(i1, j1, i2, j2):
            x1 = y1 = INF
            x2 = y2 = -INF
            for i in range(i1, i2 + 1):
                row = grid[i]
                for j in range(j1, j2 + 1):
                    if row[j] == 1:
                        if i < x1: x1 = i
                        if j < y1: y1 = j
                        if i > x2: x2 = i
                        if j > y2: y2 = j
            if x1 is INF:      # no 1s in this block
                return INF
            return (x2 - x1 + 1) * (y2 - y1 + 1)

        ans = m * n  # safe upper bound when there are at least 3 ones

        # 1) two horizontal splits
        for i1 in range(m - 1):
            for i2 in range(i1 + 1, m - 1):
                a = area(0, 0, i1, n - 1)
                b = area(i1 + 1, 0, i2, n - 1)
                c = area(i2 + 1, 0, m - 1, n - 1)
                s = a + b + c
                if s < ans: ans = s

        # 2) two vertical splits
        for j1 in range(n - 1):
            for j2 in range(j1 + 1, n - 1):
                a = area(0, 0, m - 1, j1)
                b = area(0, j1 + 1, m - 1, j2)
                c = area(0, j2 + 1, m - 1, n - 1)
                s = a + b + c
                if s < ans: ans = s

        # 3–6) one horizontal + one vertical inside one side (four configurations)
        for i in range(m - 1):
            for j in range(n - 1):
                # top split, then vertical in top (UL + UR + bottom)
                s = (area(0, 0, i, j) +
                     area(0, j + 1, i, n - 1) +
                     area(i + 1, 0, m - 1, n - 1))
                if s < ans: ans = s

                # bottom split, then vertical in bottom (top + LL + LR)
                s = (area(0, 0, i, n - 1) +
                     area(i + 1, 0, m - 1, j) +
                     area(i + 1, j + 1, m - 1, n - 1))
                if s < ans: ans = s

                # left split, then horizontal in left (UL + LL + right)
                s = (area(0, 0, i, j) +
                     area(i + 1, 0, m - 1, j) +
                     area(0, j + 1, m - 1, n - 1))
                if s < ans: ans = s

                # right split, then horizontal in right (left + UR + LR)
                s = (area(0, 0, m - 1, j) +
                     area(0, j + 1, i, n - 1) +
                     area(i + 1, j + 1, m - 1, n - 1))
                if s < ans: ans = s

        return ans
