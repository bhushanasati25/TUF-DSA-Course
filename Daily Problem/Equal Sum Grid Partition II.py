class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        total_sum = sum(sum(row) for row in grid)
        
        def check(g):
            rows, cols = len(g), len(g[0])
            top_sum = 0
            seen = set()
            
            for i in range(rows - 1):
                for j in range(cols):
                    top_sum += g[i][j]
                    seen.add(g[i][j])
                
                bot_sum = total_sum - top_sum
                diff = top_sum - bot_sum
                
                if diff == 0:
                    return True
                
                if diff > 0:
                    if i > 0 and cols > 1:
                        if diff in seen:
                            return True
                    elif i == 0:
                        if g[0][0] == diff or g[0][-1] == diff:
                            return True
                    else:
                        if g[0][0] == diff or g[i][0] == diff:
                            return True
            return False

        def transpose(g):
            return [list(x) for x in zip(*g)]

        def reverse_rows(g):
            return g[::-1]

        return (check(grid) or 
                check(reverse_rows(grid)) or 
                check(transpose(grid)) or 
                check(reverse_rows(transpose(grid))))
        