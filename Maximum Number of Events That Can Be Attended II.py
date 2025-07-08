from bisect import bisect_left

class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 1) sort events by start day
        events.sort(key=lambda e: e[0])
        n = len(events)
        starts = [e[0] for e in events]
        
        # 2) dp[j][i] = max value attending j events from events[i:]
        # +1 so dp[*][n] = 0 (base case)
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        
        # 3) fill table for j = 1..k, i = n-1..0
        for j in range(1, k + 1):
            for i in range(n - 1, -1, -1):
                # option A: skip events[i]
                best = dp[j][i + 1]
                # option B: take events[i]
                end_i, val_i = events[i][1], events[i][2]
                # find first index with start > end_i
                nxt = bisect_left(starts, end_i + 1)
                best = max(best, val_i + dp[j - 1][nxt])
                
                dp[j][i] = best
        
        return dp[k][0]
