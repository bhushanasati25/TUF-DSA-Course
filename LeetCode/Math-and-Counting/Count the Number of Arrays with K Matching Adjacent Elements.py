class Solution(object):
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Precompute factorials and inverse factorials up to n
        maxN = n
        fact = [1] * (maxN)
        inv_fact = [1] * (maxN)

        for i in range(1, maxN):
            fact[i] = fact[i - 1] * i % MOD

        # Fermat's Little Theorem for modular inverse
        inv_fact[maxN - 1] = pow(fact[maxN - 1], MOD - 2, MOD)
        for i in range(maxN - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        # Apply the formula: C(n-1, k) * m * (m-1)^(n-1-k)
        result = comb(n - 1, k) * m % MOD
        result = result * pow(m - 1, n - 1 - k, MOD) % MOD
        return result
