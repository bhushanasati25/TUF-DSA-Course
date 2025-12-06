from collections import deque

MOD = 10**9 + 7

class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        dp = [0] * (n + 1)
        dp[0] = 1  
        
        pref = [0] * (n + 1)
        pref[0] = 1
        
        minD = deque()  
        maxD = deque() 
        
        l = 0  
        
        for r, x in enumerate(nums):
            while minD and nums[minD[-1]] >= x:
                minD.pop()
            minD.append(r)
            
            while maxD and nums[maxD[-1]] <= x:
                maxD.pop()
            maxD.append(r)
            
            while nums[maxD[0]] - nums[minD[0]] > k:
                l += 1
                if minD[0] < l:
                    minD.popleft()
                if maxD[0] < l:
                    maxD.popleft()
            
            if l == 0:
                total = pref[r]              
            else:
                total = (pref[r] - pref[l-1]) % MOD  
            
            dp[r + 1] = total
            pref[r + 1] = (pref[r] + dp[r + 1]) % MOD
        
        return dp[n]
