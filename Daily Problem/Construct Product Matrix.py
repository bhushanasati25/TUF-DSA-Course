class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        m = len(grid[0])
        
        p = [[0] * m for i in range(n)]
        
        pref = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = pref
                pref = (pref * grid[i][j]) % 12345
                
        suff = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suff) % 12345
                suff = (suff * grid[i][j]) % 12345
                
        return p