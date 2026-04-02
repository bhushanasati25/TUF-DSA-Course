class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        m, n = len(coins), len(coins[0])
        dp = [[float('-inf')] * 3 for _ in range(n)]
        
        if coins[0][0] >= 0:
            dp[0][0] = coins[0][0]
        else:
            dp[0][0] = coins[0][0]
            dp[0][1] = 0
            
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = coins[i][j]
                new_dp = [float('-inf')] * 3
                
                for k in range(3):
                    prev = float('-inf')
                    
                    if i > 0: prev = max(prev, dp[j][k])
                    if j > 0: prev = max(prev, dp[j-1][k])
                        
                    if prev != float('-inf'):
                        new_dp[k] = max(new_dp[k], prev + val)
                        
                    if val < 0 and k > 0:
                        prev_k_minus_1 = float('-inf')
                        if i > 0: prev_k_minus_1 = max(prev_k_minus_1, dp[j][k-1])
                        if j > 0: prev_k_minus_1 = max(prev_k_minus_1, dp[j-1][k-1])
                            
                        if prev_k_minus_1 != float('-inf'):
                            new_dp[k] = max(new_dp[k], prev_k_minus_1)
                            
                dp[j] = new_dp
                
        return max(dp[-1])