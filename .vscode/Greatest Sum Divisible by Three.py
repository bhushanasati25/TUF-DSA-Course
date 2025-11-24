class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEG_INF = -10**18
        dp = [0, NEG_INF, NEG_INF]  

        for x in nums:
            r = x % 3
            prev = dp[:]   
            for pr in range(3):
                nr = (pr + r) % 3
                dp[nr] = max(dp[nr], prev[pr] + x)

        return dp[0]
