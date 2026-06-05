class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def solve(x):
            if x <= 0:
                return 0
            
            limit = str(x)
            memo = {}
            
            def dfs(idx, prev1, prev2, is_tight, is_leading_zero):
                if idx == len(limit):
                    return (1, 0)
                
                state = (idx, prev1, prev2, is_tight, is_leading_zero)
                if state in memo:
                    return memo[state]
                
                ans_count = 0
                ans_waviness = 0
                upper_bound = int(limit[idx]) if is_tight else 9
                
                for d in range(upper_bound + 1):
                    new_tight = is_tight and (d == upper_bound)
                    new_zero = is_leading_zero and (d == 0)
                    
                    if new_zero:
                        new_prev1, new_prev2 = -1, -1
                    else:
                        new_prev1 = d
                        new_prev2 = prev1 if not is_leading_zero else -1
                        
                    res_count, res_waviness = dfs(idx + 1, new_prev1, new_prev2, new_tight, new_zero)
                    
                    ans_count += res_count
                    ans_waviness += res_waviness
                    
                    if not is_leading_zero and prev2 != -1:
                        is_peak = (prev2 < prev1 and prev1 > d)
                        is_valley = (prev2 > prev1 and prev1 < d)
                        
                        if is_peak or is_valley:
                            ans_waviness += res_count
                            
                memo[state] = (ans_count, ans_waviness)
                return memo[state]
            
            return dfs(0, -1, -1, True, True)[1]
            
        return solve(num2) - solve(num1 - 1)