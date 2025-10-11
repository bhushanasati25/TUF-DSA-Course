class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        from collections import Counter
        from bisect import bisect_right

        if not power:
            return 0

        cnt = Counter(power)
        vals = sorted(cnt.keys())
        sums = [v * cnt[v] for v in vals] 

        dp = [0] * (len(vals) + 1)

        for i, v in enumerate(vals, 1):
            j = bisect_right(vals, v - 3)
            take = sums[i - 1] + dp[j]  
            skip = dp[i - 1]             
            dp[i] = max(take, skip)

        return dp[-1]
