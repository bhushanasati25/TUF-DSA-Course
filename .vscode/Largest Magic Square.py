class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        rowPrefix = [[0] * (n + 1) for _ in range(m)]
        colPrefix = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j]
                colPrefix[i + 1][j] = colPrefix[i][j] + grid[i][j]
        
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    
                    target = rowPrefix[i][j + k] - rowPrefix[i][j]
                    
                    valid = True
                    
                    for r in range(i, i + k):
                        if rowPrefix[r][j + k] - rowPrefix[r][j] != target:
                            valid = False
                            break
                    
                    if not valid:
                        continue
                    
                    for c in range(j, j + k):
                        if colPrefix[i + k][c] - colPrefix[i][c] != target:
                            valid = False
                            break
                    
                    if not valid:
                        continue
                    
                    diag1 = 0
                    diag2 = 0
                    for d in range(k):
                        diag1 += grid[i + d][j + d]
                        diag2 += grid[i + d][j + k - 1 - d]
                    
                    if diag1 == target and diag2 == target:
                        return k
    
        return 1
