class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        # dp_row[j][r] = number of ways to reach cell in previous row at column j with remainder r
        dp_row = [ [0] * k for _ in range(n) ]

        for i in range(m):
            new_row = [ [0] * k for _ in range(n) ]
            for j in range(n):
                val = grid[i][j] % k
                if i == 0 and j == 0:
                    new_row[0][val] = 1
                    continue

                # from top (previous dp_row[j])
                if i > 0:
                    top = dp_row[j]
                    # iterate only remainders (0..k-1)
                    for r in range(k):
                        cnt = top[r]
                        if cnt:
                            new_row[j][ (r + val) % k ] = (new_row[j][ (r + val) % k ] + cnt) % MOD

                # from left (current new_row[j-1])
                if j > 0:
                    left = new_row[j-1]
                    for r in range(k):
                        cnt = left[r]
                        if cnt:
                            new_row[j][ (r + val) % k ] = (new_row[j][ (r + val) % k ] + cnt) % MOD

            dp_row = new_row

        return dp_row[n-1][0] % MOD
