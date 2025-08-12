class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10**9 + 7
        
        max_base = 1
        while (max_base ** x) <= n:
            max_base += 1
        max_base -= 1

        memo = {}

        def dfs(remaining, current):
            if remaining == 0:
                return 1
            if remaining < 0 or current > max_base:
                return 0

            if (remaining, current) in memo:
                return memo[(remaining, current)]

            include = dfs(remaining - current**x, current + 1)
            exclude = dfs(remaining, current + 1)

            memo[(remaining, current)] = (include + exclude) % MOD
            return memo[(remaining, current)]

        return dfs(n, 1)


Code