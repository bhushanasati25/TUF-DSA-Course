class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
            
            sorted_heights = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                if sorted_heights[j] == 0:
                    break
                
                max_area = max(max_area, sorted_heights[j] * (j + 1))
                
        return max_area