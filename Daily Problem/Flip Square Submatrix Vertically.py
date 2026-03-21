class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(k // 2):
            r1 = x + i
            r2 = x + k - 1 - i
            
            for j in range(y, y + k):
                grid[r1][j], grid[r2][j] = grid[r2][j], grid[r1][j]
        
        return grid
        