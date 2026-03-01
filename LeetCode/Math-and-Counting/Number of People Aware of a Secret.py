"""
🔗 Problem: Number of People Aware of a Secret
📂 Category: Math-and-Counting
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/number-of-people-aware-of-a-secret/

📝 Description:
   Count people knowing a secret after it spreads with delay/forget.
"""

class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)   # dp[d] = # who learn the secret on day d
        dp[1] = 1            # day 1: one person knows
        active = 0           # # of people who can share on current day

        for day in range(2, n + 1):
            if day - delay >= 1:
                active = (active + dp[day - delay]) % MOD   # start sharing today
            if day - forget >= 1:
                active = (active - dp[day - forget]) % MOD  # forget today (stop sharing)
            dp[day] = active                                # new learners today

        # People who still remember on day n (haven't reached forget window)
        start = max(1, n - forget + 1)
        return sum(dp[start:n + 1]) % MOD
