"""
🔗 Problem: Water Bottles
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/water-bottles/

📝 Description:
   Max bottles you can drink by exchanging empty bottles.
"""

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drunk = numBottles
        empties = numBottles
        
        while empties >= numExchange:
            new_bottles = empties // numExchange
            drunk += new_bottles
            empties = empties % numExchange + new_bottles
        
        return drunk
