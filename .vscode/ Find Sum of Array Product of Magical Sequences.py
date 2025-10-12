class Solution(object):
    def magicalSum(self, m, k, nums):
        """
        :type m: int
        :type k: int
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # nCk modulo MOD (precompute factorials up to m)
        fact = [1]*(m+1)
        for i in range(1, m+1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1]*(m+1)
        invfact[m] = pow(fact[m], MOD-2, MOD)
        for i in range(m, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD

        def nCk(n_, k_):
            if k_ < 0 or k_ > n_:
                return 0
            return fact[n_] * invfact[k_] % MOD * invfact[n_-k_] % MOD

        # Precompute powers nums[i]^t % MOD for t in [0..m]
        pow_tbl = [[1]*(m+1) for _ in range(n)]
        for i, x in enumerate(nums):
            x %= MOD
            for t in range(1, m+1):
                pow_tbl[i][t] = (pow_tbl[i][t-1] * x) % MOD

        # dp[used] is a dict: (carry, bits) -> ways
        from collections import defaultdict
        dp = [defaultdict(int) for _ in range(m+1)]
        dp[0][(0, 0)] = 1

        for i in range(n):
            new_dp = [defaultdict(int) for _ in range(m+1)]
            for used in range(m+1):
                if not dp[used]:
                    continue
                rem = m - used
                for (carry, bits), ways in dp[used].items():
                    if ways == 0:
                        continue
                    # Assign t occurrences of index i among remaining positions
                    for t in range(rem + 1):
                        choose = nCk(rem, t)
                        val = ways * choose % MOD
                        val = val * pow_tbl[i][t] % MOD

                        s = carry + t
                        bit_i = s & 1
                        new_carry = s >> 1
                        new_bits = bits + bit_i
                        if new_bits > k:
                            continue  # prune impossible states early

                        new_used = used + t
                        new_dp[new_used][(new_carry, new_bits)] = (new_dp[new_used][(new_carry, new_bits)] + val) % MOD
            dp = new_dp

        # Finalize: add popcount of remaining carry and require used == m
        def popcount(x):
            return x.bit_count() if hasattr(int(), "bit_count") else bin(x).count("1")

        ans = 0
        for (carry, bits), ways in dp[m].items():
            if bits + popcount(carry) == k:
                ans = (ans + ways) % MOD
        return ans
