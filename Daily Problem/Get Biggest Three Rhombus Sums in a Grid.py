class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        unique_sums = set()
        
        for i in range(m):
            for j in range(n):
                unique_sums.add(grid[i][j])
                
                L = 1
                while i + 2 * L < m and j - L >= 0 and j + L < n:
                    current_sum = 0
                    
                    for k in range(L):
                        current_sum += grid[i + k][j + k]
                    
                    for k in range(L):
                        current_sum += grid[i + L + k][j + L - k]
                    
                    for k in range(L):
                        current_sum += grid[i + 2 * L - k][j - k]
                    
                    for k in range(L):
                        current_sum += grid[i + L - k][j - L + k]
                        
                    unique_sums.add(current_sum)
                    L += 1
                    
        return sorted(list(unique_sums), reverse=True)[:3]