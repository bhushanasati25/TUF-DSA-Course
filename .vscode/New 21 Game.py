class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        # If we never draw (k == 0) or even the maximum overshoot cannot exceed n
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window = 1.0  # sum of last maxPts dp's that are < k
        res = 0.0

        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                # While still drawing, dp[i] contributes to future states
                window += dp[i]
            else:
                # Once i >= k, game stops; add to result
                res += dp[i]
            # Slide window: remove dp[i - maxPts] if it's part of the window
            if i - maxPts >= 0 and i - maxPts < k:
                window -= dp[i - maxPts]

        return res
