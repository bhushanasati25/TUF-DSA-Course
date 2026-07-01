class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        if n == 1:
            return (r - l + 1) % MOD
            
        k = r - l + 1
        
        dp_up = [0] * k
        dp_down = [0] * k
        
        for v in range(k):
            dp_up[v] = v
            dp_down[v] = k - 1 - v
            
        for length in range(3, n + 1):
            new_dp_up = [0] * k
            new_dp_down = [0] * k
            
            running_sum_down = 0
            for v in range(k):
                new_dp_up[v] = running_sum_down
                running_sum_down = (running_sum_down + dp_down[v]) % MOD
                
            running_sum_up = 0
            for v in range(k - 1, -1, -1):
                new_dp_down[v] = running_sum_up
                running_sum_up = (running_sum_up + dp_up[v]) % MOD
                
            dp_up = new_dp_up
            dp_down = new_dp_down
            
        return (sum(dp_up) + sum(dp_down)) % MOD