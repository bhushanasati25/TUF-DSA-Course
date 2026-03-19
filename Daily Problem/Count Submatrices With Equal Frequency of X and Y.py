class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        prefix_x = [0] * n
        prefix_y = [0] * n
        ans = 0
        
        for i in range(m):
            row_x = 0
            row_y = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    row_x += 1
                elif grid[i][j] == 'Y':
                    row_y += 1
                
                prefix_x[j] += row_x
                prefix_y[j] += row_y
                
                if prefix_x[j] > 0 and prefix_x[j] == prefix_y[j]:
                    ans += 1
                    
        return ans