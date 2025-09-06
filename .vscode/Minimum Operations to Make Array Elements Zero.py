class Solution(object):
    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        def tier_sum(x):
            """
            f(x) = sum_{v=1..x} p(v), where p(v) is the smallest p with 4^p > v.
            Computed by summing full/partial tiers [4^(i-1), 4^i - 1].
            """
            if x <= 0:
                return 0
            res = 0
            tier_start = 1   # 4^(i-1)
            i = 1            # p-value for this tier
            while tier_start <= x:
                tier_end = tier_start * 4 - 1  # 4^i - 1
                cnt = min(tier_end, x) - tier_start + 1
                if cnt > 0:
                    res += cnt * i
                i += 1
                tier_start *= 4
            return res

        ans = 0
        for l, r in queries:
            s = tier_sum(r) - tier_sum(l - 1)   # sum of p(v) on [l, r]
            # p(r) = tier_sum(r) - tier_sum(r - 1) since p is stepwise-constant
            mx = tier_sum(r) - tier_sum(r - 1)
            ans += max((s + 1) // 2, mx)
        return ans
