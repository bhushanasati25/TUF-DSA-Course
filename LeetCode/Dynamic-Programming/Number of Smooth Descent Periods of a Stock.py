"""
🔗 Problem: Number of Smooth Descent Periods of a Stock
📂 Category: Dynamic-Programming
🎯 Difficulty: Medium
🔗 URL: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

📝 Description:
   Count smooth descent periods where price drops by 1 each day.
"""

class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0          # total smooth descent periods
        curr = 0         # length of current smooth descent streak

        for i in range(len(prices)):
            # check if we can extend the descent
            if i > 0 and prices[i] == prices[i - 1] - 1:
                curr += 1
            else:
                curr = 1

            ans += curr  # add all descent periods ending at i

        return ans
