class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
            
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i-1], nums[i])
            
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suff_min[i] = min(suff_min[i+1], nums[i])
            
        ans = [0] * n
        L = 0
        
        for k in range(n - 1):
            if pref_max[k] <= suff_min[k+1]:
                for i in range(L, k + 1):
                    ans[i] = pref_max[k]
                L = k + 1
                
        for i in range(L, n):
            ans[i] = pref_max[-1]
            
        return ans