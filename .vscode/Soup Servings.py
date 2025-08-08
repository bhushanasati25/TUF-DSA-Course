class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        # Optimization for large n
        if n > 4800:
            return 1.0
        
        # Scale down
        N = (n + 24) // 25
        
        memo = {}
        
        def dp(a, b):
            # Check memoized results
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            # Recursive calculation
            res = 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
            
            memo[(a, b)] = res
            return res
        
        return dp(N, N)
