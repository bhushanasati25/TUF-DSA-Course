class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        # Start from the last row (copy so we don't mutate input)
        dp = triangle[-1][:]

        # Bottom-up: each dp[j] becomes the min path sum from (i, j) to bottom
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
