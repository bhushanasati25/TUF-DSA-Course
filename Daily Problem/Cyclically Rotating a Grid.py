class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer
            
            elements = []
            
            for j in range(left, right + 1):
                elements.append(grid[top][j])
            
            for i in range(top + 1, bottom + 1):
                elements.append(grid[i][right])
            
            for j in range(right - 1, left - 1, -1):
                elements.append(grid[bottom][j])
            
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])
            
            L = len(elements)
            shift = k % L
            rotated = elements[shift:] + elements[:shift]
            
            idx = 0
            
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1
                
            for i in range(top + 1, bottom + 1):
                grid[i][right] = rotated[idx]
                idx += 1
                
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
                
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid