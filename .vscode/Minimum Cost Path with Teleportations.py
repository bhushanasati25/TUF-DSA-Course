class Solution(object):
    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        
        f = [[[INF] * n for _ in range(m)] for _ in range(k + 1)]
        f[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                if i > 0:
                    f[0][i][j] = min(f[0][i][j], f[0][i-1][j] + grid[i][j])
                if j > 0:
                    f[0][i][j] = min(f[0][i][j], f[0][i][j-1] + grid[i][j])
        
        g = defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[grid[i][j]].append((i, j))
        
        keys = sorted(g.keys(), reverse=True)
        
        for t in range(1, k + 1):
            mn = INF
            for val in keys:
                for i, j in g[val]:
                    mn = min(mn, f[t-1][i][j])
                for i, j in g[val]:
                    f[t][i][j] = mn
            
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        f[t][i][j] = min(f[t][i][j], f[t][i-1][j] + grid[i][j])
                    if j > 0:
                        f[t][i][j] = min(f[t][i][j], f[t][i][j-1] + grid[i][j])
        
        return min(f[t][m-1][n-1] for t in range(k + 1))