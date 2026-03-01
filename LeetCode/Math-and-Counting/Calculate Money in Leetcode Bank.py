"""
🔗 Problem: Calculate Money in Leetcode Bank
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/calculate-money-in-leetcode-bank/

📝 Description:
   Calculate total savings with weekly incrementing daily deposits.
"""

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        days = n % 7
        total = 0
        for i in range(weeks):
            total += 28 + i * 7  

        start = weeks + 1
        for j in range(days):
            total += start + j
            
        return total
