class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        for l, r, k, v in queries:
            if v == 1:
                continue
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        
        ans = 0
        for x in nums:
            ans ^= x
            
        return ans