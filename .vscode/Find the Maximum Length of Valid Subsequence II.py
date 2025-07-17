class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [[0] * k for _ in range(k)]
        ans = 0
        
        for x in nums:
            xm = x % k
            for prev in range(k):
                dp[prev][xm] = dp[xm][prev] + 1
                ans = max(ans, dp[prev][xm])
        
        return ans
