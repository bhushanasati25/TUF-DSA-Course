class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        
        # Step 1: Get powers of 2 from n's binary form
        powers = []
        bit = 0
        while n:
            if n & 1:
                powers.append(1 << bit)
            bit += 1
            n >>= 1
        
        # Step 2: Prefix product array
        prefix = [1] * len(powers)
        prefix[0] = powers[0] % MOD
        for i in range(1, len(powers)):
            prefix[i] = (prefix[i-1] * powers[i]) % MOD
        
        # Step 3: Answer queries
        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix[r] % MOD)
            else:
                res.append((prefix[r] * pow(prefix[l-1], MOD-2, MOD)) % MOD)
        return res
