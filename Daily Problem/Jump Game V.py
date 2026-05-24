class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        dp = {}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            
            max_jumps = 1
            
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dfs(j))
                
            dp[i] = max_jumps
            return dp[i]
            
        return max(dfs(i) for i in range(n))