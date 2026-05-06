class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        for i in range(m):
            empty_idx = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty_idx = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j], boxGrid[i][empty_idx] = boxGrid[i][empty_idx], boxGrid[i][j]
                    empty_idx -= 1
                    
        rotated_box = [[""] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = boxGrid[i][j]
                
        return rotated_box