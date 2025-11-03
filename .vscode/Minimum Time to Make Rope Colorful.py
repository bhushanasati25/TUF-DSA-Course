class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        n = len(colors)
        if n <= 1:
            return 0

        ans = 0
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                ans += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])  
        return ans
