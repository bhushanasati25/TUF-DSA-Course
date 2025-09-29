class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        for length in range(3, n+1):            
            for i in range(0, n - length + 1):
                j = i + length - 1
                best = float('inf')
                for k in range(i+1, j):
                    score = dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]
                    if score < best:
                        best = score
                dp[i][j] = best
        return dp[0][n-1]
