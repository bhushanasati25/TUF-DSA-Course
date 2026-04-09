class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        S = int(n ** 0.5) 
        
        small_queries = defaultdict(list)
        multiplier = [1] * n
        
        def modInverse(x):
            return pow(x, MOD - 2, MOD)
            
        for l, r, k, v in queries:
            if k > S:
                idx = l
                while idx <= r:
                    multiplier[idx] = (multiplier[idx] * v) % MOD
                    idx += k
            else:
                small_queries[k].append((l, r, v))
                
        for k, qs in small_queries.items():
            diff = [1] * n
            
            for l, r, v in qs:
                diff[l] = (diff[l] * v) % MOD
                end = l + ((r - l) // k + 1) * k
                
                if end < n:
                    diff[end] = (diff[end] * modInverse(v)) % MOD
            
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                multiplier[i] = (multiplier[i] * diff[i]) % MOD
                
        ans = 0
        for i in range(n):
            final_val = (nums[i] * multiplier[i]) % MOD
            ans ^= final_val
            
        return ans