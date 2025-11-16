class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        streak = 0  
        
        for ch in s:
            if ch == '1':
                streak += 1          
                ans = (ans + streak) % MOD  
            else:
                streak = 0          
        
        return ans
