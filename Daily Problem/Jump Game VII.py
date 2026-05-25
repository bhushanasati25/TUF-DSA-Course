class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        if s[-1] == '1': 
            return False
            
        n = len(s)
        dp = [False] * n
        dp[0] = True
        
        reachable_in_window = 0
        
        for i in range(1, n):
            if i >= minJump:
                reachable_in_window += dp[i - minJump]
            
            if i > maxJump:
                reachable_in_window -= dp[i - maxJump - 1]
                
            if s[i] == '0' and reachable_in_window > 0:
                dp[i] = True
                
        return dp[-1]