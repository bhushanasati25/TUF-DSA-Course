class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        for r in range(m):
            new_dp = [[-1] * (k + 1) for _ in range(n)]
            for c in range(n):
                if r == 0 and c == 0:
                    new_dp[0][0] = 0
                    continue
                    
                cell_score = grid[r][c]
                cell_cost = 1 if grid[r][c] > 0 else 0
                
                if r > 0 and c > 0:
                    merged_prev = [a if a > b else b for a, b in zip(new_dp[c-1], dp[c])]
                elif r > 0:
                    merged_prev = dp[c]
                else:
                    merged_prev = new_dp[c-1]
                    
                if cell_cost == 0:
                    new_dp[c] = list(merged_prev)
                else:
                    new_dp[c] = [-1] + [
                        v + cell_score if v != -1 else -1 
                        for v in merged_prev[:-1]
                    ]
            dp = new_dp
            
        ans = max(dp[n - 1])
        return ans if ans != -1 else -1