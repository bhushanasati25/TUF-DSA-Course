class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """

        n = len(prices)
        if n == 0 or k == 0:
            return 0

        NEG_INF = float('-inf')

        dp = [[0, NEG_INF, NEG_INF] for _ in range(k + 1)]

        for price in prices:
            new_dp = [[dp[j][0], dp[j][1], dp[j][2]] for j in range(k + 1)]

            for j in range(k + 1):
                if dp[j][1] != NEG_INF:
                    new_dp[j][0] = max(new_dp[j][0], dp[j][1] + price)
                if dp[j][2] != NEG_INF:
                    new_dp[j][0] = max(new_dp[j][0], dp[j][2] - price)
                if j > 0:
                    new_dp[j][1] = max(new_dp[j][1], dp[j - 1][0] - price)
                    new_dp[j][2] = max(new_dp[j][2], dp[j - 1][0] + price)

            dp = new_dp

        return dp[k][0]
